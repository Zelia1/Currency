from unittest.mock import MagicMock

from currency.tasks import parse_privatbank
from currency.models import Banks, Rate
from currency import consts


def test_parse_privatbank(mocker):
    # Rate.objects.all().delete()

    json_mock = lambda: [
        {"ccy": "USD", "base_ccy": "UAH", "buy": "26.80000", "sale": "27.20000"},
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "31.45000", "sale": "32.05000"},
        {"ccy": "RUR", "base_ccy": "UAH", "buy": "0.35500", "sale": "0.38500"},
        {"ccy": "BTC", "base_ccy": "USD", "buy": "37737.8981", "sale": "41710.3085"}
    ]
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))


    code_name = consts.CODE_NAME_PRIVATBANK
    privatbank_data = {
        'name': 'Privat',
        'url': 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
        'email_from': 'Privat@gmail.com',
        'number_phone': '+380993493543',
    }
    Banks.objects.create(code_name=code_name, **privatbank_data)

    initial_count = Rate.objects.count()
    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2
