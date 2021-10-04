import unittest
from unittest.mock import MagicMock

from src.main.python.app.App import App


class test_App(unittest.TestCase):

    def test_should_create_app(self):
        App(sensor=MagicMock(), aws=MagicMock(), logger=MagicMock())
