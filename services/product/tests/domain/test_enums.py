from src.app.domain import Color


class TestColor:
    def test_color_values(self):
        assert Color.RED == 'red'
        assert Color.GREEN == 'green'
        assert isinstance(Color.RED, str)
        assert isinstance(Color.GREEN, str)
