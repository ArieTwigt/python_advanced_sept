import argparse
from api_functions.import_functions import get_cars_by_brand

# define a argument parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument('--brand', type=str, required=True)
parser.add_argument('--max_cars', type=int, required=False)

# parse the arguments
args = parser.parse_args()


# Specify to only run the code if it is the "main"
if __name__ == '__main__':
    print(__name__ )
    # access the args object
    selected_brand = args.brand
    max_cars = args.max_cars
    
    # get the cars by the specific brand
    if max_cars is not None:
        cars_df = get_cars_by_brand(selected_brand, max_cars)
    else:
        cars_df = get_cars_by_brand(selected_brand)
    
    # print the data frame
    print(cars_df)
