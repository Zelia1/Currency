from currency.models import ContactUs

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'  # noqa

    def handle(self, *args, **options):
        for index in range(100):
            fake = Faker()
            ContactUs.objects.create(

                email_from=f"{fake.first_name()}.{fake.word()}@{fake.free_email_domain()}",
                subject=fake.country(),
                message=fake.text()

            )
