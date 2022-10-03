from api_functions.import_functions import get_cars_by_brand
from api_functions.conversion_functions import clean_dataframe

# get the cars from the API
my_cars_df = get_cars_by_brand("OPEL")

# clean the data frame
my_cars_cleaned_df = clean_dataframe(my_cars_df)

pass