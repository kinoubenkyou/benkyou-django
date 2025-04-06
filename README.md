# benkyou-django

## development

### dependencies

- chromium
- pip
- postgresql
- python
- uv

### add package

```shell
uv add $package
```

### configure

1. 
   ```shell
   uv sync --all-groups
   ```
2.
   ```shell
   cp .env .env.local
   cp .env .env.container
   ```
3.
   - fill `.env.local` file
   - fill `.env.container` file

### run

```shell
export $(grep -v '^#' .env.local | xargs)
python manage.py runserver
```

### format

```shell
ruff format
```

### lint

```shell
ruff check --fix
```

### type check

```shell
export $(grep -v '^#' .env.local | xargs)
mypy .
```

### test

```shell
export $(grep -v '^#' .env.local | xargs)
coverage run --source=main manage.py test
coverage report -m
```

## build

### dependencies

- docker
- uv

### build image

```shell
uv export --no-dev --no-hashes > requirements.txt
docker build -t benkyou-django .
```

### run container

```shell
docker run --rm --env-file .env.container -p 127.0.0.1:8000:8000 benkyou-django python manage.py runserver 0.0.0.0:8000
docker run --rm --env-file .env.container benkyou-django celery -A benkyou_django worker
```
