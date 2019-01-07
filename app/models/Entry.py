from app import db
from app.models import tags
import datetime


class Entry(db.Model):
    __tablename__   = 'entry'

    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    account_id      = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    content         = db.Column(db.Text, unique=False, nullable=False)
    created_on      = db.Column(db.DateTime, default=datetime.datetime.utcnow, unique=False, nullable=False)
    modified_on     = db.Column(db.DateTime, unique=False, nullable=True)
    tags            = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('entry', lazy=True))
    title           = db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return '<Entry {}>'.format(self.title)

    def __init__(self, account_id, content, modified_on, tags, title):
        self.account_id = account_id
        self.content = content
        self.created_on = datetime.datetime.utcnow()
        self.modified_on = modified_on
        self.tags = tags
        self.title = title