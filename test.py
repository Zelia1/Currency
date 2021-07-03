import requests
from currency.utils import to_decimal
from decimal import Decimal

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

