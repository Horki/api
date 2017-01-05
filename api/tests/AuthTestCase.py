from flask_api import status
import unittest
from faker import Factory

from api.app import app
import api.tests.helpers as helpers


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.faker = Factory.create('hr_HR')

    def tearDown(self):
        pass

    def test_get_auth_all(self):
        uri = '/auth/all'
        resp = self.app.get(uri)
        helpers.validate_json(resp, uri, 'get')
        assert resp.status_code == status.HTTP_200_OK

    def test_post_auth_register(self):
        uri = '/auth/register'
        data = {
            "username": self.faker.name(),
            "email": self.faker.email(),
            "password": "123456"
        }
        resp = self.app.post(uri, data=data)
        helpers.validate_json(resp, uri, 'post')
        assert resp.status_code == status.HTTP_201_CREATED

    def test_get_activate_user(self):
        pass

    def test_post_login(self):
        pass

    def test_get_me(self):
        pass

    def test_unauthorized(self):
        uri = '/auth/me'
        resp = self.app.get(uri)
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    def test_not_acceptable(self):
        uri = '/auth'
        resp = self.app.post(uri, data={})
        assert resp.status_code == status.HTTP_406_NOT_ACCEPTABLE
        uri = '/auth/register'
        resp = self.app.post(uri, data={})
        assert resp.status_code == status.HTTP_406_NOT_ACCEPTABLE
