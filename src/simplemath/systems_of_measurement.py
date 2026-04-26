class SystemsOfMeasurementCalculator:
    """A class providing calculations from one system of measurement to another."""

    @staticmethod
    def decimal_to_any(n: int, base: int) -> str:
        """Convert decimal to binary, octal or hexadecimal."""
        if base not in (2, 8, 16):
            raise ValueError('base must be one of the 2, 8, 16 integer')
        if not isinstance(n, int):
            raise TypeError('n must be non-negative integer')

        digits = '0123456789ABCDEF'
        result = ''

        if n == 0:
            return '0'

        while n > 0:
            result += digits[n % base]
            n = n // base

        return ''.join(result)[::-1]

    @staticmethod
    def any_to_decimal(n: str, base: int) -> int:
        """Convert binary, octal or hexadecimal number to decimal base."""
        if base not in (2, 8, 16):
            raise ValueError('base must be one of the 2, 8, 16 integer')
        if not isinstance(n, str):
            raise TypeError('n must be a string')

        digits = '0123456789ABCDEF'
        n = n.upper()
        result = 0
        power = 0

        for digit in reversed(n):
            if digit not in digits:
                raise ValueError(f"Invalid digit '{digit}' for base {base}")
            value = digits.index(digit)
            if value >= base:
                raise ValueError(
                    f"Digit '{digit}' is not valid in base {base}")
            result += value * (base ** power)
            power += 1

        return result
