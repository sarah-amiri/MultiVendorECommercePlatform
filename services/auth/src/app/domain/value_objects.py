import re
from dataclasses import dataclass

# minimum eight characters, at least one number, at lease one letter
password_regex = "^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{8,}$"


@dataclass(frozen=True)
class Password:
    value: str

    def __post_init__(self):
        if not re.fullmatch(password_regex, self.value):
            raise ValueError(
                'password must contain minimum eight characters, '
                'at least one number and at least one number'
            )
