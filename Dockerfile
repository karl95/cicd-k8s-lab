# Use a specific version for consistency
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY app.py .

EXPOSE 5000

# Command to run the app
CMD ["python", ".github/workflows/ci.yml"]
