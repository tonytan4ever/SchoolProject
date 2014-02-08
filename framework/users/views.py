from flask import Blueprint, render_template,request

from flask.ext.security import LoginForm, current_user, login_required, \
    login_user
    
from forms import RegisterForm

from ..decorators import route
from .models import User

bp = Blueprint('user', __name__)


@route(bp, '/')
def index():
    return render_template('index.html', 
                           active_nav_band = "Home",
                           total_users=User.query.count())


@bp.route('/login')
def login():
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    return render_template('security/login.html', 
                                active_nav_band = "Login",
                                form=LoginForm())


@bp.route('/register', methods=['GET', 'POST'])
@bp.route('/register/<provider_id>', methods=['GET', 'POST'])
def register(provider_id=None):
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    form = RegisterForm()

    if provider_id:
        provider = get_provider_or_404(provider_id)
        connection_values = session.get('failed_login_connection', None)
    else:
        provider = None
        connection_values = None

    if form.validate_on_submit():
        ds = current_app.security.datastore
        user = ds.create_user(email=form.email.data, password=form.password.data)
        ds.commit()

        # See if there was an attempted social login prior to registering
        # and if so use the provider connect_handler to save a connection
        connection_values = session.pop('failed_login_connection', None)

        if connection_values:
            connection_values['user_id'] = user.id
            connect_handler(connection_values, provider)

        if login_user(user):
            ds.commit()
            flash('Account created successfully', 'info')
            return redirect(url_for('profile'))

        return render_template('thanks.html', user=user)

    login_failed = int(request.args.get('login_failed', 0))

    return render_template('security/register.html',
                           active_nav_band = "Register",
                           form=form,
                           provider=provider,
                           login_failed=login_failed,
                           connection_values=connection_values)


@route(bp, '/profile')
def profile():
    return render_template('profile.html',
        twitter_conn=current_app.social.twitter.get_connection(),
        facebook_conn=current_app.social.facebook.get_connection(),
        github_conn=current_app.social.github.get_connection())


@route(bp, '/profile/<provider_id>/post', methods=['POST'])
def social_post(provider_id):
    message = request.form.get('message', None)

    if message:
        provider = get_provider_or_404(provider_id)
        api = provider.get_api()

        if provider_id == 'twitter':
            display_name = 'Twitter'
            api.PostUpdate(message)
        if provider_id == 'facebook':
            display_name = 'Facebook'
            api.put_object("me", "feed", message=message)

        flash('Message posted to %s: %s' % (display_name, message), 'info')

    return redirect(url_for('profile'))


@route(bp, '/admin')
def admin():
    users = User.query.all()
    return render_template('admin.html', users=users)


@route(bp, '/admin/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully', 'info')
    return redirect(url_for('admin'))