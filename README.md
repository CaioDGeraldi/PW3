# PW3 — Django classroom project

An educational Django application. This repository is not a production deployment.

## Run locally

1. Create a Python virtual environment and install dependencies from `requirements.txt`.
2. Copy `.env.example` to `.env` and replace the sample `DJANGO_SECRET_KEY` with a new random secret. The project loads `.env` using `python-dotenv`.
3. Run `python manage.py migrate` to create a fresh local SQLite database.
4. Run `python manage.py runserver`.

Never upload `.env` or `db.sqlite3` to Git. To generate a Django secret locally, run:

```sh
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Security note

Earlier commits tracked a `.env` file and a SQLite database. These files were removed from the current branch, but their history may still be accessible. Any previously exposed secret must be rotated or invalidated. Do not use classroom keys or database records in deployed environments.
