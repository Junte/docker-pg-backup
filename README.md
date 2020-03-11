# docker-pg-backup

Docker container for quick setup postgres backup

Example `backup.sh`:

```
#! /bin/bash

set -o errexit
set -o nounset

cd /opt/esanum/services/postgres

source .env

docker run \
    -e PGHOST=<pg_host> \
    -e PGUSER=<pg_user> \
    -e PGPASSWORD=<pg_password> \
    -e BACKUP_DATABASES=databases1,database2 \
    -v <host_backups_folder>:/pg_backup \
    junte/pg-backup:1.3-client12
```

If "BACKUP_DATABASES=\__all__" - alldump will be executed