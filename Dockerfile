FROM ahmedsajid/uwsgi-nginx-flask:python3.9 as base

COPY requirements.txt requirements.txt
COPY ./app/main.py /app/main.py
COPY ./app/templates /app/templates

RUN apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get -y install libpq-dev \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/cache /var/lib/log /var/lib/apt/lists/* \
    && pip install -r requirements.txt

FROM scratch
COPY --from=base / /

ENV PYTHONPATH=/app
ENV UWSGI_INI=/app/uwsgi.ini
ENV UWSGI_CHEAPER=2
ENV UWSGI_PROCESSES=16
ENV NGINX_MAX_UPLOAD=0
ENV NGINX_WORKER_PROCESSES=1
ENV LISTEN_PORT=80
ENV STATIC_URL=/static
ENV STATIC_PATH=/app/static
ENV STATIC_INDEX=0
ENV DB_URI="sqlite:///todo.sqlite"

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
