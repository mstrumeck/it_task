FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

COPY server /app/server
COPY /uwsgi.ini /app/uwsgi.ini

ENV FLASK_APP=/server/flask_server.py
ENV FLASK_DEBUG=False
