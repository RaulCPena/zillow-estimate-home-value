# Clean and prep script to be used on the Zillow project
import pandas as pd
import numpy as np


# drop nulls

def clean_data(df):
    # added formating options for floats
    pd.options.display.float_format = '{:.1f}'.format
    df = df.dropna()

    return df
