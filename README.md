# benkyou-django

## config

```shell
git config core.hooksPath hooks
touch django_secret_key
touch postgres_password
docker compose run --no-deps --rm app sh -c "tr -dc [:alnum:] < /dev/urandom | head -c 50 > django_secret_key"
docker compose run --no-deps --rm app sh -c "tr -dc [:alnum:] < /dev/urandom | head -c 20 > postgres_password"
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

## shell

```shell
docker compose run --no-deps --rm app sh
```

## lint and format

```shell
docker compose run --no-deps --rm app sh -c "ruff check --fix && ruff format"
```

## add package

```shell
docker compose run --no-deps --rm app sh -c "pip install <package> && pip freeze > requirements.txt"
docker compose build
docker compose down -v
```
