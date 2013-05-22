from models import *
from control import app
from flask import render_template

    
@app.route('/')
#@cached(120)  # from 200 req/s to 800 req/s
def index():
    posts = []
    #posts = Post.query.order_by('created DESC').limit(app.config['post_count'])
    # Ordering by created time DESC isstead of reversing
    return render_template('index.html', posts=posts)


