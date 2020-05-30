FROM python:3.8

# Docker won’t buffer the output from the application;
# instead, you will get to see your output in your console the way you’re used to
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/