import secrets
import os
from flask import current_app
from PIL import Image


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
