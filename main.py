"""Small collection of testable utilities.

Run directly:
    python main.py
Run tests (requires pytest installed):
    python -m pytest
"""
from __future__ import annotations

from typing import Iterable


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def average(values: Iterable[float]) -> float:
    """Return the arithmetic mean of a non-empty iterable."""
    values_list = list(values)
    if not values_list:
        raise ValueError("values must not be empty")
    return sum(values_list) / len(values_list)


def is_palindrome(text: str) -> bool:
    """Check whether text reads the same forwards and backwards (case-insensitive)."""
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]


def factorial(n: int) -> int:
    """Compute n! for non-negative n using an iterative loop."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def _demo() -> None:
    print("add(2, 3)", add(2, 3))
    print("average([1, 2, 3])", average([1, 2, 3]))
    print("is_palindrome('Race car')", is_palindrome("Race car"))
    print("factorial(5)", factorial(5))


if __name__ == "__main__":
    _demo()
