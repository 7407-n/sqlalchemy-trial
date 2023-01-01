FROM python:3.9-slim

WORKDIR /root

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONUTF8=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on

COPY requirements.txt /root

RUN pip install --upgrade pip  \
    pip install -r requirements.txt
#
#ENTRYPOINT ["alembic","upgrade","head"]