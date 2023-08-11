# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container
COPY requirements.txt ./

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install mitmproxy
RUN pip install mitmproxy

# Copy the current directory contents into the container
COPY mitm.py ./

# Command to run mitmdump with the Python script when the container starts
CMD ["mitmdump", "-s", "./mitm.py"]
