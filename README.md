## Data engineering: Taxi data 
- Downloading the data :
    - Data can be found [here](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
    - I downloaded the 2024 Jan yellow taxis data: `wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet`

### Creating a schema
    - How the schema,tables should look like according to DDl.
    - `print(pd.io.sql.get_schema(df_taxi,name='yellow_taxi_data'))`
### postgresql on docker 
- Run this to stop postgresql from running on port 5432 : `sudo systemctl stop postgresql`

- Run this to initialize a docker engine:
    ```
    docker run -it \
    -e POSTGRES_USER='root' \
    -e POSTGRES_PASSWORD='root' \
    -e POSTGRES_DB='ny_taxi' \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:latest

    ```
- Using `pgcli` run : `pgcli -h localhost -p 5432 -u root -d ny_taxi`