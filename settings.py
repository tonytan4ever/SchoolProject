import os

# initial settings

#env = os.environ.get('EXAMPLE_ENV', 'prod')
#app.config.from_object('example.settings.%sConfig' % env.capitalize())
#app.config['ENV'] = env

class Config(object):
    SECRET_KEY = 'C5G94WB6BVRPHTO85RGI2Y6TM6HYY0P'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://example.db'
    SQLALCHEMY_ECHO = True