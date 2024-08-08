FROM python:3.12.4
WORKDIR /app
COPY requirements.txt .
RUN apt update
RUN apt install -y chromium
RUN pip install -r requirements.txt
