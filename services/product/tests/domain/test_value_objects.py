import pytest
from src.app.domain import Price


class TestPrice:
    def test_valid_price(self):
        price = Price(value=100)
        assert price.value == 100

    def test_null_price_raises_error(self):
        with pytest.raises(ValueError):
            _ = Price(value=None)

    def test_zero_is_valid(self):
        price = Price(value=0)
        assert price.value == 0

    def test_negative_value_raises_error(self):
        with pytest.raises(ValueError):
            _ = Price(value=-100)

    def test_price_value_is_immutable(self):
        price = Price(value=100)
        with pytest.raises(AttributeError):
            price.value = 200
