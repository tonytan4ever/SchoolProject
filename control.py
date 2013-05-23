from functools import wraps
from flask import Flask, redirect, url_for, session, flash, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
#from flask.ext.markdown import Markdown
from werkzeug.contrib.cache import SimpleCache

import re
from datetime import datetime
from functools import wraps
from settings import DevConfig
import assets
#from cgi import escape

cache = SimpleCache()

app = Flask(__name__)

app.debug = DevConfig.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = DevConfig.SQLALCHEMY_DATABASE_URI

app.config['SECRET_KEY'] = DevConfig.SECRET_KEY

# database
db = SQLAlchemy(app)

# assets
assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

# views
from views import *


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logged = session.get('logged_in', None)
        if not logged:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


