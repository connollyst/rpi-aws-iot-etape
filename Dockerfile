FROM balenalib/raspberry-pi-debian:bullseye-build-20210912

MAINTAINER Sean Connolly <connolly.st@gmail.com>

COPY requirements.txt /
RUN python3 -m pip install -r requirements.txt

COPY src/main/python/*.py /

CMD [ "python3", "./main.py" ]