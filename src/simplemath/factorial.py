class FactorialCalculator:
    """A class providing factorial calculation methods."""

    @staticmethod
    def iterative(n: int) -> int:
        """Calculate the factorial of a non-negative integer."""

        if not isinstance(n, int):
            raise TypeError('Argument must be an integer')

        if n < 0:
            raise ValueError('Argument must be non-negative')

        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def recursive(n: int) -> int:
        """Implementation of a factorial function via recursion"""
        if not isinstance(n, int):
            raise TypeError('Argument must be an integer')
        if n < 0:
            raise ValueError('n must be non-negative integer')
        if n <= 1:
            return 1
        return n * FactorialCalculator.recursive(n - 1)
