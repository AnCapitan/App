FROM python:3.11.5

COPY ./backend /tmp/backend
COPY ./requirements.txt /tmp/backend

WORKDIR /tmp/backend/

RUN pip install -r requirements.txt

EXPOSE 5000

RUN adduser --disabled-password service-user
