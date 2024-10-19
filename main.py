from google.appengine.api import wrap_wsgi_app
from handlers import app

app = wrap_wsgi_app(app)
