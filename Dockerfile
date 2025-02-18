FROM python:3.13.1
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt
WORKDIR /app
COPY benkyou_django benkyou_django/
COPY main main/
COPY manage.py .
