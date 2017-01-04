from unittest import TestLoader, TextTestRunner, TestSuite
from flask_script import Command
from api.tests.DataTestCase import DataTestCase


class TestsCommand(Command):
    def run(self):
        # Create test suite
        loader = TestLoader()
        suite = TestSuite((
            loader.loadTestsFromTestCase(DataTestCase)
        ))

        runner = TextTestRunner(verbosity=2)
        runner.run(suite)
