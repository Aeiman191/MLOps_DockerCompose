# Use the official Python image as base
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the content of the local backend directory to the working directory
COPY . .

# Command to run the Flask application
CMD ["python", "app.py"]
