

import unittest


from flask import current_app
from flask_script import Manager

from server import create_app, db, models, bcrypt



app = create_app()
manager = Manager(app)


@manager.command
def create_admin():
    """Creates the admin user."""
    admin = models.User(username= 'gallery_admin', email='galleryblockchain@gmail.com', password =bcrypt.generate_password_hash('toledano',
        current_app.config.get('BCRYPT_LOG_ROUNDS')).decode('utf-8'), admin=True)
    admin.save()


if __name__ == '__main__':
    manager.run()
