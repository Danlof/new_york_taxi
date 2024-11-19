import pandas as pd 
import pyarrow.parquet as pq
from sqlalchemy import create_engine

table = pq.read_table("./datasets/yellow_tripdata_2024-01.parquet")

# find number of row 
num_rows = table.num_rows
print(num_rows)

# using pandas dataframe 

df_taxi = table.to_pandas()

print(df_taxi.head())

# to convert to csv to view afew things 
# df_100 = df_taxi.head(100)
# df_100.to_csv("datasets/df_taxi_100.csv")

# sql engine 
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# creating a schema 
print(pd.io.sql.get_schema(df_taxi,name='yellow_taxi_data',con=engine))