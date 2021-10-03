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
        sensor.read()
        # Then
        mock_adc.read_adc.assert_called()

    def test_should_call_adc_when_reading_sensor2(self):
        # Given
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock(return_value=12345)
        sensor = eTape(host=MagicMock(), adc=mock_adc, logger=self.LOGGER)
        # When
        sensor.read()
        json = sensor.to_json()
        # Then
        self.assertEqual(12345, json['reading']['value'])


if __name__ == '__main__':
    unittest.main()
