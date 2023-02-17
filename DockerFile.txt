FROM python:3.9-slim-buster

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the model file from Cloud Storage to the Docker image
RUN gsutil cp gs://spokendigitmodel/model /app/models/

# Copy the app code to the Docker image
COPY main.py main.py

# Start the app
CMD ["python", "main.py"]
