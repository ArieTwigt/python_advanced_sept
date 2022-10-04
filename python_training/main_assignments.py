from api_functions.import_functions import get_car_by_license_plate
from api_functions.export_functions import export_df_license, export_to_db

selected_license_plate = "rd-799-k"

# get the data frame from the api
cars_df = get_car_by_license_plate(selected_license_plate)

# export to csv
export_df_license(cars_df, selected_license_plate)

# export to database
export_to_db(cars_df)

pass