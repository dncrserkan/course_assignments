from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from myapp import db
from myapp.models import Post, Like
from myapp.posts.forms import PostForm, LikeForm, UpdatePostForm
from myapp.posts.utils import save_post_picture, process_like_action, get_user_likes
from datetime import datetime
import pytz


posts = Blueprint('posts', __name__)



@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture=save_post_picture(form.picture.data)
        post = Post(title=form.title.data,
                    content=form.content.data,
                    image_file=picture,
                    author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', form=form, legend='New Post')


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])   # dynamic id for every post
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = LikeForm()

    like_list = get_user_likes()
    temp = process_like_action(form)
    if temp is not None:
        return temp

    return render_template('post.html', post=post, form=form, like_list=like_list, Like=Like)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = UpdatePostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture = save_post_picture(form.picture.data)
            post.image_file = picture
        post.title = form.title.data
        post.content = form.content.data
        post.date_updated = datetime.now(pytz.timezone('UTC'))
        db.session.commit()
        flash('Post is updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    
    likes_to_delete = Like.query.filter_by(post_id=post.id).all()
    for like in likes_to_delete:
        db.session.delete(like)

    db.session.delete(post)
    db.session.commit()
    flash('Post is deleted', 'success')
    return redirect(url_for('main.home'))