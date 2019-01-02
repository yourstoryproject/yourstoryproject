from app import db


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'), primary_key=True)
)

class Account(db.Model):
    __tablename__   = 'account'

    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    created_on      = db.Column(db.Date, unique=False, nullable=False)
    email           = db.Column(db.String(120), index=True, unique=True)
    last_login      = db.Column(db.Date, unique=False, nullable=True)
    password_hash   = db.Column(db.String(128))
    username        = db.Column(db.String(48), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<Account {}>'.format(self.username)

class Entry(db.Model):
    __tablename__   = 'entry'

    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    account_id      = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    content         = db.Column(db.Text, unique=False, nullable=False)
    created_on      = db.Column(db.Date, unique=False, nullable=False)
    modified_on     = db.Column(db.Date, unique=False, nullable=True)
    tags            = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('entry', lazy=True))
    title           = db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return '<Entry {}>'.format(self.title)

class Tag(db.Model):
    __tablename__   = 'tag'

    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    created_on      = db.Column(db.Date, unique=False, nullable=False)
    modified_on     = db.Column(db.Date, unique=False, nullable=False)
    name            = db.Column(db.String(48), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag {}>'.format(self.name)