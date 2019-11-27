FROM python:3.8-slim-buster

ENV PG_MAJOR 12
ENV PG_CLIENT_VERSION 12

ENV PGHOST='localhost:5432' \
    PGUSER='postgres@postgres' \
    PGPASSWORD='password'

WORKDIR /src

RUN apt-get update \
    && apt-get install -y --no-install-recommends gnupg \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \
    && sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main $PG_MAJOR" > /etc/apt/sources.list.d/pgdg.list' \
    && apt-get update \
    && apt-get install -y postgresql-client-$PG_CLIENT_VERSION

COPY dumper.py .

ENTRYPOINT [ "python", "dumper.py" ]