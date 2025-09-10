# use Python base imag
FROM python:3.11-slim

# set working directry
WORKDIR /app

# copy dependency files
COPY analyzer_service/requirements.txt /app/requirements.txt

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy common utilities
COPY common /app/common

# and copy analyzer service code
COPY analyzer_service /app

# default command
CMD ["python", "main.py"]