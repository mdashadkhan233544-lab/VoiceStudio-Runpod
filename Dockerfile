# Base image with Python and CUDA (GPU support)
FROM runpod/pytorch:2.2.1-py3.10-cuda12.1.1-devel-ubuntu22.04

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git ffmpeg

# Clone VoiceStudio repository
RUN git clone https://github.com/debpalash/VoiceStudio.git .

# Install Runpod and other requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our custom Runpod handler script
COPY handler.py .

# Start the serverless handler
CMD ["python", "-u", "/app/handler.py"]