from google.appengine.ext.webapp import template
import webapp2
import os

class Robots(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        path = os.path.join(os.path.dirname(__file__), '../templates/robots.txt')
        self.response.out.write(template.render(path, {}))

app = webapp2.WSGIApplication([('/robots.txt', Robots)])
