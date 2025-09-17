FROM python:3.10-bookworm
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y netcat-openbsd
ADD requirements.txt /code/
RUN pip install -r requirements.txt