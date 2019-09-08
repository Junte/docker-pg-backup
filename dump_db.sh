DUMP_FILE_NAME="backup_`date +%Y-%m-%d-%H-%M`.dump"
echo "Creating dump: $DUMP_FILE_NAME"

cd /pg_backup

pg_dump -w --format=c > $DUMP_FILE_NAME

if [ $? -ne 0 ]; then
  rm $DUMP_FILE_NAME
  echo "Backup is not created, check db connection settings"
  exit 1
fi

echo 'Successfully Backed Up'
exit 0