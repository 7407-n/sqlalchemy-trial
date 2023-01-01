FROM python:3.9-slim

RUN mkdir -p /root/src
COPY src /root/src
COPY docker/app/requirements.txt /root

WORKDIR /root

RUN pip install --upgrade pip
RUN pip install -r requirements.txt