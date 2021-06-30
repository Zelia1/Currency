from celery import shared_task

import requests

from django.core.mail import send_mail


@shared_task
def parse_privatbank():
    from currency.models import Rate

    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()
    available_currency_type = frozenset(('USD', 'EUR'))
    currencies = response.json()

    source = 'privatbank'

    for carr in currencies:
        currencies_type = carr['ccy']
        if currencies_type in available_currency_type:
            buy = carr['buy']
            sale = carr['sale']

            Rate.objects.create(
                type=currencies_type,
                buy=buy,
                sale=sale,
                source=source,
            )



@shared_task
def send_email_contactus(body):
    send_mail(
        'Hello from contactus!',
        body,
        'PavelTest1990@gmail.com',
        ['zelenskiy.zelia@gmail.com'],
        fail_silently=False,
    )
