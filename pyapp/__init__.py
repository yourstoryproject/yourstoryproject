from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


pyapp = Flask(__name__)
pyapp.config.from_object(Config)

db = SQLAlchemy(pyapp)
migrate = Migrate(pyapp, db)

from pyapp import routes, models  # noqa
