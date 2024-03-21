import os
import secrets
from PIL import Image
from myapp import mail
from flask import current_app
from flask import url_for
from flask_mail import Message



def save_profile_picture(form_picture):
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

    picture_path = os.path.join(current_app.root_path, f'static/profile_pics', picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    box = get_box(i, output_size)
    i = i.crop(box)
    i.thumbnail(output_size)
    i.save(picture_path)
    # form_picture.save(picture_path + 'large')
    return picture_fn




def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@finalpy.com',
                  recipients=[user.email])
    msg.body = f'''To reset yout password, visit the following link;
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email.
'''
    mail.send(msg)