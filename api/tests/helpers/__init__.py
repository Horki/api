from flask import json

# General error assertion function


def assert_error(resp, status, code):
    data = json.loads(resp.data)
    assert data['code'] == code
    assert resp.status_code == status
