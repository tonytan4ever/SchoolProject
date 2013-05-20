from models import *

# ...

@app.route('/signup', methods=['POST'])
def signup():
    user = User(request.form['username'], request.form['message'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('message', username=user.username))

@app.route('/message/<username>')
def message(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('message.html', username=user.username,
                                                    message=user.message)