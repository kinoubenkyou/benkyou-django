# benkyou-django

## development

### dependencies

- chromium
- pip
- python
- uv

### add package

```shell
uv add <package>
uv export > requirements.txt
```

### configure

```shell
export DJANGO_SECRET_KEY=<django_secret_key>
```

### lint

```shell
ruff check --fix
```

### format

```shell
ruff format --preview
```
