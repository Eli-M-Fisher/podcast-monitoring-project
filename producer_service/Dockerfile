# use Python base image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy dependency files
COPY requirements.txt /app/requirements.txt

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# and copy producer service code
COPY . /app

# default command
CMD ["python", "main.py"]