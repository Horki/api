from api.app import app

import unittest
from api.config.config import configure_app


class DataTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_data(self):
        resp = self.app.get('/data/test')
        assert resp.status_code == 200
