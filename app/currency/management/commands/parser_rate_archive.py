import datetime
import random
import requests

from currency import choices
from currency.models import RateArchive
from currency.utils import valid_parse_date

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate Random records'  # noqa

    def handle(self, *args, **options):

        date_start = datetime.date(2014, 12, 1)
        date_end = datetime.date(2021, 8, 10)
        date = date_start
        date_parse = valid_parse_date(date)
        bank_name = "Privatbank"

        available_currency_type = {
            'USD': choices.RATE_TYPE_USD,
            'EUR': choices.RATE_TYPE_EUR,
        }

        while True:
            date_parse = valid_parse_date(date)
            url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date_parse}'
            response = requests.get(url)
            response.raise_for_status()
            currency_list = response.json()['exchangeRate']
            currency_data = response.json()['date']

            # validated_curr = ["USD", "EUR"]
            validated_data_currency = []
            for curr in available_currency_type:
                currencies_type = curr
                for row in currency_list:
                    if curr in row['currency']:
                        RateArchive.objects.create(
                            name=bank_name,
                            type=currencies_type,
                            sale=row['saleRate'],
                            buy=row['purchaseRate'],
                            date=row['date'],
                        )
                        # validated_data_currency.append(row)
                        # row['date'] = currency_data

            if date > date_end:
                break
            date += datetime.timedelta(days=1)
