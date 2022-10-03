from api_functions.import_functions import get_car_by_license_plate
from api_functions.export_functions import export_df_license

selected_license_plate = "RD799K"

cars_df = get_car_by_license_plate(selected_license_plate)

export_df_license(cars_df, selected_license_plate)

pass