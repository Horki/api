import os
import logging
import redis
from datetime import timedelta
from os.path import join, dirname
from flask_api import FlaskAPI
from dotenv import load_dotenv
from flask_injector import FlaskInjector

from api.app.controllers.auth import mod_auth
from api.app.controllers.data import mod_data
from api.app.controllers.book import mod_book


class BaseConfig(object):
    # load ENV file
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    DEBUG = True
    TESTING = True
    # LOGGING
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'bookshelf.log'
    LOGGING_LEVEL = logging.DEBUG

    # JWT
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # JWT_AUTH_URL_RULE = '/auth/login' # somehow this doesn't work?
    JWT_AUTH_ENDPOINT = 'jwt'
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_PASSWORD_KEY = 'password'
    JWT_AUTH_HEADER_PREFIX = "JWT"
    JWT_EXPIRATION_DELTA = timedelta(minutes=10)
    JWT_VERIFY_EXPIRATION = True
    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # RQ Redis QUEUE
    RQ_REDIS_URL = 'redis://%s:%s/%s' % (os.environ.get(
        "REDIS_HOST"), os.environ.get("REDIS_PORT"), os.environ.get("REDIS_DB")
    )
    RQ_QUEUES = ['default']
    RQ_ASYNC = True
    RQ_SCHEDULER_QUEUE = 'default'
    RQ_SCHEDULER_INTERVAL = 1
    # MAIL
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT"))
    MAIL_USE_SSL = bool(os.environ.get("MAIL_USE_SSL"))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class DevelopmentConfig(BaseConfig):
    DEBUG = True  # Flask Mail will work only if DEBUG is set to False
    TESTING = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False  # Flask Mail will work now
    TESTING = False


config = {
    "development": "api.config.DevelopmentConfig",
    "testing": "api.config.TestingConfig",
    "default": "api.config.DevelopmentConfig",
    "production": "api.config.ProductionConfig",
}


def configure_app(app):
    config_name = os.getenv('FLAKS_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)


def configure_di(binder):
    # Add via DI
    binder.bind(
        redis.Redis,
        to=redis.Redis(
            host=os.environ.get("REDIS_HOST"),
            port=os.environ.get("REDIS_PORT"),
            db=os.environ.get("REDIS_DB")))


# TODO: add all services to DI?
def create_app():
    try:
        from api.app import db, ma, rq, jwt
        # Init
        app = FlaskAPI(__name__)

        # Register routes
        app.register_blueprint(mod_data)
        app.register_blueprint(mod_auth)
        app.register_blueprint(mod_book)

        # Configure app
        configure_app(app)

        # Connect to Database
        db.init_app(app)

        # Configure Marshmallow for beautiful APIs responses
        ma.init_app(app)

        # Configure Redis Queue
        rq.init_app(app)

        # Configure Flask JSON Web Token, JWT
        from api.app.controllers.auth import authenticate, identity
        jwt.authentication_handler(authenticate)
        jwt.identity_handler(identity)
        jwt.init_app(app)

        # Init DI
        FlaskInjector(app=app, modules=[configure_di], use_annotations=True)

        return app
    except BaseException as error:
        # in case something bad happen
        app.logger.error(error)
