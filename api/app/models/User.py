import uuid
from flask_validator import ValidateEmail, ValidateString, ValidateBoolean
from werkzeug.security import generate_password_hash, check_password_hash
from api.app import db, ma


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    token = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, email, active=False):
        self.username = username
        self.__set_password(password)
        self.email = email
        self.__set_token()
        self.active = active

    def __repr__(self):
        return '<User %r>' % self.username

    def check_password(self, password):
        # TODO: Add some better hashing system
        return check_password_hash(self.password, password)

    def __set_token(self):
        # TODO: Make this better, check for uniqueness
        self.token = uuid.uuid4().hex

    def __set_password(self, password):
        # TODO: Add some better hashing system
        self.password = generate_password_hash(password)

    @classmethod
    def __declare_last__(cls):
        ValidateString(User.username)
        ValidateString(User.password)
        # TODO: fix ValidateEmail, or write custom email validation
        # ValidateEmail(User.email) # not working properly for some use cases
        # of email!!!
        ValidateString(User.token)
        ValidateBoolean(User.active)


class UserSchema(ma.Schema):

    class Meta:
        fields = ('id', 'email', 'username')
