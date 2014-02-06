# -*- coding: utf-8 -*-
"""
    User Package
    ~~~~~~~~~~~~~~~~~~

    launchpad frontend application package
"""

from functools import wraps

from flask import render_template
from flask_security import login_required

from .views import bp


def create_app(settings_override=None, register_security_blueprint=False):
    """Returns the Overholt API application instance"""

    app = factory.create_app(__name__, __path__, settings_override,
                             register_security_blueprint=register_security_blueprint)

    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    # Register custom error handlers
    #app.errorhandler(OverholtError)(on_overholt_error)
    #app.errorhandler(OverholtFormError)(on_overholt_form_error)
    #app.errorhandler(404)(on_404)

    return app


