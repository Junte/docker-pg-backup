FROM python:3.8-alpine3.10

ENV PGHOST='localhost:5432' \
    PGDATABASE='postgres' \
    PGUSER='postgres@postgres' \
    PGPASSWORD='password'

WORKDIR /src

RUN apk update && apk add postgresql-client

COPY dumper.py .

ENTRYPOINT [ "python", "dumper.py" ]