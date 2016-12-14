import redis
from flask_api import FlaskAPI
from flask_injector import FlaskInjector

from api.app.controllers.data import mod_data
from api.config.config import configure_app
import api.app.helpers


# Add via DI
def configure(binder):
    binder.bind(
        redis.Redis,
        to=redis.Redis(host='localhost', port=6379, db=0)
    )


app = FlaskAPI(__name__, instance_relative_config=True)
app.register_blueprint(mod_data)
# Configure app
# configure_app(app)
FlaskInjector(app=app, modules=[configure], use_annotations=True)


# Json errors for common errors
@app.errorhandler(406)
def not_allowed(error):
    return helpers.make_error(406, 1001, "Route not allowed.")


@app.errorhandler(404)
def not_found(error):
    return helpers.make_error(404, 1002, "Route not found.")


# Todo, add Postgre SQL
# Initialize db
# db.init_app(app)
