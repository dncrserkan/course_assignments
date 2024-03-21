from datetime import datetime, timedelta
from myapp import db, login_manager
from flask import current_app
from flask_login import UserMixin
import jwt
import pytz


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    # table name is lowercase of class name by default
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)    # 20 is max character
    email = db.Column(db.String(120), unique=True, nullable=False)    # 20 is max character
    about = db.Column(db.String(200), nullable=True, default='Hi There !')
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref="author", lazy=True)    # refers to class name
    likes = db.relationship('Like', backref="user", lazy=True)

    def get_reset_token(self, expires_min=3):
        token = jwt.encode({'user_id':self.id,
                            'exp': datetime.now(pytz.timezone('UTC')) + timedelta(minutes=expires_min)
                            },
                            current_app.config['SECRET_KEY'])           
        return token
    
    @staticmethod
    def verify_reset_token(token):
        if token is None:
            return None
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['user_id']
        except:
            return None
        return User.query.get(id)

    def __repr__(self):
        return f"""User
\tusername: {self.username}
\tid: {self.id}
\timage_file: {self.image_file}')
"""


class Post(db.Model):
    def default_time():
        return datetime.now(pytz.timezone('UTC'))

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=default_time)   # do not call function
    date_updated = db.Column(db.DateTime, nullable=False, default=default_time)
    image_file = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)   # refers to tablename.columnname
    likes = db.relationship('Like', backref="itself", lazy=True)

    def __repr__(self):
        return f"""Post
\ttitle: {self.title}
\tfirst post date: {self.date_posted}
\tupdate date: {self.date_updated}
\timage file: {self.image_file}
"""


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"user: {self.user_id} \t liked: {self.post_id}"
