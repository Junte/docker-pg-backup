FROM alpine:3.9

ENV PGHOST='localhost:5432' \
    PGDATABASE='postgres' \
    PGUSER='postgres@postgres' \
    PGPASSWORD='password'

RUN apk update && apk add postgresql-client

RUN mkdir /pg_backup

COPY dump_db.sh .

ENTRYPOINT [ "/bin/sh" ]
CMD [ "./dump_db.sh" ]