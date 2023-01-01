FROM python:3.9-slim

COPY requirements.txt /root

WORKDIR /root

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#
#ENTRYPOINT ["alembic","upgrade","head"]