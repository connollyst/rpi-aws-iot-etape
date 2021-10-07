import sys

import fake_rpi

from app.App import App
from app.Logger import get_logger
from app.milone.eTapeReader import eTapeReader
from app.rpi.Host import Host

LOGGER = get_logger(__name__)


class FakeADC:
    MAX_VALUE = 2000

    def __init__(self, logger=None):
        logger.warning("Using fake analog to digital converter (ADC)")
        self._value = 0

    def read_adc(self, index, gain):
        self._value += 100
        if self._value > self.MAX_VALUE:
            self._value += 1000
        return self._value


if __name__ == '__main__':
    sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)
    fake_host = Host()
    fake_adc = FakeADC(LOGGER)
    fake_tape = eTapeReader(host=fake_host, adc=fake_adc, logger=LOGGER)
    fake_app = App(logger=LOGGER, sensor=fake_tape)
    fake_app.start()
