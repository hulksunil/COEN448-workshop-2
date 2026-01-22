"""Simple pytest cases for main.py."""
import pytest

from main import add, average, factorial, is_palindrome


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1.5) == 0.5


def test_average():
    assert average([1, 2, 3, 4]) == 2.5
    assert average((10, 0)) == 5
    with pytest.raises(ValueError):
        average([])


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("Race car")
    assert not is_palindrome("hello")


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
