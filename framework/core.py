# -*- coding: utf-8 -*-
"""
    framework.core
    ~~~~~~~~~~~~~

    core module
"""

from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader

from social import Social

#: Flask-SQLAlchemy extension instance
db = SQLAlchemy()

#: Flask-Mail extension instance
mail = Mail()

#: Flask-Security extension instance
security = Security()

#: My Flask-Social extension instance
social = Social()


import assets
assets_env = Environment()
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)