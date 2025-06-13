from enum import Enum


class Color(str, Enum):
    RED = 'red'
    GREEN = 'green'


class Currency(str, Enum):
    USD = 'usd'
