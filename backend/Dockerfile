FROM python:3.11.5

COPY .  /backend
WORKDIR /backend/

RUN pip install -r requirements.txt

EXPOSE 8000

RUN adduser --disabled-password service-user

USER service-user
