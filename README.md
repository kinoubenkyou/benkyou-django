# benkyou-django

## config

```shell
git config core.hooksPath hooks
tr -dc [:alnum:] < /dev/urandom | head -c 50 > django_secret_key
tr -dc [:alnum:] < /dev/urandom | head -c 20 > postgres_password
docker compose run --rm app sh -c "python manage.py migrate"
```

## start

```shell
docker compose up -d
```

## stop

```shell
docker compose stop
```

## test

```shell
docker compose run --rm app sh -c "python manage.py test"
```

## fix code style

```shell
docker compose run --rm app sh -c "ruff check --fix"
docker compose run --rm app sh -c "ruff format"
```

## shell

```shell
docker exec -it benkyou-django-app-1 sh
```
