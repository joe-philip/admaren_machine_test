# Django Rest API app

## Requirements

- Python >=3.11.6

## Seting up project locally

1. Create virtual environment `python -m venv env`
1. Activate virtual environment `source env/bin/activate`
1. Install Requirements `pip install -r requirements.txt`
1. Create `.env` file
    ```
    SECRET_KEY
    ALLOWED_HOSTS
    DEBUG
    DATABASE_URL
    ```
1. Make migrations `python manage.py makemigrations`
1. Apply migrations `python manage.py migrate`
1. Run server `python manage.py runserver`

## .env variables

###### SECRET_KEY
A secret key used to sign cookies and other sensitive data. defaults to `django-insecure-r=#*ay%+%kw5fuso3-g!yv4z-fh$46r(44s8t!(bd()c0t-71p`. Random key can be generated using `python manage.py secret_key_gen`.
###### ALLOWED_HOSTS
List of hostnames that are allowed to access the app. defaults to `[]`
###### DEBUG
Set to `True` to enable debug mode. defaults to `False`
###### DATABASE_URL
The URL of the database to use. defaults to `sqlite:///{PROJECT_DIR}/db.sqlite3`,
use `postgresql://{user}:{password}@{host}:{port}/{db_name}` for using the application with postgresql
#### ACCESS_TOKEN_LIFETIME_SECONDS
Lietime of access token in seconds, defaults to `0`
#### ACCESS_TOKEN_LIFETIME_MINUTES
Lietime of access token in minutes, defaults to `0`
#### ACCESS_TOKEN_LIFETIME_HOURS
Lietime of access token in hours, defaults to `0`
#### REFRESH_TOKEN_LIFETIME_SECONDS
Lietime of refresh token in seconds, defaults to `0`
#### REFRESH_TOKEN_LIFETIME_MINUTES
Lietime of refresh token in minutes, defaults to `0`
#### REFRESH_TOKEN_LIFETIME_HOURS
Lietime of refresh token in seconds, defaults to `0`
