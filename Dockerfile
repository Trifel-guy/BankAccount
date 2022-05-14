FROM python:3.9-alpine


WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:/.
# Install and configure dependencies
RUN apk add --no-cache build-base libressl-dev musl-dev libffi-dev

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app/ .