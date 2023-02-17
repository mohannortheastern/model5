



# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application files to the working directory
COPY . .

# Set the PORT environment variable
ENV PORT 8080

# Expose the PORT specified by the PORT environment variable
EXPOSE $PORT

# Start the microservice with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
