FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && \
    apt-get install -y curl && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY read_data.py .

ENTRYPOINT ["python3" ,"read_data.py" ]