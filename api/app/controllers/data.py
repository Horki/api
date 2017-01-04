from flask import Blueprint, request
from injector import inject
import redis
from flask_api import status

mod_data = Blueprint('data', __name__, url_prefix='/data')


# Basic Hello World output
@mod_data.route('/test', methods=['GET'])
def get_data_count():
    return {"test": "test"}, status.HTTP_200_OK


# Test Redis Via DI
@mod_data.route('/cache', methods=['GET'])
@inject(re=redis.Redis)
def get_data_redis_b(re):
    re.set('foo', 'bar')
    result_output = re.get('foo').decode("utf-8")
    return {"redis": result_output}, status.HTTP_200_OK


@mod_data.route('/empty', methods=['GET'])
def get_data_empty():
    return "", status.HTTP_204_NO_CONTENT


@mod_data.route('/add', methods=['POST'])
def post_data_empty():
    data = request.data
    return data, status.HTTP_201_CREATED
