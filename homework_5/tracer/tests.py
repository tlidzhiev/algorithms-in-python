from main import tracer


@tracer
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


@tracer
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@tracer
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def test_factorial_result():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6


def test_fibonacci_result():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(4) == 3
    assert fibonacci(6) == 8


def test_gcd_result():
    assert gcd(48, 18) == 6
    assert gcd(100, 50) == 50
    assert gcd(17, 13) == 1
