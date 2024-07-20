FROM python:3.12.4
RUN apt update
RUN apt install -y chromium
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
