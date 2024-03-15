import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    taxi_dtypes = {
        'VendorID' : pd.Int64Dtype(),
        'passenger_count' : pd.Int64Dtype(),
        'trip_distance' : float,
        'RatecodeID' : pd.Int64Dtype(),
        'store_and_fwd_flag' : str,
        'PULocationID' : pd.Int64Dtype(),
        'DOLocationID' : pd.Int64Dtype(),
        'payment_type' : pd.Int64Dtype(),
        'fare_amount' : float,
        'extra' : float,
        'mta_tax' : float,
        'tip_amount' : float,
        'tolls_amount' : float,
        'improvement_surcharge' : float,
        'total_amount' : float,
        'congestion_surcharge' : float
    }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    years = ['2019']
    
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    dfs = []  # Create an empty list to store DataFrames

    for year in years:
        for month in months:
            url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_{year}-{month}.csv.gz'
            df_chunk = pd.read_csv(url, sep=',', compression='gzip')
            print(f'year{year} month{month} added to dfs list')
            dfs.append(df_chunk)

    # Concatenate all DataFrames in the list
    df = pd.concat(dfs, ignore_index=True)

    print(df.head())

    print(df.dtypes)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
