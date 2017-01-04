from flask import request
from flask_api import status
from flask_rq2 import RQ
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt import JWT
from sqlalchemy.exc import DatabaseError

import api.helpers as helper
from api.config import create_app
from api.app.exceptions.JsonSchemaException import JsonSchemaException
from api.app.exceptions.NotFoundException import NotFoundException
from api.app.exceptions.BadRequestException import BadRequestException

# Init Flask SQLAlchemy http://flask-sqlalchemy.pocoo.org/2.1/
db = SQLAlchemy()

# Init Marshmallow http://flask-marshmallow.readthedocs.io/en/latest/
ma = Marshmallow()

# Init Flask RQ https://flask-rq2.readthedocs.io/en/latest/
rq = RQ()

# Init Flask JWT https://pythonhosted.org/Flask-JWT/
jwt = JWT()

app = create_app()


# HANDLERS
# TODO: make Handlers better
@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found(error):
    return {"message": "not found"}, status.HTTP_404_NOT_FOUND


@app.errorhandler(JsonSchemaException)
def validation_exception(error):
    app.logger.error(error)
    return error.to_dict(), status.HTTP_406_NOT_ACCEPTABLE


@app.errorhandler(DatabaseError)
def database_exception(error):
    db.session.rollback()
    app.logger.error(error)

    # TODO: figure a way how to handle error output better
    return {"error": str(error)}, status.HTTP_500_INTERNAL_SERVER_ERROR


@app.errorhandler(NotFoundException)
def database_exception(error):
    db.session.rollback()
    app.logger.error(error)

    return error.to_dict(), status.HTTP_404_NOT_FOUND


@app.errorhandler(BadRequestException)
def database_exception(error):
    db.session.rollback()
    app.logger.error(error)

    return error.to_dict(), status.HTTP_400_BAD_REQUEST


@app.before_request
def before():
    helper.validate_json(app)

    # if request.method == 'DELETE':
    #    return {"prije": "prije"}, status.HTTP_204_NO_CONTENT
