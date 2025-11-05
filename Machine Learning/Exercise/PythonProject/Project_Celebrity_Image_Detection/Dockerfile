# Base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . /app

COPY model/facenet_keras.h5 /root/.deepface/weights/

RUN mkdir -p /root/.deepface/weights
COPY model/arcface_weights.h5 /root/.deepface/weights


# Install system dependencies and CA certificates
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY model/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "server/server.py"]