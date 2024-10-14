# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script and other necessary files
COPY DevOps-app.py .

# Copy the templates and static folders
COPY templates/ ./templates/
COPY static/ ./static/

# Command to run the application
CMD ["python", "DevOps-app.py"]

