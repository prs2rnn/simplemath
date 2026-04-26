def is_prime(n: int) -> bool:
    """Check is a number prime."""
    if not isinstance(n, int):
        raise TypeError('n must be non negative integer')
    if n < 0:
        raise ValueError('n must be non negative integer')
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5), 2):
        if n % i == 0:
            return False
    return True
