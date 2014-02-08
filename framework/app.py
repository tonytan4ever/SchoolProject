from flask import redirect, url_for, render_template

import factory
from models import User
from settings import DefaultConfig


def create_app(settings_override=None, register_security_blueprint=True):
    """Returns the Overholt API application instance"""

    app = factory.create_app(DefaultConfig.PROJECT_NAME, 
                             DefaultConfig.PROJECT_ROOT, 
                             settings_override,
                             register_security_blueprint=register_security_blueprint)
    
    @app.route("/")
    def index():
        return render_template('index.html', 
                           active_nav_band = "Home",
                           total_users=User.query.count())
            
    return app