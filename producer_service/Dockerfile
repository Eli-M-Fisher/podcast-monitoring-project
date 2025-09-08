# use Python base image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy dependency files
COPY producer_service/requirements.txt /app/requirements.txt

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy common utilities
COPY common /app/common

# and copy producer service code
COPY producer_service /app

# default command
CMD ["python", "main.py"]