FROM python:3.12.5
WORKDIR /app
RUN apt update -y
RUN apt install -y chromium chromium-driver
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN echo DEBUG1
RUN echo DEBUG
