from config import Config
from flask import Flask, send_from_directory
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

pyapp = Flask(__name__)
pyapp.config.from_object(Config)

login_manager = LoginManager(pyapp)
login_manager.login_view = 'login'

db = SQLAlchemy(pyapp)
migrate = Migrate(pyapp, db)

from pyapp import routes, models  # noqa
