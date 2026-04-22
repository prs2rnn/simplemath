import pytest
from src.simplemath.calculator import *


class TestFactorial:

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120
        assert factorial(3) == 6

    def test_factorial_large_number(self):
        assert factorial(10) == 3628800

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_large_non_integer(self):
        with pytest.raises(TypeError):
            factorial(3.5)
            factorial("5")


class TestRecursiveFactorial:

    def test_recursive_factorial_n_0(self):
        assert recursive_factorial(0) == 1

    def test_recursive_factorial_n_1(self):
        assert recursive_factorial(1) == 1

    def test_recursive_factorial_large_number(self):
        assert recursive_factorial(10) == 3628800

    def test_recursive_factorial_negative(self):
        with pytest.raises(ValueError):
            recursive_factorial(-1)

    def test_recursive_factorial_large_non_integer(self):
        with pytest.raises(TypeError):
            recursive_factorial("5")
            recursive_factorial(3.5)


class TestFibonacci:

    def test_fibonacci_less_than_one(self):
        with pytest.raises(ValueError) as excinfo:
            fibonacci(1)
            fibonacci(0)
            fibonacci(-1)
        assert 'n must be more than 1' in str(excinfo.value)

    def test_fibonacci_non_integer(self):
        with pytest.raises(TypeError):
            fibonacci('1')
            fibonacci(0.5)

    def test_fibonacci_n_10(self):
        result = fibonacci(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        assert result == expected


class TestFibonacciGenerator:

    def test_first_few_values(self):
        gen = fibonacci_generator()
        assert next(gen) == 0
        assert next(gen) == 1
        assert next(gen) == 1
        assert next(gen) == 2
        assert next(gen) == 3

    def test_generate_n_numbers(self):
        gen = fibonacci_generator()
        result = []

        for i, value in enumerate(gen):
            if i >= 8:
                break
            result.append(value)
        expected = [0, 1, 1, 2, 3, 5, 8, 13]
        assert result == expected
