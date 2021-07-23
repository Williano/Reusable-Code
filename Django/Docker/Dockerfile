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
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/

# Create staticfiles
RUN mkdir -p /code/staticfiles/

# Copy Static files
CMD python manage.py collectstatic --noinput

# Run database migrations
CMD python manage.py migrate

# Start server
CMD gunicorn kotoko_express_dashboard.wsgi
