# benkyou-django

## config

```shell
docker compose run --rm app python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" > django_secret_key
docker compose run --rm app sh -c "tr -dc [:graph:] < /dev/urandom | head -c 20 > postgres_password"
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
docker exec -it benkyou-django-app-1 sh
```
