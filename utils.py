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
