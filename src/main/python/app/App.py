import json
import time
from uuid import uuid4

from .Logger import get_logger
from .aws.AwsIotCore import AwsIotCore
from .milone.eTape import eTape
from .rpi.Host import Host


class App:
    LOGGER = get_logger(__name__)

    AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'
    AWS_IOT_MQTT_TOPIC = 'atlas'  # 'iot/devices/readings'
    AWS_CLIENT_ID = "iot-milone-" + str(uuid4())

    def __init__(self, sensor=None, aws=None):
        self._sensor = sensor or eTape(host=Host(), logger=self.LOGGER)
        self._writer = aws or AwsIotCore(endpoint=self.AWS_ENDPOINT, logger=self.LOGGER)
        self._running = False

    def start(self):
        # Every half second take a reading
        # Calculate the current rate of change
        # The higher the rate of change, the more frequent messaging to AWS IoT
        self._running = True
        self._sensor.start()
        while self._running:
            try:
                self._run()
                time.sleep(5)
            except KeyboardInterrupt:
                self.LOGGER.info("Stopping..")
                self._running = False
                self._sensor.stop()

    def _run(self):
        if self._sensor.read():
            self._writer.connect(self.AWS_CLIENT_ID)
            self._writer.write(self.AWS_IOT_MQTT_TOPIC, json.dumps(self._sensor.to_json(), indent=4, default=str))
            self._writer.disconnect()
