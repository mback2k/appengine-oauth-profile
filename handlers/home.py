from google.appengine.api import app_identity
from google.appengine.api import users
from flask import Blueprint, request, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    userinfo = {}

    user = users.get_current_user()
    if user:
        userinfo['id'] = user.user_id()
        userinfo['email'] = user.email()
        userinfo['nickname'] = user.nickname()

        url = users.create_logout_url(request.path)
        url_linktext = 'Logout'

    else:
        url = users.create_login_url(request.path)
        url_linktext = 'Login'

    template_values = {
        'hostname': app_identity.get_default_version_hostname(),
        'userinfo': userinfo,
        'url': url,
        'url_linktext': url_linktext,
    }

    return render_template('home.html', **template_values)
