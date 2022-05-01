## Lenguages and Technologs Used 

<div style="display: inline_block"> <br>
    <img align="center", alt="python3", src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img align="center", alt="python3", src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

</div> <br>

- `Python: 3.8.10`
- `djangorestframework: 3.13.1`
- `Django: 4.0.2`
- `django-filter: 21.1`
- `Docker version: 20.10.12`
- `docker-compose: 1.29.2`

<br>

## Quickstart

<br>

Installng a virtual env:
`pip3 install virtualenv`

create a virtualenv:
`python3 -m venv venv`

Starting your virtualenv:
`source venv/bin/activate`

Necessary packages instalation:
`pip3 install -r requeriments.txt`

create migrations:
`python3 manage.py makemigrations`

migrating on database:
`python3 manage.py migrate`

Create a user:
`python3 manage.py createsuperuser`

~~~
- Input: Username
- Input: Email
- Input: Password
- Input: Confime password
~~~

Seeder generator:
`python3 manage.py seed core --number=10`

Getting the Token:
`python3 manage.py drf_create_token Your_Username`

Start server
`python3 manage.py runserver`

## Routes

~~~
http://localhost:8000/documentation - GET DOCUMENTATIO
http://localhost:8000/ - GET ALL URLS
http://localhost:8000/admin - Controll Panel Django
http://localhost:8000/swagger/ - Swagger documentation
http://localhost:8000/redoc/ - Swagger documentation
http://localhost:8000/api/v1/token/ - Create token for your user
http://localhost:8000/api/v1/token/refresh/ - Refresh your Token
~~~
