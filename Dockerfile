FROM python:3.12.5
WORKDIR /app
RUN apt update -y
COPY requirements.txt .
RUN pip install -r requirements.txt
