from flask import Blueprint, current_app as app, request
from flask_jwt import jwt_required, current_identity
from flask_api import status

from api.app.exceptions.NotFoundException import NotFoundException

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


def authenticate(email, password):
    from api.app.models.User import User
    user = User.query.filter_by(email=email, active=True).first()

    if user and user.check_password(password) is True:
        return user


def identity(payload):
    app.logger.error(payload)
    from api.app.models.User import User
    user_id = payload['identity']
    return User.query.filter_by(id=user_id, active=True).first()


# Login
# Done via FLASK-JWT
# @mod_auth.route('/login', methods=['POST'])
# def post_login():
#    from api.app import jwt
#    data = request.data
#    app.logger.error(data)
#    user = authenticate(data['email'], data['password'])
#    if user is None:
#        raise BadRequestException('Invalid email or password')
#
#    return {"data": True}, status.HTTP_200_OK


@mod_auth.route('/all', methods=['GET'])
def get_all():
    from api.app.models.User import User, UserSchema
    users = User.query.filter_by(active=True).all()
    user_schema = UserSchema(many=True)

    return {"data": user_schema.dump(users).data}, status.HTTP_200_OK


@mod_auth.route('/register', methods=['POST'])
def post_register():
    from api.app import db
    from api.app.models.User import User
    from api.app.jobs.mail import send_mail

    data = request.data
    user = User(
        username=data['username'],
        password=data['password'],
        email=data['email'])

    db.session.add(user)

    db.session.commit()

    send_mail.queue(user)

    return {"message": "Hej %s, please check your email: %s." % (
        data['username'], data['email'])}, status.HTTP_201_CREATED


@mod_auth.route('/activate/<string:token>', methods=['GET'])
def get_activate(token):
    from api.app.models.User import User
    from api.app import db
    user = User.query.filter_by(token=token).first()
    if user is None:
        raise NotFoundException('Non existing user')
    user.active = True
    db.session.commit()

    return {"message": "User '%s' is activated" %
                       user.username}, status.HTTP_200_OK


@mod_auth.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    from api.app.models.User import UserSchema
    user_schema = UserSchema()
    return {"data": user_schema.dump(
        current_identity).data}, status.HTTP_200_OK
