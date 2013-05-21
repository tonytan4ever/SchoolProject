from models import *

from control import app

from flask import render_template

#===============================================================================
# @app.route('/signup', methods=['POST'])
# def signup():
#    user = User(request.form['username'], request.form['message'])
#    db.session.add(user)
#    db.session.commit()
#    return redirect(url_for('message', username=user.username))
# 
# @app.route('/message/<username>')
# def message(username):
#    user = User.query.filter_by(username=username).first_or_404()
#    return render_template('message.html', username=user.username,
#                                                    message=user.message)
#===============================================================================
    
    
@app.route('/')
#@cached(120)  # from 200 req/s to 800 req/s
def index():
    posts = []
    #posts = Post.query.order_by('created DESC').limit(app.config['post_count'])
    # Ordering by created time DESC isstead of reversing
    return render_template('index.html', posts=posts)


