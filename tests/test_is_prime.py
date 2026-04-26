import pytest
from src.simplemath import is_prime


class TestIsPrime:

    @pytest.mark.parametrize('n,expected', [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (10, False),
        (5, True),
        (133, False),
    ])
    def test_is_prime(self, n, expected):
        assert is_prime(n) == expected

    def test_is_prime_negative(self):
        with pytest.raises(ValueError):
            is_prime(-1)
