from django.core.management.base import BaseCommand
from currency.models import ContactUs

from faker import Faker


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for index in range(100):
            fake = Faker()
            ContactUs.objects.create(
                email_from=f"{fake.first_name()}.{fake.word()}@{fake.free_email_domain()}",
                subject=fake.country(),
                message=fake.text()

            )