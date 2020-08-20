# Defining the language package
FROM python:3.8-alpine

# Setting the maintainer label
LABEL maintainer="robnmrz"

ENV PYTHONUNBUFFERED 1

# Define the dependencies and install them via "requirement.txt" file
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Creating the directory
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Adding a user and select that user as active USER
RUN adduser -D user
USER user