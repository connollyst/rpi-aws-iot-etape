import time

from ..adafruit import Adafruit_ADS1x15


class eTape:
    NAME = "rpi-ads1115-etape"
    TYPE = "level"
    MODULE = "eTape"

    GAIN = 1
    MAX_READ = 30782
    SAMPLE_COUNT = 10
    EDGE_SAMPLE_COUNT = 3

    def __init__(self, host=None, adc=None, logger=None):
        if not host:
            raise RuntimeError("host required")
        self._host = host
        self._logger = logger
        self._adc = adc or Adafruit_ADS1x15.ADS1115()
        self._address = 72
        self._value = None

        # Note you can change the I2C address from its default (0x48), and/or the I2C
        # bus by passing in these optional parameters:
        # adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

    def read(self):
        self._value = self._adc.read_adc(0, gain=self.GAIN)
        return self._value

    def to_json(self):
        return {
            "name": self.NAME,
            "module": self.MODULE,
            "version": "0.2",
            "host": self._host.identifier,
            "addressType": "I2C",
            "address": self._address,
            "reading": {
                "type": self.TYPE,
                "value": self._value,
                "timestamp": time.time()
            }
        }
