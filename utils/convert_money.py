import locale
from typing import Union


def convert_money(money: Union[float, int]) -> str:
    """Returns money converted into dollar"""
    locale.setlocale(locale.LC_ALL, "en_US.UTF8")
    formatted_money = locale.currency(money, grouping=True)
    return formatted_money
