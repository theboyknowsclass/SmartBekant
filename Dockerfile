FROM balenalib/rpi-debian:buster-run
ENTRYPOINT []

RUN apt-get update && \
    apt-get -qy install curl ca-certificates
    
USER root

CMD ["curl", "-SL", "https://docker.com"]
