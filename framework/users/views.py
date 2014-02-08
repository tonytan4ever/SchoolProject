from flask import Blueprint, current_app, render_template,request, flash,\
           session, redirect, url_for

from flask.ext.security import LoginForm, current_user, login_required, \
    login_user, logout_user

from social.utils import config_value, get_provider_or_404
from social.views import connect_handler
from forms import RegisterForm

from ..core import security

from ..decorators import route
from .models import User

bp = Blueprint('user', __name__, url_prefix="/user")


@bp.route('/')
def index():
    return redirect('/')


@bp.route('/login')
def login():
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    return render_template('security/login.html', 
                                active_nav_band = "Login",
                                form=LoginForm())
    
@route(bp, '/logout')
def logout():
    """View function which handles a logout request."""

    if current_user.is_authenticated():
        logout_user()

    return redirect(request.args.get('next', None) or
                                url_for('user.index'))


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
        ds = current_app.extensions['security'].datastore
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
            return redirect(url_for('user.profile'))

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
        twitter_conn=current_app.extensions['social'].twitter.get_connection(),
        facebook_conn=current_app.extensions['social'].facebook.get_connection(),
        #github_conn=current_app.extensions['social'].github.get_connection()
        )



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

    return redirect(url_for('userprofile'))


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