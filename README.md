# graph-with-django-graphene

### Run in Local

```commandline
python manage.py runserver
```

### Run With Docker

After docker run you need to run migration
```docker
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```


## Environment Variable

```dotenv
SECRET_KEY=must-define
DEBUG=True

POSTGRES_DB=must-define
POSTGRES_USER=must-define
POSTGRES_PASSWORD=must-define
POSTGRES_HOST_PORT=must-define
POSTGRES_CONTAINER_PORT=must-define

DJANGO_HOST_PORT=must-define
DJANGO_CONTAINER_PORT=must-define
```