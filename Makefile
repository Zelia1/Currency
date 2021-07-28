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

worker:
	cd app && celery -A settings worker -l info

beat:
	cd app && celery -A settings beat -l info

show_urls:
	$(manage_py) show_urls
