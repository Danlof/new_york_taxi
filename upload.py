import pandas as pd 
from sqlalchemy import create_engine


def upload_zones():

    df_zones = pd.read_csv("./datasets/taxi_zone_lookup.csv")
    print(df_zones.head())

    # upload to sql 
    engine = create_engine(f'postgresql://root:root@localhost:5432/ny_taxi')
    df_zones.to_sql(name="zones",con=engine,if_exists="replace")
upload_zones()