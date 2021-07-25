# Pull base image
FROM python:3.8-slim

# File Author / Maintainer
MAINTAINER william kwabla "paawilly17@gmail.com"

# Set environment varibales
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/

# Copy Static files
RUN python manage.py collectstatic --noinput

