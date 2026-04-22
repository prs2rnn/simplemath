class FibonacciCalculator:
    """A class providing Fibonacci sequence calculation methods."""
    @staticmethod
    def sequence(n: int) -> list:
        """Return a Fibonacci sequence within n > 1."""

        if not isinstance(n, int):
            raise TypeError('Argument must be an integer')

        if n < 1:
            raise ValueError('n must be more than 1')

        digits = []

        for i in range(n + 1):
            if i <= 1:
                digits.append(i)
            else:
                fibonacci_digit = digits[i - 1] + digits[i - 2]
                digits.append(fibonacci_digit)

        return digits

    @staticmethod
    def generator():
        """Return a generator that yields Fibonacci numbers indefinitely."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
