from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class Upload(FlaskForm):

    name = StringField(
        'Name',
        validators=[
            DataRequired()
            ]
        )

    description = TextAreaField(
        'Description',
        validators=[
            DataRequired(),
        ]
    )

    crypto_painting = FileField(
        'Crypto Painting',
        validators=[
            FileRequired()
        ]
    )
