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

def to_binary(n):
    """Konwertuje liczbę naturalną (0-100) na binarną reprezentację jako string.
    Podnosi ValueError dla liczb spoza zakresu 0-100.
    Podnosi TypeError jeśli liczba nie jest całkowita.
    """
    if not isinstance(n, int):
        raise TypeError("Liczba musi być całkowita")
    if not (0 <= n <= 100):
        raise ValueError("Liczba musi być w zakresie 0-100")
    return bin(n)[2:]  # usuwa '0b' z początku
