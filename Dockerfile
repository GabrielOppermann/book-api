# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory to /app in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the current directory contents into container at /app
COPY ./ /app/

# Command to run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]