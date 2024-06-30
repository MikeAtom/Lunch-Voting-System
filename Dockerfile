FROM ubuntu:latest
LABEL authors="Mike"

ENTRYPOINT ["top", "-b"]