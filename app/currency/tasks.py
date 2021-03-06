import requests
from bs4 import BeautifulSoup
from celery import shared_task
from currency import choices
from currency import consts
from currency.utils import to_decimal, valid_number
from django.core.mail import send_mail
from fake_useragent import UserAgent


def _get_privatbank_currencies(url):
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task
def parse_privatbank():
    from currency.models import Rate, Banks

    bank = Banks.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)
    currencies = _get_privatbank_currencies(bank.url)
    available_currency_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    for curr in currencies:
        currencies_type = curr['ccy']
        if currencies_type in available_currency_type:
            currencies_type = available_currency_type[curr['ccy']]

            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(bank=bank, type=currencies_type).order_by('created').last()

            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):

                Rate.objects.create(
                    type=currencies_type,
                    buy=buy,
                    sale=sale,
                    bank=bank,
                )


@shared_task
def parse_vkurse():
    from currency.models import Rate, Banks

    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    available_currency_type = {
        'Dollar': choices.RATE_TYPE_USD,
        'Euro': choices.RATE_TYPE_EUR,
    }
    currencies = response.json()

    bank = Banks.objects.get(code_name=consts.CODE_NAME_VKURSE)

    for curr in currencies:
        if curr in available_currency_type:
            currencies_type = available_currency_type[curr]
            buy = to_decimal(currencies[curr]['buy'])
            sale = to_decimal(currencies[curr]['sale'])

            previous_rate = Rate.objects.filter(bank=bank, type=currencies_type).order_by('created').last()

            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    type=currencies_type,
                    buy=buy,
                    sale=sale,
                    bank=bank,
                )


@shared_task
def parse_monobank():
    from currency.models import Rate, Banks

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.json()
    response.raise_for_status()
    available_currency_type = {
        840: choices.RATE_TYPE_USD,
        978: choices.RATE_TYPE_EUR,
    }
    available_currency_type_second = 980
    currencies = response.json()

    bank = Banks.objects.get(code_name=consts.CODE_NAME_MONOBANK)

    for curr in currencies:
        validity_label_one = curr['currencyCodeA']
        validity_label_two = curr['currencyCodeB']

        if validity_label_one in available_currency_type and validity_label_two == available_currency_type_second:
            currencies_type = available_currency_type[curr['currencyCodeA']]
            buy = to_decimal(curr['rateBuy'])
            sale = to_decimal(curr['rateSell'])

            previous_rate = Rate.objects.filter(bank=bank, type=currencies_type).order_by('created').last()
            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    type=currencies_type,
                    buy=buy,
                    sale=sale,
                    bank=bank,
                )


@shared_task
def parse_eximb():
    from currency.models import Rate

    url = 'https://www.eximb.com/services/v1/rates/'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    available_currency_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }
    data = currencies['rates']['cash']['data']

    source = 'eximb'

    for curr in data:
        if curr['code'] in available_currency_type:
            currencies_type = available_currency_type[curr['code']]
            buy = to_decimal(valid_number(curr['buy']))
            sale = to_decimal(valid_number(curr['sell']))

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
def parse_pumb():
    url = 'https://about.pumb.ua/ru/info/currency_converter'
    header = {'User-Agent': UserAgent().firefox}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('div', {'class': 'exchange-rate'}).find_all('td', limit=6)
    available_currency_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    currencies = {}

    for curr_from_data in data:
        if data.index(curr_from_data) < 3:
            if curr_from_data.text in available_currency_type:
                currencies[curr_from_data.text] = []
            else:
                currencies['USD'].append(curr_from_data.text)
        else:
            if curr_from_data.text in available_currency_type:
                currencies[curr_from_data.text] = []
            else:
                currencies['EUR'].append(curr_from_data.text)

    source = 'pumb'

    for curr in currencies:
        from currency.models import Rate

        if curr in available_currency_type:
            currencies_type = available_currency_type[curr]
            buy = to_decimal(currencies[curr][0])
            sale = to_decimal(currencies[curr][1])

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
