from app import db
from werkzeug import check_password_hash, generate_password_hash
import datetime


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'), primary_key=True)
)

class Account(db.Model):
    __tablename__   = 'account'

    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    created_on      = db.Column(db.DateTime, default=datetime.datetime.utcnow, unique=False, nullable=False)
    email           = db.Column(db.String(120), index=True, unique=True, nullable=False)
    last_login      = db.Column(db.Date, unique=False, nullable=True)
    password_hash   = db.Column(db.String(128))
    username        = db.Column(db.String(48), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<Account {}>'.format(self.username)

    def __init__(self, email, last_login, password, username):
        self.created_on = datetime.datetime.utcnow()
        self.email  = email.lower()
        self.last_login  = last_login
        self.set_password(password)
        self.username = username

    def set_password(self, password):
        self.password_hash   = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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

class Tag(db.Model):
    __tablename__   = 'tag'

    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    created_on      = db.Column(db.DateTime, default=datetime.datetime.utcnow, unique=False, nullable=False)
    modified_on     = db.Column(db.Date, unique=False, nullable=True)
    name            = db.Column(db.String(48), unique=True, nullable=False)

    def __init__(self, modified_on, name):
        """
        Class constructor
        """
        self.created_on = datetime.datetime.utcnow()
        self.modified_on = modified_on
        self.name = name.lower()

    @staticmethod
    def get_tags():
        return Tag.query.all()

    @staticmethod
    def get_tag(id):
        return Tag.query.get(id)

    def to_json(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'modified_on': self.modified_on,
            'name': self.name
        }

    def __repr__(self):
        return '<Tag {}>'.format(self.name)
