import os
from flask import json
from jsonschema import validate


# General error assertion function


def assert_error(resp, status, code):
    data = json.loads(resp.data)
    assert data['code'] == code
    assert resp.status_code == status


def validate_json(resp, uri, http_method='GET'):
    validate(
        json.loads(
            resp.data), json.loads(
            open(
                os.path.abspath(
                    'schemas/%s/%s/response.schema.json' %
                    (uri, http_method.lower()))).read()))
