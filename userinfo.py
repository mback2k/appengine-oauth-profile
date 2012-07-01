from google.appengine.api import oauth
import webapp2
import json

class UserInfo(webapp2.RequestHandler):
    def get(self):
        userinfo = {}

        try:
            user = oauth.get_current_user()
            userinfo['id'] = user.user_id()
            userinfo['email'] = user.email()
            userinfo['nickname'] = user.nickname()

        except oauth.OAuthRequestError, e:
            return self.error(401)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(userinfo))

app = webapp2.WSGIApplication([('/oauth/v1/userinfo', UserInfo)])
