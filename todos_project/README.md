# README

## Initial Setup

These directories contain all project files following the initial creation of
this Django 3 project using these instructions:

1. django-admin startproject todos_project
2. cd todos_project
3. python manage.py startapp todos

## Deployment

### Python Version

3.8.10

### Django Version

3.2.8

### System Dependencies

#### Python

The python code base relies on the following packages being present:

* django-cors-headers
* djangorestframework
* requests

#### JavaScript

JQuery 3.6.0 [Included]

#### Bootstrap

Bootstrap 5.1.3 [Included]

#### Database

SQLite version 3.0 or higher is required if not installed already by Django

### Database Creation

python manage.py migrate

### How To Run The Test Suite

python manage.py test

### Instructions

#### Starting The Server

python manage.py runserver

#### Connecting To The Server

**http://localhost:8000/todos** .

## Notes