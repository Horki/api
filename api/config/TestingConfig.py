from api.config import BaseConfig


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    # POSTGRESQL_DATABASE = 'flask_api_testing'
