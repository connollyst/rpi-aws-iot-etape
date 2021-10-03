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

    def test_should_take_average_of_readings(self):
        # Given
        avg_value = 1
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock()
        mock_adc.read_adc.side_effect = [avg_value for _ in range(eTape.SAMPLE_COUNT)]
        sensor = eTape(host=MagicMock(), adc=mock_adc, logger=self.LOGGER)
        # When
        reading = sensor.read()
        # Then
        self.assertEqual(avg_value, reading)

    def test_should_take_average_of_readings_excluding_edges(self):
        # Given
        avg_value = 1
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock()
        mock_adc.read_adc.side_effect = [0, 0, 0, avg_value, avg_value, avg_value, avg_value, 0, 0, 0]
        sensor = eTape(host=MagicMock(), adc=mock_adc, logger=self.LOGGER)
        # When
        reading = sensor.read()
        # Then
        self.assertEqual(avg_value, reading)

    def test_should_return_reading_in_json(self):
        # Given
        avg_value = 42
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock()
        mock_adc.read_adc.side_effect = [avg_value for _ in range(eTape.SAMPLE_COUNT)]
        sensor = eTape(host=MagicMock(), adc=mock_adc, logger=self.LOGGER)
        # When
        sensor.read()
        # Then
        self.assertEqual(avg_value, sensor.to_json()['reading']['value'])


if __name__ == '__main__':
    unittest.main()
