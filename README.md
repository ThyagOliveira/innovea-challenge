## General Instructions

To set up the environment, create a .env file following the example in [.env.example](.env.example) and then execute the following commands:

```
$ docker-compose build
$ docker-compose up
$ docker-compose run app python manage.py migrate
```

To create a superuser:
```
$ docker-compose run app python manage.py createsuperuser
```

To run the tests use:

```
$ docker-compose run app python manage.py test
```

In general, you can use the following to run commands in the django application container:
```
$ docker-compose run app <command>
```

To access the API documentation:

```
http://0.0.0.0:8000/api/swagger/
```
