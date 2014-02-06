import factory

from settings import DefaultConfig


def create_app(settings_override=None, register_security_blueprint=True):
    """Returns the Overholt API application instance"""

    app = factory.create_app(DefaultConfig.PROJECT_NAME, 
                             DefaultConfig.PROJECT_ROOT, 
                             settings_override,
                             register_security_blueprint=register_security_blueprint)
    return app