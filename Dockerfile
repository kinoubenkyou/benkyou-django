FROM python:3.13.1
WORKDIR /app
COPY . .
RUN pip install -r build.requirements.txt
