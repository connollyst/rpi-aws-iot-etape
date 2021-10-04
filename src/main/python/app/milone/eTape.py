import time
from threading import Thread

from ..adafruit import Adafruit_ADS1x15


class eTape:
    NAME = "rpi-ads1115-etape"
    TYPE = "level"
    MODULE = "eTape"
    DEFAULT_ADDRESS = "0x48"
    # Choose a gain of 1 for reading voltages from 0 to 4.09V.
    # Or pick a different gain to change the range of voltages that are read:
    #  - 2/3 = +/-6.144V
    #  -   1 = +/-4.096V
    #  -   2 = +/-2.048V
    #  -   4 = +/-1.024V
    #  -   8 = +/-0.512V
    #  -  16 = +/-0.256V
    # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
    GAIN = 1
    MAX_READ = 30782
    SAMPLE_COUNT = 10
    EDGE_SAMPLE_COUNT = 3

    def __init__(self, host=None, adc=None, logger=None):
        if not host:
            raise RuntimeError("host required")
        self._host = host
        self._logger = logger
        # Note you can change the I2C address from its default (0x48), and/or the I2C
        # bus by passing in these optional parameters:
        # adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)
        self._adc = adc or Adafruit_ADS1x15.ADS1115()
        self._address = int(self.DEFAULT_ADDRESS, 0)
        self._running = False
        self._value = None
        self._thread = None

    def start(self):
        self._logger.info("Starting eTape..")
        self._running = True
        self._thread = Thread(target=self._take_samples, args=(0, self.GAIN))
        self._thread.start()

    def _take_samples(self, index, gain):
        while self._running:
            self._value = self._adc.read_adc(index, gain=gain)
            self._logger.info("Took sample: {}".format(self._value))
            time.sleep(0.5)

    def stop(self):
        self._running = False
        self._thread.join()

    def read(self):
        return self._value

    def to_json(self):
        return {
            "name": self.NAME,
            "module": self.MODULE,
            "version": "0.3",
            "host": self._host.identifier,
            "addressType": "I2C",
            "address": self._address,
            "reading": {
                "type": self.TYPE,
                "value": self._value,
                "timestamp": time.time()
            }
        }
