import pytest
from src.simplemath import SumCalculator


class TestSumCalculator:

    def test_sum_to_n_negative(self):
        with pytest.raises(ValueError) as e:
            SumCalculator.recursive(-1)
        assert 'Argument must be non-negative' in str(e.value)

    @pytest.mark.parametrize('n,expected', [
        (0, 0),
        (1, 1),
        (2, 3),
        (5, 15),
        (10, 55),
        (16, 136),
        (100, 5050),
    ])
    def test_sum_to_n_positive(self, n, expected):
        assert SumCalculator.recursive(n) == expected
