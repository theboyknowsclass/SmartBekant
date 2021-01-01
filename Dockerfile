FROM balenalib/rpi-python:latest-run
ENTRYPOINT []

RUN apt-get update && \
    apt-get -qy install curl ca-certificates
    
USER root

CMD ["curl", "-SL", "https://docker.com"]
