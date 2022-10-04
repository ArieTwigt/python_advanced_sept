from email.iterators import body_line_iterator
import math
from urllib import request
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
def get_cars_by_brand(brand: str, max_cars: int=5, color: str=None) -> pd.DataFrame:
    '''
    Returns a DataFrame of cars by the brand specified


    Parameters:
    * brand

    Return
    * pandas.DataFrame
    
    '''
    
    # upper the brand name
    brand_name_upper = brand.upper()

    # compose the endpoint
    if color != None:
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_name_upper}&eerste_kleur={color}"
    else: 
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_name_upper}"

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

    # limit the amount of cars
    cars_df_max = cars_df.head(max_cars)
     
    return cars_df_max


def get_car_by_license_plate(plate: str, as_dict: body_line_iterator=False) -> pd.DataFrame:
    '''
    Function to get a car by its license plate

    Parameters:
    * plate

    Returns
    * df with the single car
    
    '''

    # uppercase the letters and remove the "-"
    plate_upper = plate.upper().replace("-", "")
    
    # specify the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate_upper}"

    # execute the api request
    response = requests.get(endpoint)

    # conditional statement for the response
    if response.status_code != 200:
        print(f"Something went wrong with the request")
        print(f"{response.status_code}")
    

    # get the content of the response
    cars_list = response.json()

    # if the list is empty
    if len(cars_list) != 1:
        print(f"No car found for license plate: {plate}")

    # return the dictionary that is more suitable for web pages
    if as_dict:
        return cars_list


    # convert the car to a Data Frame
    cars_df = pd.DataFrame(cars_list)

    return cars_df


if __name__ == "__main__":
    print("This function is now the main")


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