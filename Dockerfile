FROM python:3.5

MAINTAINER Michelle D. Zhang <zhang.michelle.d@gmail.com>

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Add dockerize, which will add a command we can use to wait for
# dependent containers to finish setup (instead of just startup)
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.1.0/dockerize-linux-amd64-v0.1.0.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.1.0.tar.gz

RUN mkdir /opt/grpc_python_example/
WORKDIR /opt/grpc_python_example/

ARG GIT_COMMIT
ENV GIT_COMMIT $GIT_COMMIT

# Docker caches packages so that this line is only re-run
# when requirements change
RUN mkdir /opt/grpc_python_example/requirements
ADD ./requirements/*.txt /opt/grpc_python_example/requirements/
RUN pip install -r requirements/dev.txt

COPY . /opt/grpc_python_example

# Server and clients are run from same container
# so rely on docker compose to determine command
CMD []
