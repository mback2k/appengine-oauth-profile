from google.appengine.ext.webapp import template
import webapp2
import os

class NotFound(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/notfound.html')
        self.response.out.write(template.render(path, {}))

app = webapp2.WSGIApplication([('/.*', NotFound)])
