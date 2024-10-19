from flask import Flask
from . import home, robots, userinfo, notfound

app = Flask(__name__)
app.template_folder = '../templates'
app.register_blueprint(home.bp)
app.register_blueprint(robots.bp)
app.register_blueprint(userinfo.bp)
app.register_blueprint(notfound.bp)
