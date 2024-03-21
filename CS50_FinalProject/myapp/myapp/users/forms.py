from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from myapp.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()     # return None if not exist
        if user:
            raise ValidationError('Username is taken. Please choose different username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()     # return None if not exist
        if user:
            raise ValidationError('Email is taken. Please choose different email.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpddateAccountForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    about = TextAreaField('About', 
                          validators=[Length(max=200)])
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpg', 'png', 'jpeg']),
                                    FileSize(max_size=1e+7, message='File is too large')])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:                          # submit with same name
            user = User.query.filter_by(username=username.data).first()     # return None if not exist
            if user:
                raise ValidationError('Username is taken. Choose different username.')

    def validate_email(self, email):
        if email.data != current_user.email:                          # submit with same mail
            user = User.query.filter_by(email=email.data).first()     # return None if not exist
            if user:
                raise ValidationError('Email is taken. Choose different username.')


class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField('Current Password', validators=[DataRequired()]) # checking equal to current password in routes
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change')


class RequestPasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError('There is no account with this email.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


class DeleteUserForm(FlaskForm):
    submit = SubmitField('Delete')
