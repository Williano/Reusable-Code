# Pull base image
FROM python:3.8-slim

# Set environment varibales
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy project
COPY . /code/
