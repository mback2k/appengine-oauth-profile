from google.appengine.api import oauth
import webapp2
import json

class UserInfo(webapp2.RequestHandler):
    def get(self):
        userinfo = {}
        errormsg = None

        try:
            user = oauth.get_current_user()
            if user:
                userinfo['id'] = user.user_id()
                userinfo['email'] = user.email()
                userinfo['nickname'] = user.nickname()

        except oauth.InvalidOAuthTokenError, e:
            errormsg = 'invalid token'

        except oauth.OAuthRequestError, e:
            errormsg = 'invalid header'

        except oauth.OAuthServiceFailureError, e:
            errormsg = 'service failure'

        if errormsg:
            error = get_error(errormsg)
            self.error(error['error']['code'])

            data = json.dumps(error)

        else:
            data = json.dumps(userinfo)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

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

app = webapp2.WSGIApplication([('/oauth/v1/userinfo', UserInfo)])
