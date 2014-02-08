# -*- coding: utf-8 -*-
"""
    framework.factory
    ~~~~~~~~~~~~~~~~

    framework factory module
"""

import os

from celery import Celery
from flask import Flask
from flask_security import SQLAlchemyUserDatastore

from .core import db, mail, security, social, assets_env
from .helpers import register_blueprints
from .middleware import HTTPMethodOverrideMiddleware
from .models import User, Role

from settings import DefaultConfig, INSTALLED_APPS
 


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the Overholt platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object(DefaultConfig)
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    db.init_app(app)
    mail.init_app(app)
    security.init_app(app, SQLAlchemyUserDatastore(db, User, Role),
                      register_blueprint=register_security_blueprint)
    social.init_app(app)
    assets_env.init_app(app)

    register_blueprints(app, INSTALLED_APPS)
    
    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
    
    
    return app


def create_celery_app(app=None):
    app = app or create_app('After School Heavn', os.path.dirname(__file__))
    celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery