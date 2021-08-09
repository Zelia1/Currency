from decimal import Decimal


def to_decimal(number: str) -> Decimal:
    return Decimal(number).quantize(Decimal('0.01'))


def valid_number(number):
    new_number = max([float(i) for i in number.replace(',', '.').split()])
    return new_number
