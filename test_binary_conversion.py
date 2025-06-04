import pytest
from utils import to_binary


def test_to_binary_valid():
    assert to_binary(0) == "0"
    assert to_binary(1) == "1"
    assert to_binary(5) == "101"
    assert to_binary(100) == "1100100"


@pytest.mark.parametrize("value", [-1, 101, 150])
def test_to_binary_out_of_range(value):
    with pytest.raises(ValueError):
        to_binary(value)


@pytest.mark.parametrize("value", [1.5, 2.7, -3.1])
def test_to_binary_not_integer(value):
    with pytest.raises(TypeError):
        to_binary(value)
