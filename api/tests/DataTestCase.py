from flask_api import status
import unittest

from api.app import app
import api.tests.helpers as helpers


# from api.config import configure_app


class DataTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_data(self):
        uri = '/data/test'
        resp = self.app.get(uri)
        helpers.validate_json(resp, uri, 'get')
        assert resp.status_code == status.HTTP_200_OK

    def test_get_cache(self):
        uri = '/data/cache'
        resp = self.app.get(uri)
        helpers.validate_json(resp, uri, 'get')
        assert resp.status_code == status.HTTP_200_OK

    def test_get_empty(self):
        uri = '/data/empty'
        resp = self.app.get(uri)
        assert resp.status_code == status.HTTP_204_NO_CONTENT

    def test_add_empty(self):
        uri = '/data/add'
        data = {
            "testing": "testing"
        }
        resp = self.app.post(uri, data=data)

        assert resp.status_code == status.HTTP_201_CREATED
