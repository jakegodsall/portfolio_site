# Use an official Python image
FROM python:3.13-slim

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    rustc \
    cargo \
    git \
    libffi-dev \
    libssl-dev \
    libsqlite3-dev \
    zlib1g-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Copy the requirements file into the container
COPY ./requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ../../../.. /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000