from flask import Blueprint
from injector import inject
import redis

mod_data = Blueprint('data', __name__, url_prefix='/data')


# Basic Hello World output
@mod_data.route('/test', methods=['GET'])
def get_data_count():
    return {"hello": "world"}


# Test Redis Via DI
@mod_data.route('/cache', methods=['GET'])
@inject(re=redis.Redis)
def get_data_redis_b(re):
    re.set('foo', 'aaa')
    result = re.get('foo').decode("utf-8")
    return {"redis": result}
