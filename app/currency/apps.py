from django.apps import AppConfig
from django.db import connection


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        from currency.models import Banks
        from currency import consts

        all_tables = connection.introspection.table_names()

        # check if table exists
        # table could be absent before initial migration
        # if Bank._meta.db_table in all_tables:
        if 'currency_banks' in all_tables:
            code_name = consts.CODE_NAME_PRIVATBANK
            privatbank_data = {
                'name': 'Privat',
                'url': 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
                'email_from': 'Privat@gmail.com',
                'number_phone': '+380993493543',
            }
            Banks.objects.update_or_create(code_name=code_name, defaults=privatbank_data)
