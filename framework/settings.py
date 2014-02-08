# -*- coding: utf-8 -*-

import os

# project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# Instance folder path, make it independent.
INSTANCE_FOLDER_PATH = PROJECT_ROOT

INSTALLED_APPS = (
  'framework.api',
  #'social',  
  'framework.users',
)

def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception, e:
        raise e


class BaseConfig(object):

    PROJECT_NAME = "After School Heaven"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = PROJECT_ROOT

    DEBUG = False
    TESTING = False

    ADMINS = ['youremail@yourdomain.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'your secret key'

    LOG_FOLDER = os.path.join(PROJECT_ROOT, 'logs')
    make_dir(LOG_FOLDER)

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')
    make_dir(UPLOAD_FOLDER)
    
    SOCIAL_TWITTER = dict(
          consumer_key='s9I90X4WxYbZvL7wPF4Fg',
          consumer_secret='Tz9o8aI1VBBklqbOsdKVE2ze1aPphzQ4gES7YeLY6A'
    )

    SOCIAL_FACEBOOK = dict(
        consumer_key='527132627401839',
        consumer_secret='21174e6e7c44880e7eb360ce52888ca6',
        request_token_params=dict(
                scope='email,publish_stream'
        )
    )

    #SOCIAL_GITHUB = dict(
    #    consumer_key='key',
    #    consumer_secret='secret',
    #    #module='app.github'
    #)


class DefaultConfig(BaseConfig):

    DEBUG = True

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = False
    # SQLITE for prototyping.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + INSTANCE_FOLDER_PATH + '/db.sqlite'
    # MYSQL for production.
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db?charset=utf8'

    # Flask-babel: http://pythonhosted.org/Flask-Babel/
    ACCEPT_LANGUAGES = ['zh', 'en']
    BABEL_DEFAULT_LOCALE = 'en'

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    # Flask-mail: http://pythonhosted.org/flask-mail/
    # https://bitbucket.org/danjac/flask-mail/issue/3/problem-with-gmails-smtp-server
    MAIL_DEBUG = DEBUG
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Should put MAIL_USERNAME and MAIL_PASSWORD in production under instance folder.
    MAIL_USERNAME = 'yourmail@gmail.com'
    MAIL_PASSWORD = 'yourpass'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    # Flask-openid: http://pythonhosted.org/Flask-OpenID/
    OPENID_FS_STORE_PATH = os.path.join(INSTANCE_FOLDER_PATH, 'openid')
    make_dir(OPENID_FS_STORE_PATH)
    
    #SECURITY_LOGIN_USER_TEMPLATE = 'security/login.html'
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['email', 'username']
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = '4f1WQbWEKMPv9S7p'
    SECURITY_RECOVERABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = False
    #SECURITY_CHANGE_URL = '/change_password',
    #SECURITY_LOGIN_URL =  '/user/login'
    #SECURITY_LOGOUT_URL =  '/user/logout'
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    
    SECURITY_SEND_REGISTER_EMAIL = False


class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'