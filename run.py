from pyapp import pyapp
from pyapp import db
from pyapp.models import Account, Entry, Tag

db.init_app(pyapp)


@pyapp.shell_context_processor
def make_shell_context():
    return {'db': db, 'Account': Account, 'Entry': Entry, 'Tag': Tag}
