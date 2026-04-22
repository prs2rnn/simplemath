import pytest
from src.simplemath import FibonacciCalculator

class TestFibonacciCalculator:
    def test_sequence_valid_input(self):
        expected = [0, 1, 1, 2, 3, 5]
        assert FibonacciCalculator.sequence(5) == expected

    def test_generator_first_values(self):
        gen = FibonacciCalculator.generator()
        first_values = [next(gen) for _ in range(8)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13]
        assert first_values == expected
