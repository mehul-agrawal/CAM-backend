# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9.0-buster

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy requirements file from the host to the container
ADD ./requirements.txt /app/requirements.txt

# Install all needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app/
