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
    base_url ='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green'
    months=['2020-10', '2020-11', '2020-12']
    results=[]

    for month in months:
        url = f"{base_url}/green_tripdata_{month}.csv.gz"
        # print(url)
        response = requests.get(url,stream=True)

        if response.status_code == 200:
            try:
                parse_dates = ['lpep_pickup_datetime','lpep_dropoff_datetime']  
                df = pd.read_csv(io.BytesIO(response.content),compression='gzip',parse_dates=parse_dates)
                print(f"{month}: {df.shape}")
                results.append(df)
            except Exception as e:
                print(f"error reading {month}:{e}")
        else:
            print(f"Request failed for {month} - Status code:{ response.status_code}")
    
    
    return pd.concat(results,ignore_index=True)



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
