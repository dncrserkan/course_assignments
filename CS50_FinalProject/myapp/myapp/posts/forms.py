from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired, FileSize


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[Length(max=200)])
    picture = FileField('Select Picture', validators=[FileRequired(), 
                                                      FileAllowed(['jpg', 'png', 'jpeg']),
                                                      FileSize(max_size=1e+7, 
                                                               message='File is too large')])
    submit = SubmitField('Post')


class UpdatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content')
    picture = FileField('Select Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg']),
                                                      FileSize(max_size=1e+7,
                                                               message='File is too large')])
    submit = SubmitField('Update')


class LikeForm(FlaskForm):
    liked_post_id = HiddenField(DataRequired())
    action = HiddenField(DataRequired())
    page = HiddenField(DataRequired())
    submit = SubmitField()
