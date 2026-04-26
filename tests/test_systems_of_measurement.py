import pytest
from src.simplemath import SystemsOfMeasurementCalculator


class TestDecimalToAny:

    def test_decimal_to_any_2(self):
        for i in range(100):
            assert SystemsOfMeasurementCalculator.decimal_to_any(i, 2) == bin(i)[
                2::]

    def test_decimal_to_any_8(self):
        for i in range(100):
            assert SystemsOfMeasurementCalculator.decimal_to_any(i, 8) == oct(i)[
                2::]

    def test_decimal_to_any_16(self):
        for i in range(100):
            assert SystemsOfMeasurementCalculator.decimal_to_any(i, 16) == hex(i)[
                2::].upper()

    def test_decimal_to_any_other_base(self):
        with pytest.raises(ValueError):
            SystemsOfMeasurementCalculator.decimal_to_any(1, 1)
            SystemsOfMeasurementCalculator.decimal_to_any(1, '1')

    def test_decimal_to_any_not_int_n_and_base(self):
        with pytest.raises(TypeError):
            SystemsOfMeasurementCalculator.decimal_to_any('1', 16)


class TestAnyToDecimal:

    def test_any_to_decimal_base_2(self):
        digits = (bin(i)[2::] for i in range(100))
        for digit in digits:
            assert int(digit, 2) == SystemsOfMeasurementCalculator.any_to_decimal(
                digit, 2)

    def test_any_to_decimal_base_8(self):
        digits = (oct(i)[2::] for i in range(100))
        for digit in digits:
            assert int(digit, 8) == SystemsOfMeasurementCalculator.any_to_decimal(
                digit, 8)

    def test_any_to_decimal_base_16(self):
        digits = (hex(i)[2::] for i in range(100))
        for digit in digits:
            assert int(digit, 16) == SystemsOfMeasurementCalculator.any_to_decimal(
                digit, 16)
