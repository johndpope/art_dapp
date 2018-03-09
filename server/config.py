# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(
    #     os.path.join(basedir, 'dev.db'))
    # SQLALCHEMY_BINDS = {
    #     'users': 'sqlite:///{0}'.format(
    #         os.path.join(basedir, 'users.db'))
    # }
    MONGODB_SETTINGS = {'host': 'mongodb://localhost:27017/test', 'db': 'TestMongo'}
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    DEBUG_TB_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_DATABASE_URI = 'postgres://bqtbtxykpgitmf:0c62c97c68881740454e00de6df6c21ef5fe59c92535f46ba310a0fe1ce7a303@ec2-54-197-233-123.compute-1.amazonaws.com:5432/d3bk6mfhnishr5'
    DEBUG_TB_ENABLED = False
