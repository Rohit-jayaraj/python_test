import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(3, 5) == 8
    assert calc.add(-1, 1) == 0

def test_subtract():
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(10, 5) == 5

def test_multiply():
    assert calc.multiply(2, 3) == 6

def test_divide():
    assert calc.divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)

