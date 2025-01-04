########################################
# Builder stage
########################################
FROM python:3.13-alpine AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_ENV=development

# Install required system dependencies
RUN apk update && apk add --no-cache \
    build-base \
    rust \
    cargo \
    git \
    libffi-dev \
    openssl-dev \
    sqlite-dev \
    zlib-dev \
    curl


# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/

# Install dependencies
RUN python3 -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Set Django settings module for production during build (if necessary for collectstatic)
# This can be overridden at runtime using docker-compose or environment variables.
ENV DJANGO_SETTINGS_MODULE=portfolio_site.settings.production

########################################
# Final Runtime Stage
########################################
FROM python:3.13-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_ENV=production

WORKDIR /app

# Install runtime dependencies
RUN apk update && apk add --no-cache \
    libffi-dev \
    openssl-dev \
    sqlite-dev

# Copy installed Python packages from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code and static files from builder
COPY --from=builder /app /app

# Expose port 8000
EXPOSE 8000

# In production, you would run Gunicorn, for example:
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio_site.wsgi:application"]
