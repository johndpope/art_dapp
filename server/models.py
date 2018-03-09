# project/server/models.py


import datetime
from flask import current_app
from server import db, bcrypt


# class PreReleaseFormObj(db.Model):
#     __tablename__ = "pre_release_form"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(255))
#     email = db.Column(db.String(255))
#     type = db.Column(db.String(255))
#     signedup_on = db.Column(db.DateTime)
#
#
#     def __init__(self, email, name, type):
#         self.email = email
#         self.name = name
#         self.type = type
#         self.signedup_on = datetime.datetime.now()
#
# #     def __repr__(self):
#         return '<User {0}>'.format(self.email)

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
