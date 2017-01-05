from flask_api import status
import unittest

from api.app import app


class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_all_books(self):
        pass

    def test_post_add_book(self):
        pass

    def test_get_books_by_user(self):
        pass

    def test_get_book_by_id(self):
        pass

    def test_edit_book_by_id(self):
        pass

    def test_delete_book_by_id(self):
        pass

    def test_unauthorized(self):
        # TODO: this is pretty bad figure out how to add notations
        uri = '/books'
        resp = self.app.get(uri)
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED
        uri = '/books/'
        resp = self.app.post(uri, data={})
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED
        uri = '/books/me'
        resp = self.app.get(uri)
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED
        uri = '/books/1'
        resp = self.app.get(uri)
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED
        uri = '/books/1'
        resp = self.app.put(uri, data={})
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED
        uri = '/books/1'
        resp = self.app.delete(uri)
        assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    def test_not_acceptable(self):
        pass
