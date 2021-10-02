import time
from uuid import uuid4

from .Logger import get_logger
from .aws.AwsIotCore import AwsIotCore


class App:
    LOGGER = get_logger(__name__)

    AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'
    AWS_IOT_MQTT_TOPIC = 'atlas'  # 'iot/devices/readings'
    AWS_CLIENT_ID = "iot-etape-" + str(uuid4())

    def start(self):
        print('Starting!')
        while True:
            self._run()
            time.sleep(10)

    def _run(self):
        writer = AwsIotCore(endpoint=self.AWS_ENDPOINT, logger=self.LOGGER)
        writer.connect(self.AWS_CLIENT_ID)
