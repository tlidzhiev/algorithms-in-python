import pytest
from main import is_palindrome


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, True),
        (1, True),
        (7, True),
        (11, True),
        (22, True),
        (121, True),
        (12321, True),
        (1221, True),
        (10, False),
        (100, False),
        (12, False),
        (1231, False),
        (-121, False),
    ],
)
def test_various(n, expected):
    assert is_palindrome(n) == expected


def test_large_palindrome():
    assert is_palindrome(1234567890987654321) is True


def test_large_non_palindrome():
    assert is_palindrome(1234567890123456789) is False
