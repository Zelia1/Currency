import random

from currency.models import Banks

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):

    help = 'Closes the specified poll for voting' # noqa

    def handle(self, *args, **options):
        for index in range(100):
            fake = Faker()
            banks_list = ["Monobank", "Privatbank", "Ukrsibbank", "Sberbank", "PUMB"]
            name_bank = random.choice(banks_list)
            Banks.objects.create(

                name=name_bank,
                url=fake.uri_path(),
                email_from=f"{name_bank}@gmail.com",
                number_phone=fake.phone_number(),


            )
