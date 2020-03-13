#!/usr/bin/env python

import os
import subprocess
import pathlib

from datetime import datetime

BASE_BACKUP_PATH = "/pg_backup"
LATEST_LINK = "latest.dump"

databases = [
    db_name.strip()
    for db_name in os.environ.get("BACKUP_DATABASES", "").split(",")
    if db_name.strip()
]

print("Databases to dump: {}".format(databases), flush=True)


def dump_database(db_name: str) -> subprocess.CompletedProcess:
    dest_path = "{base}/{db_name}".format(base=BASE_BACKUP_PATH, db_name=db_name)
    pathlib.Path(dest_path).mkdir(parents=True, exist_ok=True)
    filename = "backup_{:%Y-%m-%d_%H:%M}.dump".format(datetime.now())

    dest_file = "{path}/{file}".format(path=dest_path, file=filename,)

    if db_name == "__all__":
        dump_cmd = ["pg_dumpall", "--clean"]
    else:
        dump_cmd = ["pg_dump", "-d", db_name, "-w", "--format", "c"]

    with open(dest_file, "w") as outfile:
        exe_result = subprocess.run(dump_cmd, stdout=outfile)

    if exe_result.returncode == 0:
        os.chdir(dest_path)

        if os.path.exists(LATEST_LINK):
            os.unlink(LATEST_LINK)

        os.symlink(filename, LATEST_LINK)

    return exe_result


for database in databases:
    print("# Backup database: {} ... ".format(database), end="", flush=True)

    result_msg = "ok"
    try:
        proc_result = dump_database(database)
    except Exception as err:
        result_msg = "fail [err: {}]".format(err)
    else:
        if proc_result.returncode != 0:
            result_msg = "fail [ret code: {}]".format(proc_result.returncode)

    print(result_msg)

