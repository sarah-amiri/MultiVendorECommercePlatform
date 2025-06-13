from dataclasses import dataclass


@dataclass(frozen=True)
class Price:
    value: int

    def __post_init__(self):
        if self.value is None:
            raise ValueError('price cannot be null')
        if self.value < 0:
            raise ValueError('price value cannot be zero')
