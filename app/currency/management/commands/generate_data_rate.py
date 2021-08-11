import random

from currency.models import Rate
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate Random records'  # noqa

    def handle(self, *args, **options):
        source_list = ['monobank', 'privatbank', 'vkurse']
        for index in range(100):
            Rate.objects.create(

                type=random.choice(('usd', 'eur')),
                sale=random.uniform(20.00, 29.99),
                buy=random.uniform(20.00, 29.99),
                source=random.choice(source_list),

            )
