import time
from uuid import uuid4

from .Logger import get_logger
# Import the ADS1x15 module.
from .adafruit import Adafruit_ADS1x15
from .aws.AwsIotCore import AwsIotCore


class App:
    LOGGER = get_logger(__name__)

    AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'
    AWS_IOT_MQTT_TOPIC = 'atlas'  # 'iot/devices/readings'
    AWS_CLIENT_ID = "iot-etape-" + str(uuid4())

    # Create an ADS1115 ADC (16-bit) instance.
    adc = Adafruit_ADS1x15.ADS1115()

    # Or create an ADS1015 ADC (12-bit) instance.
    # adc = Adafruit_ADS1x15.ADS1015()

    # Note you can change the I2C address from its default (0x48), and/or the I2C
    # bus by passing in these optional parameters:
    # adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

    def start(self):
        print('Reading ADS1x15 values, press Ctrl-C to quit...')
        # Print nice channel column headers.
        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
        print('-' * 37)
        while True:
            self._run()
            time.sleep(10)

    def _run(self):
        writer = AwsIotCore(endpoint=self.AWS_ENDPOINT, logger=self.LOGGER)
        writer.connect(self.AWS_CLIENT_ID)
        values = [0] * 4
        values[0] = adc.read_adc(0, gain=GAIN)
        values[1] = (adc.read_adc(0, gain=GAIN) / MAX_READ)
        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
