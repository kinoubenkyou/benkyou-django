FROM python:3.12.5
WORKDIR /app
RUN apt update -y
RUN apt install -y chromium
COPY requirements.txt .
RUN pip install -r requirements.txt
