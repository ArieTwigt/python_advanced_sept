import math

# Add a function, with type hinting
def calculate_circle(diameter: float) -> float:
    '''
    A function to calculate the size of a circle, given the diameter

    Parameters:
    * diameter 

    Returns:
    * Size of circle
    '''

    radius = diameter / 2
    size = radius ** 2 * math.pi

    return size