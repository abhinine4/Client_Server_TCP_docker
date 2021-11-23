FROM python:3.8-slim-buster

ADD jokeServer.py /server/
ADD client_handshake.txt /server/

RUN pip install requests

WORKDIR /server/