import pandas as pd 
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time
import argparse,os,sys

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # get the file from url
    file_name = url.rsplit('/',1)[-1].strip()
    print(f'Downloading {file_name} ...')
    # download file from url
    os.system(f'curl {url.strip()} -o {file_name}')
    print('\n')

    # Create SQL engine 
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')


    # Read file based on csv or parquet

    if '.csv' in file_name:
        df = pd.read_csv(file_name,nrows=10)
        df_iter = pd.read_csv(file_name,iterator=True,chunksize=100000)
    elif '.parquet' in file_name:
        file = pq.ParquetFile(file_name)
        df = next(file.iter_batches(batch_size=10)).to_pandas()
        df_iter= file.iter_batches(batch_size=100000)
    else:
        print("Only csv or parquet files allowed")
        sys.exit() 
    
    # create the taable 
    df.head(0).to_sql(name=table_name,con=engine,if_exists='replace')


    # insert values to the table 

    t_start = time()
    count = 0
    for batch in df_iter:
        count+=1

        if  '.parquet' in file_name:
            batch_df = batch.to_pandas()
        else:
            batch_df = batch
        print(f'insterting batch {count} ...')

        b_start = time()

        batch_df.to_sql(name=table_name,con=engine,if_exists="append")
        b_end=time()
        print(f"Inserted! Time taken {b_end-b_start:10.3f} seconds .\n")
    t_end=time()
    print(f"Completed!Total time taken was {t_end-t_start:10.3f} seconds for {count} batches.")

if __name__ == '__main__':
        # parsing arguments

        parser =  argparse.ArgumentParser(description="Ingest data to Postgres")

        parser.add_argument('--user',help="user name for postgres")
        parser.add_argument('--password',help="password for postgres")
        parser.add_argument('--host',help="host for postgres")
        parser.add_argument('--port',help="port for postgres")
        parser.add_argument('--db',help="database name for postgres")
        parser.add_argument('--table_name',help="name of table where we will write the results to")
        parser.add_argument('--url',help="url of the parquet  file ")

        args = parser.parse_args()
        main(args)

