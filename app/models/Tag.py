from app import db
import datetime


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
