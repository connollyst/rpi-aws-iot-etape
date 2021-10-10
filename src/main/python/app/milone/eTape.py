import statistics
import time
from collections import deque


class eTape:
    NAME = "rpi-ads1115-etape"
    TYPE = "level"
    MODULE = "eTape"
    MIN_INDEX = 0
    MAX_INDEX = 3
    MIN_GAIN = 0
    MAX_GAIN = 1
    MIN_READ = 4650
    MAX_READ = 30782
    SAMPLE_COUNT = 10

    def __init__(self, index, gain, logger=None):
        if index not in range(self.MIN_INDEX, self.MAX_INDEX + 1):
            raise ValueError('index {} is outside valid range: {}-{}'.format(index, self.MIN_INDEX, self.MAX_INDEX))
        self._index = index
        if gain not in range(self.MIN_GAIN, self.MAX_GAIN + 1):
            raise ValueError('gain {} is outside valid range: {}'.format(gain, range(self.MIN_GAIN, self.MAX_GAIN)))
        self._gain = gain
        self._logger = logger
        self._value = None
        self._values = deque()
        self._variance = {}

    def read(self, adc):
        self._value = adc.read_adc(self._index, self._gain)
        self._logger.debug("eTape #{}: {}".format(self._index, self._value))
        self._values.append(self._value)
        if len(self._values) > self.SAMPLE_COUNT:
            self._values.popleft()
        return self._value

    def variance(self):
        samples = list(self._values)
        if not samples:
            return 0
        pvariance = statistics.pvariance(samples)
        pstdev = statistics.pstdev(samples)
        mean = statistics.mean(samples)
        cv = pstdev / mean
        self._variance = {
            'pvariance': pvariance,
            'pstdev': pstdev,
            'mean': mean,
            'cv': cv
        }
        return round(cv, 2)

    def to_json(self):
        return {
            "type": self.TYPE,
            "index": self._index,
            "gain": self._gain,
            "raw": self._value,
            "value": round(self._value / self.MAX_READ, 4),
            "variance": self._variance,
            "timestamp": time.time()
        }
