import pytest
from utils import to_binary


# Test poprawnej konwersji
@pytest.mark.parametrize(
    "num, expected",
    [
        (0, "0b0"),
        (1, "0b1"),
        (2, "0b10"),
        (100, "0b1100100"),
    ],
)
def test_valid_conversion(num, expected):
    assert to_binary(num) == expected


# Test liczby poza zakresem
@pytest.mark.parametrize("num", [-1, 101, 999])
def test_out_of_range(num):
    with pytest.raises(ValueError, match="Number out of allowed range"):
        to_binary(num)


# Test liczby nienaturalnej
@pytest.mark.parametrize("num", [1.5, 2.7, "10", None])
def test_invalid_type(num):
    with pytest.raises(TypeError, match="Number must be a natural integer"):
        to_binary(num)
