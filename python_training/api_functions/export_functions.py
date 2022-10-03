import pandas as pd
import os

def export_df(df: pd.DataFrame, brand="Unknown", folder_name="data") -> None:

    # specify the path
    file_name = f"export_{brand}.csv"

    # specify the full path
    file_folder_path = f"{folder_name}/{file_name}"

    # export the file
    print("Exporting")
    df.to_csv(file_folder_path, sep=";")
    print(f"Exported to {file_folder_path}")


def export_df_license(df: pd.DataFrame, license_plate, brand="Unknown") -> None:
    '''
    Function to export a DataFrame with the selected car by license

    Parameters:
    * license

    Returns
    * A csv-file in the filesystem
    
    
    '''


    # get the name of the brand
    brand = df['merk']
    brand_name = brand[0]
    brand_name_lower = brand_name.lower()
    
    # lowercase the license plate
    license_plate_lower = license_plate.lower().replace("-", "")
    
    # specify path
    folder_name = f"data/license/{brand_name}"

    # create the directory if it does not exist yet
    os.makedirs(folder_name, exist_ok=True)

    # specify the path
    file_name = f"export_{license_plate_lower}.csv"

    # combine folder and file path
    file_folder_path = f"{folder_name}/{file_name}"

    # export the name
    print("📄 Exporting")
    df.to_csv(file_folder_path, sep=";", index=False)
    print("Exported")

    pass