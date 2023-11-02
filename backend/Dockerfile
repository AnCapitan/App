# Используйте образ, который содержит как Python, так и Node.js
FROM python:3.11.5

COPY .  /backend
WORKDIR /backend/

RUN pip install -r requirements.txt

EXPOSE 5000

RUN adduser --disabled-password service-user

USER service-user
