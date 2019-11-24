#!/usr/bin/env python

import os
import subprocess
import pathlib

from datetime import datetime

BASE_BACKUP_PATH = "/pg_backup"

databases = os.environ.get("BACKUP_DATABASES", "").split(",")

print("Databases to dump: {}".format(databases))


def dump_database(db_name: str):
    print("Backup database: {}".format(db_name))

    dest_path = "{base}/{db_name}".format(base=BASE_BACKUP_PATH, db_name=db_name)
    pathlib.Path(dest_path).mkdir(parents=True, exist_ok=True)

    dest_file = "{path}/{file}".format(
        path=dest_path, file="backup_{:%Y-%m-%d_%H:%M}.dump".format(datetime.now()),
    )

    dump_cmd = ["pg_dump", "-d", db_name, "-w", "--format", "c"]
    with open(dest_file, "w") as outfile:
        proc_result = subprocess.run(dump_cmd, stdout=outfile)

    print("return code = {}".format(proc_result.returncode))


for database in databases:
    dump_database(database.strip())
