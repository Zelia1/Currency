# Generated by Django 3.2.3 on 2021-07-12 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_alter_banks_code_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='source',
        ),
    ]
