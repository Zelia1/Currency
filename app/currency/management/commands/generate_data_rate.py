from django.core.management.base import BaseCommand
from currency.models import Rate

import random


class Command(BaseCommand):
    help = 'Generate Random records'

    def handle(self, *args, **options):
        source_list = ['monobank', 'privatbank', 'vkurse']
        for index in range(100):
            Rate.objects.create(
                type=random.choice(('usd', 'eur')),
                sale=random.uniform(20.00, 29.99),
                buy=random.uniform(20.00, 29.99),
                source=random.choice(source_list),

            )