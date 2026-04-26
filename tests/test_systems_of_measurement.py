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

    def test_decimal_to_any_to_decimal(self):
        assert SystemsOfMeasurementCalculator.decimal_to_any(123, 10) == '123'


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

    def test_any_to_decimal_incorrect_base(self):
        with pytest.raises(ValueError):
            SystemsOfMeasurementCalculator.any_to_decimal('A', 17)

    def test_any_to_decimal_incorrect_n(self):
        with pytest.raises(ValueError) as e:
            SystemsOfMeasurementCalculator.any_to_decimal('K', 16)
        assert "Invalid digit 'K' for base 16" in str(e.value)

    def test_any_to_decimal_incorrect_n_and_base(self):
        with pytest.raises(ValueError) as e:
            SystemsOfMeasurementCalculator.any_to_decimal('A', 8)
        assert "Digit 'A' is not valid in base 8" in str(e.value)


class TestConvertBase:

    @pytest.mark.parametrize('n,from_base,to_base,expected', [
        ('0', 2, 10, '0'),
        ('11001', 2, 16, '19'),
        ('A3', 16, 2, '10100011'),
    ])
    def test_convert_base(self, n, from_base, to_base, expected):
        assert SystemsOfMeasurementCalculator.convert_base(
            n, from_base, to_base) == expected
