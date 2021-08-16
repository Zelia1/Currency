import datetime
from datetime import datetime as dt
from time import sleep

import requests
from currency import choices
from currency.models import Rate, Banks
from currency.utils import valid_parse_date, to_decimal
from django.core.management.base import BaseCommand
from currency import consts


class Command(BaseCommand):
    help = 'Generate Random records'  # noqa

    def handle(self, *args, **options):

        date_start = datetime.date(2014, 12, 1)
        date_end = dt.now().date()
        date = date_start

        available_currency_type = {
            'USD': choices.RATE_TYPE_USD,
            'EUR': choices.RATE_TYPE_EUR,
        }

        while True:
            date_parse = f'json&date={valid_parse_date(date)}'
            url = 'https://api.privatbank.ua/p24api/exchange_rates'
            response = requests.get(url, params=date_parse)
            response.raise_for_status()
            currency_list = response.json()['exchangeRate']
            currency_data = response.json()['date']

            for curr in available_currency_type:
                currencies_type = available_currency_type[curr]
                for row in currency_list:
                    if ("currency" in row and
                            curr in row["currency"] and
                            'saleRate' in row and
                            'purchaseRate' in row):

                        sale = to_decimal(row['saleRate'])
                        buy = to_decimal(row['purchaseRate'])
                        bank = Banks.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)

                        previous_rate = Rate.objects.filter(date=currency_data, type=currencies_type)\
                            .order_by('created').last()

                        if (
                                previous_rate is None or
                                previous_rate.sale != sale or
                                previous_rate.buy != buy
                        ):

                            Rate.objects.create(
                                bank=bank,
                                type=currencies_type,
                                sale=sale,
                                buy=buy,
                                date=currency_data,
                            )

            if date > date_end:
                break
            date += datetime.timedelta(days=1)
            sleep(7)
