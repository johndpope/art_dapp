from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=1, max=40)
        ]
    )

    email = StringField(
        'Email Address',
        validators=[
            DataRequired(),
            Email(message=None),
            Length(min=6, max=40)
        ]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )

    confirm = PasswordField(
        'Confirm password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )


class ArtistApplication(FlaskForm):

    name = StringField(
        'Name',
        validators=[
            DataRequired(),
            Length(min=1, max=40)
            ]
        )

    email = StringField(
        'Email Address',
        validators=[
            DataRequired(),
            Email(message=None),
            Length(min=6, max=40)
        ]
    )

    bio = TextAreaField(
        'Biography',
        validators=[
            DataRequired(),
        ]
    )

    background_photo = FileField(
        'Background Photo',
        validators=[
            FileRequired()
        ]
    )

    profile_photo = FileField(
        'Profile Photo',
        validators=[
            FileRequired()
        ]
    )
