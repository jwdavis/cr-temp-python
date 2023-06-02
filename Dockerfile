# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app