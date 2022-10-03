import math
import requests

# Add a function, with type hinting
def calculate_circle(diameter: float) -> float:
    '''
    A function to calculate the size of a circle, given the diameter

    Parameters:
    * diameter 

    Returns:
    * Size of circle
    '''
    
    accepted_types = [int, float]

    if type(diameter) not in accepted_types:
        raise TypeError("The value should be an int or float")

    radius = diameter / 2
    size = radius ** 2 * math.pi

    return size


# create a function that sends a request to the RDW API
def get_cars_by_brand(brand: str) -> None:
    pass