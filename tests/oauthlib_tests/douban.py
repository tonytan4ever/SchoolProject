from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth


app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

douban = oauth.remote_app(
    'douban',
    consumer_key='<consumer_key>',
    consumer_secret='<consumer_secret>',
    base_url='https://api.douban.com/v2/',
    request_token_url=None,
    request_token_params={'scope': 'douban_basic_common'},
    access_token_url='https://www.douban.com/service/auth2/token',
    authorize_url='https://www.douban.com/service/auth2/auth',
    access_token_method='POST',
)


@app.route('/')
def index():
    if 'douban_token' in session:
        resp = douban.get('user/~me')
        return jsonify(resp.data)
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return douban.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
def logout():
    session.pop('douban_token', None)
    return redirect(url_for('index'))


@app.route('/login/authorized')
@douban.authorized_handler
def authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['douban_token'] = (resp['access_token'], '')
    return redirect(url_for('index'))


@douban.tokengetter
def get_douban_oauth_token():
    return session.get('douban_token')


if __name__ == '__main__':
    app.run(host="10.0.2.15",
                    port=5000)
