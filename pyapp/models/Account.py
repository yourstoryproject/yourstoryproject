from pyapp import db
from pyapp import login_manager
from werkzeug import check_password_hash, generate_password_hash
import datetime


class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    created_on = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        unique=False,
        nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    last_login = db.Column(
        db.Date,
        default=datetime.datetime.utcnow,
        unique=False,
        nullable=True)
    password_hash = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), default='user')

    def __init__(self, email, password):
        """
        Class constructor
        """
        self.authenticated = False
        self.created_on = datetime.datetime.utcnow()
        self.email = email.lower()
        self.last_login = datetime.datetime.utcnow()
        self.set_password(password)
        self.role = 'user'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, salt_length=8)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def has_role(self, role):
        if self.role == role:
            return True

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def to_json(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'email': self.email,
            'last_login': self.last_login,
            'role': self.role
        }

    def __repr__(self):
        return '<Account {}>'.format(self.id)
