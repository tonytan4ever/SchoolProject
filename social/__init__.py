# -*- coding: utf-8 -*-
"""
    flask.ext.social
    ~~~~~~~~~~~~~~~~

    Flask-Social is a Flask extension that aims to add simple OAuth provider
    integration for Flask-Security

    :copyright: (c) 2012 by Matt Wright.
    :license: MIT, see LICENSE for more details.
"""

__version__ = '1.6.2'

from .core import Social
from .datastore import SQLAlchemyConnectionDatastore, \
     MongoEngineConnectionDatastore, PeeweeConnectionDatastore
from .signals import connection_created, connection_failed, login_failed, \
     connection_removed, login_completed
from views import create_blueprint

class fake_state:
    def __init__(self, blueprint_name):
        self.blueprint_name = blueprint_name
        self.url_prefix =""
        
bp = create_blueprint(fake_state('social'), __name__)