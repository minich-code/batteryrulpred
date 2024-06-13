# Base Image Selection:
FROM python:3.11-slim-buster

    
# Setting Working Directory:
# This line sets the working directory inside the container to /app. This is where your application code will be copied.
WORKDIR /app

# Copying Application Code:
# This command copies all the files from the current directory (where the Dockerfile is located) into the /app directory in the Docker container.
COPY . /app

# Installing Python Dependencies:
RUN pip install --no-cache-dir -r requirements.txt

# Exposing Port
EXPOSE 8080

# Setting Default Command:
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
