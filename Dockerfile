FROM resin/rpi-raspbian:latest
ENTRYPOINT []

RUN apt-get update && \
    apt-get -qy install python

CMD ["curl", "https://docker.com"]
