from config import Config
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

pyapp = Flask(__name__)
pyapp.config.from_object(Config)

csrf = CSRFProtect(pyapp)

login_manager = LoginManager(pyapp)
login_manager.login_view = 'login'

db = SQLAlchemy(pyapp)
migrate = Migrate(pyapp, db)

from pyapp import routes, models  # noqa
