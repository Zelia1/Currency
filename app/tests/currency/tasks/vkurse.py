from unittest.mock import MagicMock

from currency import consts
from currency.models import Banks, Rate
from currency.tasks import parse_vkurse


def test_parse_vkurse(mocker):

    json_mock = lambda: { # noqa
        "Dollar": {"buy": "26.85", "sale": "27.00"},
        "Euro": {"buy": "31.60", "sale": "31.65"},
        "Rub": {"buy": "0.363", "sale": "0.367"}
    }

    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock)) # noqa

    code_name = consts.CODE_NAME_VKURSE
    vkurse_data = {
        'name': 'Vkurse',
        'url': 'https://api.vkurse.ua/p24api/pubinfo?json&exchange&coursid=5',
        'email_from': 'Vkurse@gmail.com',
        'number_phone': '+380995473543',
    }
    Banks.objects.create(code_name=code_name, **vkurse_data)

    initial_count = Rate.objects.count()
    parse_vkurse()
    assert Rate.objects.count() == initial_count + 2
