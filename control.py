from functools import wraps
from flask import Flask, redirect, url_for, session, flash, render_template, request, abort
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.markdown import Markdown
from werkzeug.contrib.cache import SimpleCache

import re
from datetime import datetime
from functools import wraps
from settings import DevConfig
#from cgi import escape

cache = SimpleCache()

app = Flask(__name__)

app.debug = DevConfig.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = DevConfig.SQLALCHEMY_DATABASE_URI

app.config['SECRET_KEY'] = DevConfig.SECRET_KEY

db = SQLAlchemy(app)

from views import *


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logged = session.get('logged_in', None)
        if not logged:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function



if __name__ == '__main__':
    import sys
    host,port = sys.argv[1], sys.argv[2]
    app.run(host=host, port=int(port))


