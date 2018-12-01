from app import db


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(
                value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

class Account(db.Model):
    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    created_on      = db.Column(db.Date, unique=False, nullable=False)
    last_login      = db.Column(db.Date, unique=False, nullable=True)
    user_name       = db.Column(db.String(48), unique=True, nullable=False)

class Entry(db.Model):
    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    account_id      = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    content         = db.Column(db.Text, unique=False, nullable=False)
    created_on      = db.Column(db.Date, unique=False, nullable=False)
    last_modified   = db.Column(db.Date, unique=False, nullable=True)
    tags            = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('entry', lazy=True))
    title           = db.Column(db.String(128), unique=False, nullable=False)

class Tag(db.Model):
    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    created_on      = db.Column(db.Date, unique=False, nullable=False)
    modified_on     = db.Column(db.Date, unique=False, nullable=False)
    name            = db.Column(db.String(24), unique=True, nullable=False)

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'), primary_key=True)
)