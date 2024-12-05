# Use an official Python image

########################################
# Build stage
########################################
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
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


# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Set Django settings module for production during build (if necessary for collectstatic)
# This can be overridden at runtime using docker-compose or environment variables.
ENV DJANGO_SETTINGS_MODULE=mysite.settings.production

# Collect static files
RUN python manage.py collectstatic --noinput

########################################
# Final Runtime Stage
########################################
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libffi-dev \
    libssl-dev \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code and static files from builder
COPY --from=builder /app /app

# Expose port 8000
EXPOSE 8000

# In production, you would run Gunicorn, for example:
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]
