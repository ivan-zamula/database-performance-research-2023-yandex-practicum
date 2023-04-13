FROM python:3.10-slim as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

COPY requirements.txt .

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

FROM base as performance
CMD ["python", "-m", "run"]

