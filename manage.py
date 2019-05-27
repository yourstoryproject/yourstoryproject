import os
import datetime
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from pyapp import pyapp, db
from pyapp.models.Account import Account

pyapp.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(pyapp, db)
manager = Manager(pyapp)

manager.add_command('db', MigrateCommand)

@manager.command
def create_admin():
    """Create an admin user"""
    db.session.add(Account(
        email="ad@min.com",
        password="admin",
        admin=True,
        confirmed=True,
        confirmed_on=datetime.datetime.now())
    )
    db.session.commit()

if __name__ == '__main__':
    manager.run()
