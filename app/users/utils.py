import os
import secrets
from PIL import Image
from flask import url_for, current_app
from app import mail
from flask_mail import Message
from azure.storage.blob import BlockBlobService


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    blob_service = BlockBlobService('herokustorage', '/1LCdFzgOqwTu8i752Ww4PnVdEsjZbV1hqgEMHF/QgRl7rSFRETUipUNMz0CTPp2V6wW/GIMMv6gFjZkhCQQOg==')
    blob_service.create_blob_from_path('images', picture_fn, picture_path)

    url = blob_service.make_blob_url('images', picture_fn)
    print(url)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='niklasbae@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made
'''
    mail.send(msg)
