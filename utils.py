"""
Moduł utils zawiera podstawowe funkcje kalkulatora: dodawanie, odejmowanie,
mnożenie i dzielenie dwóch liczb całkowitych.
"""


def add(a: int, b: int) -> int:
    """Zwraca sumę dwóch liczb całkowitych a i b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Zwraca różnicę dwóch liczb całkowitych a i b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Zwraca iloczyn dwóch liczb całkowitych a i b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Zwraca iloraz dwóch liczb całkowitych a i b jako liczbę zmiennoprzecinkową."""
    return a / b

def to_binary(n: int) -> str:
    """
    Converts a natural number in range 0–100 to its binary representation.
    Raises ValueError for out-of-range numbers.
    Raises TypeError for non-integers or non-natural numbers.
    """
    if not isinstance(n, int):
        raise TypeError("Number must be a natural integer")
    if not 0 <= n <= 100:
        raise ValueError("Number out of allowed range")
    return bin(n)