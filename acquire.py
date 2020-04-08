import pandas as pd
import numpy as np
from env import host, user, password

# function to get url

def get_db_url(db_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

# function that passes my query and my url to return df
def get_zillow_data_from_sql():
    query = '''
    SELECT
    bathroomcnt AS bathrooms,
    bedroomcnt AS bedrooms,
    calculatedfinishedsquarefeet AS square_feet,
    fips AS fips_number,
    ptype.propertylandusetypeid,
    ptype.propertylandusedesc,
    taxvaluedollarcnt AS home_value,
    taxamount AS tax_amount
    FROM properties_2017 AS prop
        JOIN
        predictions_2017 AS pred
        ON prop.parcelid = pred.parcelid
        JOIN
        propertylandusetype AS ptype
        ON prop.propertylandusetypeid = ptype.propertylandusetypeid

    WHERE transactiondate
    BETWEEN '2017-05-01' AND '2017-06-30' AND propertylandusedesc = 'Single Family Residential'
    '''
    df = pd.read_sql(query, get_db_url('zillow'))
    return df
