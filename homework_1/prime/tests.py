import pytest
from main import count_primes


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),  # {2}
        (4, 2),  # {2,3}
        (5, 2),  # {2,3}
        (6, 3),  # {2,3,5}
        (7, 3),  # {2, 3, 5}
    ],
)
def test_small_values(n, expected):
    assert count_primes(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (7, 3),  # <7: {2,3,5}
        (10, 4),  # {2,3,5,7}
        (11, 4),  # <11: {2,3,5,7}
        (12, 5),  # +11
        (20, 8),
        (30, 10),
        (49, 15),
        (50, 15),
        (100, 25),
        (1000, 168),
        (10000, 1229),
    ],
)
def test_known_pi_values(n, expected):
    assert count_primes(n) == expected


def test_returns_int_type():
    res = count_primes(123)
    assert isinstance(res, int) and res >= 0
