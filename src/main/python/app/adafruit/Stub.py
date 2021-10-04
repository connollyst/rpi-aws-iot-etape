class Stub:

    def __init__(self, logger=None):
        logger.info("Using stub!")
        self._value = 0

    def read_adc(self, index, gain):
        self._value += 100
        return self._value
