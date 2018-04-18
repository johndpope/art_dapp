from flask import current_app
from flask_script import Manager

from server import create_app, db, models, bcrypt

app = create_app()
manager = Manager(app)


@manager.command
def migrate_contract(network):
    """
    Should call truffle migrate --network network
    """
    print(network)

@manager.command
def config(config):
    if config == 'production':
        app_settings = os.getenv(
            'APP_SETTINGS', 'server.config.ProductionConfig')
    elif config == 'test':
        app_settings = os.getenv(
            'APP_SETTINGS', 'server.config.TestingConfig')
    elif config == 'develop':
        app_settings = os.getenv(
            'APP_SETTINGS', 'server.config.DevelopmentConfig')
    else:
        print(str(config)+ ' is an invalid configuration')
        return

    app.config.from_object(app_settings)


@manager.command
def create_admin():
    """Creates the admin user."""
    admin = models.User(username= 'gallery_admin', email='galleryblockchain@gmail.com', password =bcrypt.generate_password_hash('toledano',
        current_app.config.get('BCRYPT_LOG_ROUNDS')).decode('utf-8'), admin=True)
    admin.save()


if __name__ == '__main__':
    manager.run()
