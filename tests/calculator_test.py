"""Testing the Calculator"""

from calculator import main


def test_add():
    """ Testing the Add function of the calculator """
    result = main.add(4, 2)
    assert result == 6


def test_subtract():
    """ Testing the subtract function of the calculator """
    result = main.subtract(4, 2)
    assert result == 2


def test_multiply():
    """ Testing the multiply function of the calculator """
    result = main.multiply(4, 2)
    assert result == 8


def test_divide():
    """ Testing the divide function of the calculator """
    result = main.divide(4, 2)
    assert result == 2


def test_divide_by_zero_does_not_give_error():
    """ Testing divide by zero does not give an exception """
    result = main.divide(4, 0)
    assert not isinstance(result, Exception)
