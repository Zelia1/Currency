from unittest.mock import MagicMock

from currency import consts
from currency.models import Banks, Rate
from currency.tasks import parse_monobank


def test_parse_monobank(mocker):

    json_mock = lambda: [ # noqa
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1628284206, "rateBuy": 26.77, "rateSell": 26.9702},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1628284206, "rateBuy": 31.55, "rateSell": 31.9},
    ]

    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock)) # noqa

    code_name = consts.CODE_NAME_MONOBANK
    monobank_data = {
        'name': 'Monobank',
        'url': 'https://api.mono.ua/p24api/pubinfo?json&exchange&coursid=5',
        'email_from': 'Mono@gmail.com',
        'number_phone': '+380995693543',
    }
    Banks.objects.create(code_name=code_name, **monobank_data)

    initial_count = Rate.objects.count()
    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
