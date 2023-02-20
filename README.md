# backend

- cp .env.template .env
- poetry install
- docker compose up -d
- poetry export --without-hashes -f requirements.txt --output requirements.txt
- poetry shell
- ./manage.py migrate

### Install pre-commit:

- pre-commit install

### Test:

coverage run --source='.' manage.py test --no-input && coverage html && coverage report --skip-covered

### Celery:

celery -A main worker -l info

### Celery Beat:

celery -A main beat -l info

### Run both Celery and Celery Beat in one process
celery -A main worker -l info -B

### Backup & Restore db:

./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db_backups/{backup_name}.json
./manage.py dumpdata backend > db_backups/{backup_name}.json

./manage.py loaddata db_backups/{backup_name}.json

### docker compose

docker compose up -d
docker-compose up -d --no-deps --build web celery

### branch naming Convention

https://dev.to/couchcamote/git-branching-name-convention-cch

https://dev.to/i5han3/git-commit-message-convention-that-you-can-follow-1709

# JSON return structure:

## HTTP Status code need to reflect result

- 200: OK
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 500: Internal Server Error

### OK

```
{
  "data": []
}

{
  "data": {}
}

{
  "data": "Primitive Data like Integer, Float, String, Boolean"
}
```

### Error

```
{
  "message": {
    "token": [
      "This field is required."
    ]
  }
}

{
  "message": "Error message"
}
```
