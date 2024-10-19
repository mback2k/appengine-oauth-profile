from flask import Blueprint, render_template

bp = Blueprint('notfound', __name__)

@bp.errorhandler(404)
@bp.route("/<path:path>")
def notfound(path):
    return render_template('notfound.html'), 404
