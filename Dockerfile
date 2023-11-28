# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container
COPY requirements.txt ./

# Install required Python packages
RUN apt-get update && apt-get install -y build-essential
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY mitm.py ./

# Command to run mitmdump with the Python script when the container starts
CMD ["mitmdump", "-s", "./mitm.py"]
