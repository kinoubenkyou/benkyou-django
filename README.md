# benkyou-django

## add package

```shell
docker compose run --no-deps --rm --volume .:/app app sh -c "pip install <package> && pip freeze > requirements.txt"
docker compose build
docker compose down -v
```
