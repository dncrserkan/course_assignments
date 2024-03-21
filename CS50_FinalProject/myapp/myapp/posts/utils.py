import os
import secrets
from PIL import Image
from flask import url_for, request, redirect, flash, current_app
from flask_login import current_user
from myapp import db
from myapp.models import Post, Like


def process_like_action(form):
    def create_url(target):
        """ Purpose of this function is not to send 
            extra information other than page needs """
        if target == 'main.home':
            return url_for(target, page=page)
        elif target == 'users.user_posts':
            return url_for(target, page=page, username=post.author.username)
        elif target == 'posts.post':
            return url_for(target, post_id=post.id)

    # Process to register like or unlike
    if request.method=='POST' and form.liked_post_id.data.isnumeric():
        page = int(form.page.data)
        post = Post.query.get(form.liked_post_id.data)
        if current_user.is_authenticated:
            if form.action.data == 'like':
                like = Like(user_id=current_user.id, post_id=post.id)
                db.session.add(like)
            elif form.action.data == 'unlike':
                Like.query.filter_by(user_id=current_user.id, post_id=post.id).delete()
            db.session.commit()
            return redirect(create_url(request.endpoint))
        else:
            flash('You need an account to like a post', 'warning')
        return redirect(create_url(request.endpoint))
    return None


def get_user_likes():
    like_list = []
    if current_user.is_authenticated:
        like_list = [like.post_id for like in current_user.likes]
    return like_list


def save_post_picture(form_picture):
    def get_box(im, target_size):
        width, height = im.size
        target_width, target_height = target_size
        aspect_ratio = width / height
        target_aspect_ratio = target_width / target_height
        if aspect_ratio > target_aspect_ratio:
            new_width = int(height * target_aspect_ratio)
            left = (width - new_width) / 2
            right = (width + new_width) / 2
            box = (left, 0, right, height)
        else:
            new_height = int(width / target_aspect_ratio)
            top = (height - new_height) / 2
            bottom = (height + new_height) / 2
            box = (0, top, width, bottom)
        return box

    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext

    picture_path = os.path.join(current_app.root_path, f'static/post_pics', picture_fn)
    
    output_size = (600, 800)
    i = Image.open(form_picture)
    box = get_box(i, output_size)
    i = i.crop(box)
    i.thumbnail(output_size)
    i.save(picture_path)
    # form_picture.save(picture_path + 'large')
    return picture_fn
