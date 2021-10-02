FROM balenalib/raspberry-pi-debian:bullseye-build-20210912

MAINTAINER Sean Connolly <connolly.st@gmail.com>

RUN sudo apt-get update && \
    sudo apt-get install -y \
    python3-pip \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN python3 -m pip install -r requirements.txt

COPY src/main/python/*.py /
COPY src/main/python/app/*.py /app/
COPY src/main/python/app/adafruit/*.py /app/adafruit/
COPY src/main/python/app/adafruit/Adafruit_ADS1x15/*.py /app/adafruit/Adafruit_ADS1x15/
COPY src/main/python/app/aws/*.py /app/aws/
COPY certs/ /certs/

CMD [ "python3", "./main.py" ]