SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver

createsuperuser:
	$(manage_py) createsuperuser

shell:
	$(manage_py) shell_plus --print-sql

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate
