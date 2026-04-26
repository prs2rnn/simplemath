class SumCalculator:
    """A class providing the sum calculation methods."""

    @staticmethod
    def recursive(n: int) -> int:
        """Return the sum from 1 to n recursively."""
        if not isinstance(n, int):
            raise TypeError('Argument must be non negative integer')
        if n < 0:
            raise ValueError('Argument must be non-negative')
        if n <= 1:
            return n
        return n + SumCalculator.recursive(n - 1)
