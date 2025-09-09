FROM python:3.11-slim

# set working directory
WORKDIR /app

# i needed to install system dependencies for audio processing ((ffmpeg is required)l.f)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# copy dependency files
COPY transcriber_service/requirements.txt /app/requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy common utilities
COPY common /app/common

# copy transcriber service code
COPY transcriber_service /app

# default command
CMD ["python", "main.py"]