import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from pyapp import pyapp, db


pyapp.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(pyapp, db)
manager = Manager(pyapp)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
