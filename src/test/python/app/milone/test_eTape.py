import unittest
from unittest.mock import MagicMock, Mock

from src.main.python.app.Logger import get_logger
from src.main.python.app.milone.eTape import eTape


class test_App(unittest.TestCase):
    LOGGER = get_logger(__name__)

    def test_should_create_sensor(self):
        eTape(host=MagicMock(), adc=MagicMock(), logger=self.LOGGER)

    def test_should_call_adc_when_reading_sensor(self):
        # Given
        mock_adc = MagicMock()
        sensor = eTape(host=MagicMock(), adc=mock_adc, logger=self.LOGGER)
        # When
        sensor.read(0, 1)
        # Then
        mock_adc.read_adc.assert_called()

    def test_should_return_raw_reading_in_json(self):
        # Given
        raw_value = 42
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock(return_value=raw_value)
        sensor = eTape(host=MagicMock(), adc=mock_adc, logger=self.LOGGER)
        # When
        sensor.read(0, 1)
        # Then
        self.assertEqual(raw_value, sensor.to_json()['reading']['raw'])

    def test_should_return_relative_reading_in_json(self):
        # Given
        raw_value = 42
        relative_value = round(raw_value / eTape.MAX_READ, 4)
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock(return_value=raw_value)
        sensor = eTape(host=MagicMock(), adc=mock_adc, logger=self.LOGGER)
        # When
        sensor.read(0, 1)
        # Then
        self.assertEqual(relative_value, sensor.to_json()['reading']['value'])


if __name__ == '__main__':
    unittest.main()
