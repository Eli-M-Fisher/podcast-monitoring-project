FROM python:3.11-slim

# set working directory
WORKDIR /app

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