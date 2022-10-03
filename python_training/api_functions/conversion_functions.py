import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    ''' 
    Function to clean and convert the DataFrame

    Parameters:
    * df

    Returns
    * DataFrame
    '''

    # conversion of the column
    df['catalogusprijs'] = df['catalogusprijs'].astype(float)

    # fill the 'NaN' values with 0
    df['catalogusprijs'] = df['catalogusprijs'].fillna(0)

    return df