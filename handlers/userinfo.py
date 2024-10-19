from google.appengine.api import oauth
from flask import Blueprint
import json

bp = Blueprint('userinfo', __name__)

@bp.route('/oauth/v1/userinfo')
def userinfo_v1():
    callback = lambda: oauth.get_current_user()
    return userinfo(callback)

@bp.route('/oauth/v2/userinfo')
def userinfo_v2():
    scope = 'https://www.googleapis.com/auth/userinfo.email'
    callback = lambda: oauth.get_current_user(scope)
    return userinfo(callback)

def userinfo(callback):
    userinfo = {}
    errormsg = None
    code = 200

    try:
        user = callback()
        if user:
            userinfo['id'] = user.user_id()
            userinfo['email'] = user.email()
            userinfo['nickname'] = user.nickname()

    except oauth.InvalidOAuthTokenError:
        errormsg = 'invalid token'

    except oauth.OAuthRequestError:
        errormsg = 'invalid header'

    except oauth.OAuthServiceFailureError:
        errormsg = 'service failure'

    if errormsg:
        error = get_error(errormsg)
        code = error['error']['code']
        data = json.dumps(error)

    else:
        data = json.dumps(userinfo)

    return data, code, {'Content-Type': 'application/json'}

def get_error(message, code=401, location='header'):
    return {
      'error': {
        'errors': [
          {
            'domain': 'com.google.auth',
            'reason': 'invalidAuthentication',
            'message': message,
            'locationType': location,
            'location': 'Authorization'
          }
        ],
        'code': code,
        'message': message
      }
    }
