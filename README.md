# benkyou-django

## config

```shell
touch django_secret_key
docker compose run --no-deps --rm --volume .:/app app sh -c "tr -dc [:alnum:] < /dev/urandom | head -c 50 > django_secret_key"
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
docker compose run --no-deps --rm --volume .:/app app sh
```

## add package

```shell
docker compose run --no-deps --rm --volume .:/app app sh -c "pip install <package> && pip freeze > requirements.txt"
docker compose build
docker compose down -v
```
