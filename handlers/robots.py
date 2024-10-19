from flask import Blueprint, render_template

bp = Blueprint('robots', __name__)

@bp.route('/robots.txt')
def robots():
    return render_template('robots.txt'), {'Content-Type': 'text/plain'}
