FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /graph-with-django-graphene

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
