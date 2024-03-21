from flask import render_template, request, Blueprint, flash
from myapp.models import Post, Like
from myapp.posts.forms import LikeForm
from myapp.posts.utils import get_user_likes, process_like_action 


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home(page=1):
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_updated.desc()).paginate(page=page, per_page=3)
    form = LikeForm()

    like_list = get_user_likes()
    temp = process_like_action(form)
    if temp is not None:
        return temp
    
    return render_template('home.html', posts=posts, form=form, like_list=like_list, Like=Like)
