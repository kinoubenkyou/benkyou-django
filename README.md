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
uv export --no-dev > build.requirements.txt
```

### configure

1. 
   ```shell
   uv sync --all-groups
   ```
2.
    ```shell
    cp .env .env.local
    ```
3. fill `.env.local` file

### run

```shell
export $(grep -v '^#' .env.local | xargs)
python manage.py runserver
```

### lint

```shell
ruff check --fix
```

### format

```shell
ruff format
```

### test

```shell
coverage run --source=main manage.py test
coverage report
```

## build

### dependencies

- docker

### configure

1.
    ```shell
    cp .env .env.container
    ```
2. fill `.env.container` file

### build image

```shell
docker build -t $image .
```

### push image

```shell
docker push ${image}:latest
```

### run container

```shell
docker run --rm --env-file .env.container -p 127.0.0.1:8000:8000 $image python manage.py runserver 0.0.0.0:8000
```
