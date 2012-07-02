from google.appengine.ext.webapp import template
from google.appengine.api import users
import webapp2
import json
import os

class Home(webapp2.RequestHandler):
    def get(self):
        userinfo = {}

        user = users.get_current_user()
        if user:
            userinfo['id'] = user.user_id()
            userinfo['email'] = user.email()
            userinfo['nickname'] = user.nickname()

            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'

        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'userinfo': userinfo,
            'url': url,
            'url_linktext': url_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/home.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', Home)])
