FROM python:3.8.6-buster

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt
ENV run_env=docker
CMD gunicorn -c gunicorn.py -k uvicorn.workers.UvicornWorker main:app