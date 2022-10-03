import math
import requests
import pandas as pd

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
def get_cars_by_brand(brand: str) -> pd.DataFrame:
    '''
    Returns a DataFrame of cars by the brand specified


    Parameters:
    * brand

    Return
    * pandas.DataFrame
    
    '''
    
    # compose the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"

    # execute the API request
    response = requests.get(endpoint)
    
    # verify the request was succesful
    if response.status_code != 200:
        raise ValueError("No data for this endpoint")
        return None

    # get the contents from the response
    cars_list = response.json()

    # create a pandas DataFrame from the list
    cars_df = pd.DataFrame(cars_list)

    return cars_df



# object
# str
# dict
# DataFrame
# response
# 
# Object:
# - methods
# - attributes
#     my_name = "Arie"
#    my_name.upper() # calling, it is callable