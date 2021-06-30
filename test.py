import requests

from currency.models import Rate


def parse_privatbank():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()
    available_carrency_type = frozenset(('USD', 'EUR'))
    carrencies = response.json()

    source = 'privatbank'

    for carr in carrencies:
        carrencies_type = carr['ccy']
        if carrencies_type in available_carrency_type:
            buy = carr['buy']
            sale = carr['sale']

            Rate.odjects.create(
                type=carrencies_type,
                buy=buy,
                sale=sale,
                source=source,
            )

