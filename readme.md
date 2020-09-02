# My Site Rest API

[![Build Status](https://travis-ci.org/jjpaulo2/mysite-rest-api.svg?branch=master)](https://travis-ci.org/jjpaulo2/mysite-rest-api)

This repository contains the source code from my GitHub personal's website back-end. It was made with [**Django**](https://www.djangoproject.com/) and [**Django Rest Framework**](https://www.django-rest-framework.org).

## Dependency management

The project was build using `Pipenv (2020.8)`. Make sure it's installed and install the project dependencies.

```shell
$ pipenv install
```

### Application dependencies

- [django](https://pypi.org/project/Django/) (3.1)
- [djangorestframework](https://pypi.org/project/djangorestframework/) (3.11)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (0.14)

## Environment variables

The environment variables may been setted into `mysite/config/.env` file.

```shell
SECRET_KEY="xxx..."
```