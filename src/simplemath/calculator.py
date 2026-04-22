def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""

    if not isinstance(n, int):
        raise TypeError('Argument must be an integer')

    if n < 0:
        raise ValueError('Argument must be non-negative')

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def recursive_factorial(n: int) -> int:
    """Implementation of a factorial function via recursion"""
    if not isinstance(n, int):
        raise TypeError('Argument must be an integer')
    if n < 0:
        raise ValueError('n must be non-negative integer')
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)


def fibonacci(n: int) -> list:
    """Return a Fibonacci list within n > 1."""

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


def fibonacci_generator():
    """Return a generator that yields Fibonacci numbers indefinitely."""
    digits = []
    count = 0
    while True:
        if count > 1:
            fibonacci_digit = digits[count - 1] + digits[count - 2]
            digits.append(fibonacci_digit)
        else:
            digits.append(count)
        yield digits[count]
        count += 1
