SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver