from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import (login_user, current_user, logout_user,
                         fresh_login_required, login_fresh)
from myapp import db, bcrypt
from myapp.models import User, Post, Like
from myapp.users.forms import (RegistrationForm, LoginForm, DeleteUserForm, 
                               UpddateAccountForm, UpdatePasswordForm,
                               RequestPasswordResetForm, ResetPasswordForm)
from myapp.users.utils import save_profile_picture, send_reset_email
from myapp.posts.forms import LikeForm
from myapp.posts.utils import process_like_action, get_user_likes
from datetime import timedelta


users = Blueprint('users', __name__)

    
@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, 
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created. You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated and login_fresh():
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data, duration=timedelta(weeks=1))
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Logged in unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@fresh_login_required
def account():
    print(login_fresh())
    account_form = UpddateAccountForm()
    password_form = UpdatePasswordForm()
    delete_user_form = DeleteUserForm()

    if account_form.validate_on_submit():
        if account_form.picture.data:
            current_user.image_file = save_profile_picture(account_form.picture.data)
        current_user.username = account_form.username.data
        current_user.email = account_form.email.data
        current_user.about = account_form.about.data
        db.session.commit()
        flash('Account updated!', 'success')
        return redirect(url_for('users.account'))
    elif password_form.validate_on_submit() and bcrypt.check_password_hash(current_user.password, password_form.old_password.data):
        hashed_password = bcrypt.generate_password_hash(password_form.new_password.data).decode('utf-8')
        current_user.password = hashed_password
        db.session.commit()
        flash('Password changed!', 'success')
        return redirect(url_for('users.account'))
    elif delete_user_form.validate_on_submit():
        likes_to_delete = Like.query.filter_by(user_id=current_user.id).all()
        posts_to_delete = Post.query.filter_by(author=current_user).all()
        for like in likes_to_delete:
            db.session.delete(like)
        for post in posts_to_delete:
            db.session.delete(post)
        db.session.delete(current_user)
        db.session.commit()
        logout_user()
        flash('Your account is deleted. You can come back anytime you want.', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        account_form.username.data = current_user.username
        account_form.email.data = current_user.email
        account_form.about.data = current_user.about
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', 
                           image_file=image_file, 
                           account_form=account_form,
                           password_form=password_form,
                           delete_user_form=delete_user_form)


@users.route('/user/<string:username>', methods=['GET', 'POST'])
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
                .order_by(Post.date_posted.desc())\
                .paginate(page=page, per_page=3)
    form = LikeForm()
    
    like_list = get_user_likes()
    temp = process_like_action(form)
    if temp is not None:
        return temp

    return render_template('user_posts.html', user=user, form=form,
                           posts=posts, like_list=like_list, Like=Like)


@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestPasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent to reset yourpassword.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', form=form)


@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password is updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', form=form)
