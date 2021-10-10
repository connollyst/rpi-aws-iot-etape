import unittest
from unittest.mock import MagicMock

from src.main.python.app.Logger import get_logger
from src.main.python.app.milone.eTapeReader import eTapeReader


class test_eTapeReader(unittest.TestCase):
    LOGGER = get_logger(__name__)

    def test_should_create_eTape_reader(self):
        eTapeReader(host=MagicMock(), adc=MagicMock(), logger=self.LOGGER)


if __name__ == '__main__':
    unittest.main()
