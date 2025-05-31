import re
from dataclasses import dataclass

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self):
        if not re.fullmatch(regex, self.value):
            raise ValueError('Incorrect email address')

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class MobileNumber:
    value: str

    def __post_init__(self):
        if len(self.value) != 11 or self.value[:2] != '09' or not self.value.isdigit():
            raise ValueError('Incorrect mobile number')

    def __str__(self):
        return self.value
