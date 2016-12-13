from api.config import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TEST = True
    # POSTGRESQL_DATABASE = 'flask_api'
