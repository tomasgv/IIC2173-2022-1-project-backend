# ./django-docker/app/Dockerfile
FROM python:3.7.5-buster

# set work directory
WORKDIR /opt/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./celery/requirements.txt /opt/requirements.txt 
RUN chmod +x /opt/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./celery /opt/
