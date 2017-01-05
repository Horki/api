from unittest import TestLoader, TextTestRunner, TestSuite
from flask_script import Command
from api.tests.DataTestCase import DataTestCase
from api.tests.AuthTestCase import AuthTestCase
from api.tests.BookTestCase import BookTestCase


class TestsCommand(Command):
    def run(self):
        # Create test suite
        # TODO: Figure out how to add notations to test method
        # TODO: How to create a dummy database for testing
        # TODO: How to load different config ENV
        # TODO: Find a better API testing framework
        loader = TestLoader()
        suite = TestSuite((
            loader.loadTestsFromTestCase(DataTestCase),
            # loader.loadTestsFromTestCase(AuthTestCase),
            # loader.loadTestsFromTestCase(BookTestCase)
        ))

        runner = TextTestRunner(verbosity=2)
        runner.run(suite)
