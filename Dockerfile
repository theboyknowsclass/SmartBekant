FROM balenalib/rpi-python:latest-run
ENTRYPOINT []

RUN apt-get update && \
    apt-get -qy install curl ca-certificates

CMD ["curl", "https://docker.com"]
