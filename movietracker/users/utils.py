import secrets
import os
from flask import current_app, flash
from PIL import Image
from movietracker.models import User
from flask_login import current_user


def save_picture(form_picture):
    # generate random hex for filename
    random_hex = secrets.token_hex(8)

    # get extension of picture file
    _, f_ext = os.path.splitext(form_picture.filename)

    # merge hex and extension
    picture_filename = random_hex + f_ext

    # create path for pics
    picture_path = os.path.join(current_app.root_path, 'static/photos', picture_filename)

    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_filename


def validate_username(username):
    # check if user changes his own username
    try:
        if username.data == current_user.username:
            return True
    except AttributeError:
        pass

    # check if other users have same username
    user = User.query.filter_by(username=username.data).first()
    if user:
        flash('This username is already taken. '
              'Please choose a different one', 'error')
        return False
    return True


def validate_email(email):
    # check if user changes his own email
    try:
        if email.data == current_user.email:
            return True
    except AttributeError:
        pass

    # check if other users have same email
    user = User.query.filter_by(email=email.data).first()
    if user:
        flash('This email is already taken. '
              'Please choose a different one', 'error')
        return False
    return True
