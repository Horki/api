from flask import Blueprint, request
from flask_jwt import jwt_required, current_identity
from flask_api import status

from api.app.exceptions.NotFoundException import NotFoundException

mod_book = Blueprint('book', __name__, url_prefix='/book')


@mod_book.route('/', methods=['GET'])
@jwt_required()
def get_books():
    from api.app.models.Book import Book, BookSchema
    books = Book.query.all()
    book_schema = BookSchema(many=True)
    return {"data": book_schema.dump(books).data}, status.HTTP_200_OK


@mod_book.route('/me', methods=['GET'])
@jwt_required()
def get_user_books():
    from api.app.models.Book import Book, BookSchema
    books = Book.query.filter_by(user_id=current_identity.id).all()
    book_schema = BookSchema(many=True)
    return {"data": book_schema.dump(books).data}, status.HTTP_200_OK


@mod_book.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_book(id):
    from api.app.models.Book import Book, BookSchema
    book = Book.query.get(id)

    if book is None:
        raise NotFoundException('Non existing book')
    book_schema = BookSchema()
    return {"data": book_schema.dump(book).data}, status.HTTP_200_OK


@mod_book.route('/<int:id>', methods=['PUT'])
@jwt_required()
def edit_book(id):
    # User can edit only his books
    # TODO: this is a bit dirty, but will figure out a better way
    from api.app import db
    from api.app.models.Book import Book, BookSchema

    data = request.data
    book = Book.query.filter_by(id=id, user_id=current_identity.id).first()
    if book is None:
        raise NotFoundException('Non existing book, or invalid book')

    if "title" in data:
        book.title = data['title']

    if "author" in data:
        book.author = data['author']

    db.session.commit()

    book_schema = BookSchema()

    return {"data": book_schema.dump(book).data}, status.HTTP_200_OK


@mod_book.route('/', methods=['POST'])
@jwt_required()
def add_book():
    from api.app import db
    from api.app.models.Book import Book, BookSchema

    data = request.data

    book = Book(
        title=data['title'],
        author=data['author'],
        user=current_identity
    )

    db.session.add(book)

    db.session.commit()

    book_schema = BookSchema()

    return {"data": book_schema.dump(book).data}, status.HTTP_201_CREATED


@mod_book.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    from api.app import db
    from api.app.models.Book import Book

    book = Book.query.filter_by(id=id, user_id=current_identity.id).first()
    if book is None:
        raise NotFoundException('Non existing book, or invalid book')

    db.session.delete(book)

    db.session.commit()

    return {"message": "Book id: %d deleted" % id}, status.HTTP_200_OK
