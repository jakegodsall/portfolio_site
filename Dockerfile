FROM python:3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY .. /code/

EXPOSE 8000

# Run the production server
ENTRYPOINT ["python", "portfolio_site/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]