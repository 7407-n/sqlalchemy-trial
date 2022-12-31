FROM python:3.9-slim

RUN mkdir -p /root/src
COPY docker/alembic/requirements.txt /root/src
WORKDIR /root/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt