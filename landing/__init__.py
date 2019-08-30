import os
from flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

from flask_restful import Resource, Api
import os


app = Flask(__name__)
# CsrfProtect(app)
login_manager = LoginManager()

login_manager.init_app(app)

api = Api(app)


db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite4')
db_uri = 'sqlite:///{}'.format(db_path)

app.config.update(dict(
	SECRET_KEY="4b332#@@1!74-006b-4889-8#@#-67b#@#b90ddffd",
    WTF_CSRF_SECRET_KEY='8207bece0139#4980!af20a681e3bf56f3',
    SQLALCHEMY_DATABASE_URI=db_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    # FLASK_ADMIN_SWATCH=cerulean,
	))

admin = Admin(app, name='fvse', template_mode='bootstrap3')


db = SQLAlchemy(app)

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
static = os.path.join(base, 'static')

from .views import *
from .jobs.views import *
from .home.views import *
from .videos.views import *