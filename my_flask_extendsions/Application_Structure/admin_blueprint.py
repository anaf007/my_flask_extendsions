"""http://flask.pocoo.org/snippets/59/

"""

"""__init__.py"""
from flask import Flask
import admin
app = Flask(__name__)
app.register_blueprint(admin.bp, url_prefix='/admin')



"""admin/__init__.py"""
from flask import Blueprint
from flask import redirect, request
from google.appengine.api import users

bp = Blueprint('admin', __name__)

@bp.before_request
def restrict_bp_to_admins():
    if not users.is_current_user_admin():
        return redirect(users.create_login_url(request.url))