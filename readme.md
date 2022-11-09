# Introduction
A RESTful API for tracking IOUs. Four roommates have a habit of borrowing money from each
other frequently, and have trouble remembering who owes whom, and how much. This application helps them keep track of how much money they borrowed and how much thet gave out as loan.

# How to install/run?

## Create virtual environment

```sh
python -m venv .venv
source .venv/bin/activate
```

### Install the requirements

```sh
pip install -r requirements.txt
```
### Make migrations and migrate if required
The project already has a demo sqlite db. If you would like to add a new database backend, please modify settings.py file and run the migrations

```sh
python manage.py makemigrations
python manage.py migrate
```
### Run the server

```sh
python manage.py runserver
```

# Running test cases
In order to run the test cases, make sure you have pytest installed in your test environment and run the below command.
```sh
pytest
```

# Documentation
The api documentation is available at `/docs`

# Demo

A demo project is hosted at [demo46.justhomas.in](https://demo46.justhomas.in)

# New Features / Scaling options
- Replacing SQLite with a database backend like PostgreSQL.
- Proper authentication to make sure that a third party cannot make fake entries.
- Payment Gateway integration to make it easier to transfer money through this app and keep records of transfers.
- Splitting the app to smaller services (user authentication service, service for managing and displaying iou entrieds etc...)  so that they can be developed and scale independantly.

