# README

## Initial Setup

These directories contain all project files following the initial creation of
this Django 3 project using these instructions:

1. ```django-admin startproject todos_project```
2. ```cd todos_project```
3. ```python manage.py startapp todos```

## Deployment

### Python Version

Python version 3.8.10 is used for this project.

### Django Version

Django version 3.2.8 is used for this project.

### System Dependencies

#### Python

The file *requirements.txt* states all Python packages needed in this project.

* asgiref version 3.4.1
* certifi version 2021.10.8
* charset-normalizer version 2.0.7
* django version 3.2.8
* django-cors-headers version 3.10.0
* djangorestframework version 3.12.4
* idna version 3.3
* pytz version 2021.3
* requests version 2.26.0
* sqlparse version 0.4.2
* urllib3 version 1.26.7

#### JavaScript

jQuery 3.6.0 is included in this project.

#### Bootstrap

Bootstrap 5.1.3 is included in this project.

#### Database

SQLite version 3.0 or higher is required if not installed already by Django.

### Database Creation

```python manage.py migrate```

### How To Run The Test Suite

```python manage.py test```

### Instructions

#### Starting The Server

```python manage.py runserver```

#### Connecting To The Server

Open the link **http://localhost:8000/todos** in a web browser.

## Notes

1. This code represents a self-contained Django 3 project that can be run in Docker.
2. The code is not optimized, particularly the JavaScript part. Improvements in 
responsiveness will be seen by using a React front-end communicating by REST API 
to the Django 3 back-end.
3. SQLite 3 is the database used. A switch to PostgreSQL is recommended for a
production system.
4. An API key from Openweathermap (http://openweathermap.org) must be provided in 
file *./todos_project/settings.py* in order for weather data to be brought in.