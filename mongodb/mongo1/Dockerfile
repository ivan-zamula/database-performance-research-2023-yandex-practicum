FROM python:3.11-slim

WORKDIR /opt/app

ENV PYTHONPATH /opt/etl_app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

COPY ./src ./

COPY docker-entrypoint.sh docker-entrypoint.sh
RUN ["chmod", "+x", "/opt/app/docker-entrypoint.sh"]
ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]