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
uv add <package>
uv export > requirements.txt
```

### configure

1.
    ```shell
    cp .env.sample .env
    ```
2. fill `.env` file

### run

```shell
export $(grep -v '^#' .env | xargs)
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
