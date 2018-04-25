import datetime
from flask import current_app
from server import db, bcrypt

class Collector(db.Document):

    username = db.StringField(unique=True, required = True)
    email = db.EmailField(unique=True, required=True)
    address = db.StringField(unique=True, required = True)
    password = db.StringField()
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
        return '<Collector {0}>'.format(self.username)


class Artist(db.Document):

    name = db.StringField(unique=True, required = True)
    email = db.EmailField(unique=True, required=True)
    bio = db.StringField(required = True)
    background_photo_path = db.StringField(unique=True)
    profile_photo_path = db.StringField(unique=True)
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
        return '<Artist {0}>'.format(self.name)
