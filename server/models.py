import datetime
from flask import current_app
from server import db, bcrypt

class User(db.Document):

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
        return '<User {0}>'.format(self.username)


class Artist(db.Document):

    name = db.StringField(unique=True, required = True)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    bio = db.StringField()
    link_to_work = db.StringField()
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

class Auction(db.Document):

    initial_price = db.FloatField()
    max_time = db.FloatField()
    id_for_painting = db.StringField()
    bidders = db.ListField()



class ArtInformation(db.Document):

    name = db.StringField(required=True)
    description = db.StringField()
    file_name=db.StringField()
    file_URI = db.StringField()
    watermarked_URI = db.StringField()
    for_sale = db.BooleanField(default=False)
    file_type = db.StringField()
    date_created = db.DateTimeField(default=datetime.datetime.now())
