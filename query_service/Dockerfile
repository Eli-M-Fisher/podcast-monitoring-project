# use Python base image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy dependency files
COPY query_service/requirements.txt /app/requirements.txt

# need install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy common utilities
COPY common /app/common

# and copy query service code
COPY query_service /app

# default command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]