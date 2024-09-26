FROM python:3.12.5
WORKDIR /app
RUN apt update -y
RUN apt install -y chromium chromium-driver
COPY requirements.txt .
RUN echo DEBUG
RUN pip install -r requirements.txt
