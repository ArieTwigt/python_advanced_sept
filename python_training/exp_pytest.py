import pytest
from exp_decorators import calc_interest, calc_interest_inflated, calc_circle


# define our tests
def test_calc_interest():
    assert calc_interest(100, 5, 1) == 105

def test_calc_interest_inflated():
    assert round(calc_interest_inflated(1000, 5, 10), 3) == 1280.085

def test_calc_circle():
    assert calc_circle(10) == 78.53981633974483
    