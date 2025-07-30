from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, MetaData
from sqlalchemy.dialects.postgresql import ARRAY 
import os
from dotenv import load_dotenv

# Loading environment
load_dotenv() # parse .env and loads all variables
DB_URL = os.getenv("DB_URL") # Gets url from my env

# Connect to Postgres
engine = create_engine(DB_URL)
metadata = MetaData()



def insert_dataframe(df, table_name):
    """
    Inserts pandas DataFrame into specified postgres table.
    - df: DataFrame to insert
    - table_name: Name of the table in Postgres
    """
    df.to_sql(table_name, engine, if_exists='append', index=False) # pandas df -> SQL table -> insert into postgres
    print(f"Yay! You inserted {len(df)} rows into {table_name}")



# Create events table
events_table = Table(
    'events',
    metadata,
    Column('id', String, primary_key=True),
    Column('name', String, nullable=False),
    Column('date', String, nullable=False)
)

# Create videos table
videos_table = Table(
    'videos',
    metadata,
    Column('id', String, primary_key=True),
    Column('article_id', String),
    Column('headline', String),
    Column('caption', String),
    Column('duration', Integer),
    Column('premium', Boolean),
    Column('lastModified', String),
    Column('originalPublishDate', String),
    Column('syndicatable', Boolean),
    Column('keywords', ARRAY(String)),
    Column('ad_sport', String),
    Column('ad_bundle', String),
    Column('source', String),
)

#creates table
metadata.create_all(engine)

print("events  table created successfully in espn_db")