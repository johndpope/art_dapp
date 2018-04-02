

import unittest
import coverage

from flask import current_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import create_app, db, models, bcrypt



app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1



# @manager.command
# def create_db():
#     """Creates the db tables."""
#     db.create_all()
#     db.create_all(bind=['users'])
#
#
# @manager.command
# def drop_db():
#     """Drops the db tables."""
#     db.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    admin = models.User(username= 'gallery_admin', email='galleryblockchain@gmail.com', password =bcrypt.generate_password_hash('toledano',
        current_app.config.get('BCRYPT_LOG_ROUNDS')).decode('utf-8'), admin=True)
    admin.save()


if __name__ == '__main__':
    manager.run()
