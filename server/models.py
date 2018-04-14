import datetime
from flask import current_app
from server import db, bcrypt

class User(db.Document):
    username = db.StringField(unique=True, required = True)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    admin = db.BooleanField(default=False)
    active = db.BooleanField(default=True)
    registered_on = db.DateTimeField(default=datetime.datetime.now())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)
