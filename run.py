from app import app
from app import db
from app.models import Account, Entry, Tag

db.init_app(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Account': Account, 'Entry': Entry, 'Tag': Tag}
