def my_adder(a: float, b: float, c: float) -> float:
    """function to sum the 3 numbers

    Args:
        a: float
        b: float
        c: float

    Returns: 
        out: the total sum of the three numbers
    """

    out = a + b + c

    return out

def my_thermo_stat(temp: int, desired_temp: int) -> str:
    """ Changes the status of the thermostat based on
    temperature and desired temperature

    Args:
        temp: actual temperature
        desired_temp: temperature you'd like

    Returns:
        status: status of the thermostat
    """
    if temp < desired_temp - 5:
        status = "Heat"
    elif temp > desired_temp + 5:
        status = "AC"
    else:
        status = "off"
    return status


def have_digits(s: str) -> int:
    """Checks if a string has digits in it

    Args: 
        s: string

    Returns:
        out: 0 if it doesn't contain digits and 1 if it does
    """

    out = 0

    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break

    return out

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
