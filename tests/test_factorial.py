import pytest
from src.simplemath import FactorialCalculator

class TestFactorialCalculator:
    def test_iterative_factorial_zero(self):
        assert FactorialCalculator.iterative(0) == 1

    def test_iterative_factorial_one(self):
        assert FactorialCalculator.iterative(1) == 1

    def test_iterative_factorial_positive(self):
        assert FactorialCalculator.iterative(5) == 120

    def test_recursive_factorial_positive(self):
        assert FactorialCalculator.recursive(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError) as excinfo:
            FactorialCalculator.iterative(-1)
        assert 'Argument must be non-negative' in str(excinfo.value)

    def test_factorial_non_integer(self):
        with pytest.raises(TypeError):
            FactorialCalculator.iterative(3.5)
