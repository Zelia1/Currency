SHELL := /bin/bash

manage_py := docker exec -it backend python ./app/manage.py

build:
	docker-compose down && docker-compose up -d

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

pytest:
	pytest app/tests/ --cov=app --cov-report html && coverage report --fail-under=60

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

parser-rate-archive:
	$(manage_py) parser_rate_archive

uwsgi:
	cd app && uwsgi --http :8000 --module settings.wsgi --processes=4
