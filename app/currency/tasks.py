from celery import shared_task
from currency.utils import to_decimal

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

    for curr in currencies:
        currencies_type = curr['ccy']
        if currencies_type in available_currency_type:
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, type=currencies_type).order_by('created').last()

            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):

                Rate.objects.create(
                    type=currencies_type,
                    buy=buy,
                    sale=sale,
                    source=source,
                )

@shared_task
def parse_vkurse():
    from currency.models import Rate

    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    available_currency_type = {'Dollar': 'USD', 'Euro': 'EUR'}
    currencies = response.json()

    source = 'vkurse'

    for curr in currencies:
        if curr in available_currency_type:
            currencies_type = available_currency_type[curr]
            buy = to_decimal(currencies[curr]['buy'])
            sale = to_decimal(currencies[curr]['sale'])

            previous_rate = Rate.objects.filter(source=source, type=currencies_type).order_by('created').last()

            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    type=currencies_type,
                    buy=buy,
                    sale=sale,
                    source=source,
                )


@shared_task
def parse_monobank():
    from currency.models import Rate

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.json()
    response.raise_for_status()
    available_currency_type = {840: 'USD', 978: 'EUR'}
    available_currency_type_second = 980
    currencies = response.json()

    source = 'monobank'

    for curr in currencies:
        validity_label_one = curr['currencyCodeA']
        validity_label_two = curr['currencyCodeB']

        if validity_label_one in available_currency_type and validity_label_two == available_currency_type_second:
            currencies_type = available_currency_type[validity_label_one]
            buy = to_decimal(curr['rateBuy'])
            sale = to_decimal(curr['rateSell'])

            previous_rate = Rate.objects.filter(source=source, type=currencies_type).order_by('created').last()

            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
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
