from pyapp import db
from pyapp.models import tags
import datetime


class Entry(db.Model):
    __tablename__ = 'entry'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    account_id = db.Column(
        db.Integer,
        db.ForeignKey('account.id'),
        nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    created_on = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        unique=False,
        nullable=False)
    modified_on = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        unique=False,
        nullable=True)
    tags = db.relationship(
        'Tag',
        secondary=tags,
        lazy='subquery',
        backref=db.backref(
            'entry',
            lazy=True))
    title = db.Column(db.String(128), unique=False, nullable=False)

    def __init__(self, account_id, content, tags, title):
        """
        Class constructor
        """
        self.account_id = account_id
        self.content = content
        self.created_on = datetime.datetime.utcnow()
        self.modified_on = datetime.datetime.utcnow()
        self.title = title

    def to_json(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'content': self.content,
            'created_on': self.created_on,
            'modified_on': self.modified_on,
            'tags': [tag.name for tag in self.tags],
            'title': self.title
        }

    def __repr__(self):
        return '<Entry {}>'.format(self.title)
