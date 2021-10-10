import unittest
from unittest.mock import MagicMock, Mock

from src.main.python.app.Logger import get_logger
from src.main.python.app.milone.eTape import eTape


class test_eTape(unittest.TestCase):
    LOGGER = get_logger(__name__)
    DEFAULT_INDEX = 0
    DEFAULT_GAIN = 0
    DEFAULT_VALUE = 42

    def test_should_create_sensor_with_high_gain(self):
        eTape(index=self.DEFAULT_INDEX, gain=1, logger=self.LOGGER)

    def test_should_create_sensor_with_low_gain(self):
        eTape(index=self.DEFAULT_INDEX, gain=0, logger=self.LOGGER)

    def test_should_not_create_sensor_with_very_high_gain(self):
        self.assertRaises(
            ValueError,
            eTape,
            index=self.DEFAULT_INDEX, gain=2, logger=self.LOGGER
        )

    def test_should_not_create_sensor_with_very_low_gain(self):
        self.assertRaises(
            ValueError,
            eTape,
            index=self.DEFAULT_INDEX, gain=-1, logger=self.LOGGER
        )

    def test_should_call_adc_when_reading_sensor(self):
        # Given
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock(return_value=self.DEFAULT_VALUE)
        sensor = eTape(index=self.DEFAULT_INDEX, gain=self.DEFAULT_GAIN, logger=self.LOGGER)
        # When
        sensor.read(mock_adc)
        # Then
        mock_adc.read_adc.assert_called()

    def test_should_return_raw_reading_in_json(self):
        # Given
        raw_value = 42
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock(return_value=raw_value)
        sensor = eTape(index=self.DEFAULT_INDEX, gain=self.DEFAULT_GAIN, logger=self.LOGGER)
        # When
        sensor.read(mock_adc)
        # Then
        print(sensor.to_json())
        self.assertEqual(raw_value, sensor.to_json()['raw'])

    def test_should_return_relative_reading_in_json(self):
        # Given
        raw_value = 42
        relative_value = round(raw_value / eTape.MAX_READ, 4)
        mock_adc = MagicMock()
        mock_adc.read_adc = Mock(return_value=raw_value)
        sensor = eTape(index=self.DEFAULT_INDEX, gain=self.DEFAULT_GAIN, logger=self.LOGGER)
        # When
        sensor.read(mock_adc)
        # Then
        self.assertEqual(relative_value, sensor.to_json()['value'])


if __name__ == '__main__':
    unittest.main()
