from decimal import Decimal


def to_decimal(number: str) -> Decimal:
    return Decimal(number).quantize(Decimal('0.01'))


def valid_number(number):
    new_number = max([float(i) for i in number.replace(',', '.').split()])
    return new_number


def valid_parse_date(date):
    # valid_date = {
    #     'day': date.isoformat()[8:],
    #     'month': date.isoformat()[5:7],
    #     'year': date.isoformat()[:4]
    # }
    #
    # return valid_date
    return f'{date.isoformat()[8:]}.{date.isoformat()[5:7]}.{date.isoformat()[:4]}'
