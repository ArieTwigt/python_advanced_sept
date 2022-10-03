from api_functions.import_functions import get_cars_by_brand
from api_functions.conversion_functions import clean_dataframe
from api_functions.export_functions import export_df

# assign the brand
selected_brand = input("Specify the brand you like to import:\n")

# get the cars from the API
my_cars_df = get_cars_by_brand(selected_brand)

# clean the data frame
my_cars_cleaned_df = clean_dataframe(my_cars_df)

# export the data frame
export_df(my_cars_cleaned_df, selected_brand)

pass