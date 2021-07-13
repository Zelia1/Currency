from django.db import migrations


def forwards(apps, schema_editor):
    Rate = apps.get_model('currency', 'Rate')
    Banks = apps.get_model('currency', 'Banks')

    privat = Banks.objects.create(
        name='privat',
        url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
        email_from='Privat@gmail.com',
        number_phone='458762287642523',
    )

    for rate in Rate.objects.all():
        if 'privat' in rate.source.lower():
            rate.bank = privat

        rate.save()


def backwards(apps, schema_editor):
        pass # noqa


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_rate_bank'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]
