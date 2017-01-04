from flask_validator import ValidateEmail, ValidateString
from api.app import db, ma


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=None)
    user = db.relationship('User', backref=db.backref('books'))

    def __init__(self, title, author, user=None):
        self.title = title
        self.author = author
        self.user = user

    def __repr__(self):
        return '<Book %r>' % self.title

    @classmethod
    def __declare_last__(cls):
        ValidateString(Book.title)
        ValidateString(Book.author)


class BookSchema(ma.Schema):

    class Meta:
        fields = ('id', 'title', 'author', 'user')

    from api.app.models.User import UserSchema
    user = ma.Nested(UserSchema)
    # edited_user = ma.Nested(UserSchema)

    # from api.app.models.User import UserSchema
    # created_user_id = ma.Nested(UserSchema)
