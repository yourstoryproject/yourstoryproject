from app import db
import datetime


class Tag(db.Model):
    __tablename__   = 'tag'

    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    created_on      = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False, unique=False)
    modified_on     = db.Column(db.Date, default=datetime.datetime.utcnow, nullable=True, unique=False)
    name            = db.Column(db.String(48), unique=True, nullable=False)

    def __init__(self, name):
        """
        Class constructor
        """
        self.created_on = datetime.datetime.utcnow()
        self.modified_on = datetime.datetime.utcnow()
        self.name = name.lower()

    @staticmethod
    def get_tags():
        return Tag.query.all()

    @staticmethod
    def get_tag(id):
        return Tag.query.get(id)

    @staticmethod
    def create_tag(name):
        if not Tag.query.filter_by(name=name).first():
            newTag = Tag(name=name)

            db.session.add(newTag)
            db.session.commit()

            return 'Success!'
        else:
            return 'Tag already exists'

    def to_json(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'modified_on': self.modified_on,
            'name': self.name
        }

    def __repr__(self):
        return '<Tag {}>'.format(self.name)
