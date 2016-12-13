import os

config = {
    "development": "api.config.DevelopmentConfig",
    "testing": "api.config.TestingConfig",
    "default": "api.config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('FLAKS_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
