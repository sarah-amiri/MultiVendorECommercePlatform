from dataclasses import dataclass


@dataclass(frozen=True)
class Price:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError('price value cannot be zero')
