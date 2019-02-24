# Django Rest Framework with React
Basic rest api tutorial with Django and React, hosted on Divio Cloud.

## Get started
ToDo

## Useful commands

Migrate the database
```
docker-compose run web python manage.py migrate
```

Run style guide tests
```
docker-compose run --rm web sh -c "flake8"
```

Start the project
```
divio project up
```

Shut it down
```
divio project stop
```

Run a command in a specific container, such as:
```
docker-compose run --rm --service-ports web bash
python manage.py runserver 0.0.0.0:80
```

Check what Docker processes are running:
```
docker ps
```