import pandas as pd

def export_df(df: pd.DataFrame, brand="Unknown", folder_name="data") -> None:

    # specify the path
    file_name = f"export_{brand}.csv"

    # specify the full path
    file_folder_path = f"{folder_name}/{file_name}"

    # export the file
    print("Exporting")
    df.to_csv(file_folder_path, sep=";", index=False)
    print(f"Exported to {file_folder_path}")