FROM python:3.9

WORKDIR /home/build

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uwsgi", "--http", "0.0.0.0:8000", "--chdir", "/home/build/app", "--module", "settings.wsgi", "--processes=4"]

