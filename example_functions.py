# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

import pytest


def my_adder(a: float, b: float, c: float) -> float:
    """
    function to sum the 3 numbers
    Input: 3 numbers a, b, c
    Output: the sum of a, b, and c
    author:
    date:
    """

    # this is the summation
    out = a + b + c

    return out


# Testing my_adder
@pytest.mark.parametrize(
    "a, b , c, expected", [(1, 2, 3, 6), (1, 1, 1, 3), (5, 5, 5, 15)]
)
def test_my_adder(a, b, c, expected):
    assert my_adder(a, b, c) == expected


# -------------
def my_thermo_stat(temp: float, desired_temp: float) -> str:
    """
    Changes the status of the thermostat based on
    temperature and desired temperature
    author
    date
    :type temp: Int
    :type desiredTemp: Int
    :rtype: String
    """
    if temp < desired_temp - 5:
        status = "Heat"
    elif temp > desired_temp + 5:
        status = "AC"
    else:
        status = "off"
    return status


# Testing my_thermo_stat
@pytest.mark.parametrize(
    "temp, desired_temp, expected", [(20, 20, "off"), (30, 20, "AC")]
)
def test_my_thermo_stat(temp, desired_temp, expected):
    assert my_thermo_stat(temp, desired_temp) == expected


def have_digits(s: str) -> int:
    """
    Checks if a string has digits in it
    """

    out = 0

    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break

    return out


# testing have_digit
@pytest.mark.parametrize(
    "s, expected", [("01928326", 1), ("diet coke", 0), ("abc123", 1)]
)
def test_have_digits(s, expected):
    assert have_digits(s) == expected


def area_of_rectangle(width: float, height: float) -> float:
    area = width * height
    return area


@pytest.mark.parametrize("width,height,area", [(3, 5, 15), (2, 4, 8), (6, 9, 54)])
def test_area(width, height, area):
    output = area_of_rectangle(width, height)
    assert output == area

def perimeter_of_rectangle(width: float, height: float) -> float:
    perimeter = 2*(width+height)
    return perimeter 

@pytest.mark.parametrize("width,height,perimeter", [(3, 5, 16), (2, 4, 12), (6, 9, 30)])
def test_perimeter(width, height, perimeter):
    output = perimeter_of_rectangle(width,height)
    assert output == perimeter