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
- Using `pgcli` run : `pgcli -h localhost -p 5432 -U root -d ny_taxi`

- For convinience it is paramount to use pgAmin for controlling/exploring our data. Run the following to use pgAdmin
```
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4

```

### Running PgAdmin and postgres together
- A same network for the pgadmin and docker is important to avoid errors.run the following.

- Create a network :

`docker network create pg-network`
- Run postgres:

```
 docker run -it \
    -e POSTGRES_USER='root' \
    -e POSTGRES_PASSWORD='root' \
    -e POSTGRES_DB='ny_taxi' \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:latest
```

- Run pgAdmin :

```
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgadmin \
    dpage/pgadmin4

```
- After the above check `localhost:8080` for the pgAmin GUI.

- After coming back you can restart the containers by :`docker start pg-database` and `docker start pgadmin`

-- In case you havee a notebook you can convert it usiing `jupyter --to=script read_data.py`

### Data ingestion

- Running the script locally:

```
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
python read_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="${URL}"
```

### Running the script on docker 
- Build the docker image
```
docker build -t taxi_ingestion:v001 .

```

- Run docker container  

```
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
docker run -it \
    --network=pg-network \
    taxi_ingestion:v001 \
        --user=root \
        --password=root \
        --host=pg-database \
        --port=5432 \
        --db=ny_taxi \
        --table_name=yellow_taxi_trips \
        --url="${URL}"
```
- note ; Make sure the pg-database is up and running 

### Docker compose 
- This is usefull to manage multiple container, making it easier to manage multiple container configurations and dependencies.
- Check the script for more information.

- To stop docker compose :
`docker-compose down`

to start it :
`docker-compose up -d `

## Homework 
#### Question 1 :
- Run docker with the python:3.12.8 image in an interactive mode, use the entrypoint bash.What's the version of pip in the image?
    ```
    docker run -it --entrypoint bash python:3.12.8

    pip --version

    ```