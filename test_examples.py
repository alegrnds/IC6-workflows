# Tests from https://www.softwaretestinghelp.com/pytest-tutorial/
import pytest

def area_of_rectangle(width: float, height: float) -> float:
    """Calculates the area of a rectangle

    Args:
        width: width of the rectangle
        height: height of the rectangle

    Returns:
        area: area of the rectangle
    
    """
    area = width * height
    return area

def perimeter_of_rectangle(width: float, height: float) -> float:
    """Calculates the perimeter of a rectangle

    Args: 
        width: width of the rectangle
        height: height of the rectangle

    Returns: 
        perimeter: perimeter of the rectangle
    """
    perimeter = 2*(width+height)
    return perimeter 

@pytest.mark.parametrize("width,height,area", [(3, 5, 15), (2, 4, 8), (6, 9, 54)])
def test_area(width, height, area):
    output = area_of_rectangle(width, height)
    assert output == area

@pytest.mark.parametrize("width,height,perimeter", [(3, 5, 16), (2, 4, 12), (6, 9, 30)])
def test_perimeter(width, height, perimeter):
    output = perimeter_of_rectangle(width,height)
    assert output == perimeter
    
