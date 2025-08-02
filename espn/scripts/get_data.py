from espn.backend.api import api_call

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import os
from dotenv import load_dotenv

# Loading environment
load_dotenv() # parse .env and loads all variables
DB_URL = os.getenv("DB_URL")

# Connect to Postgres / outdated
engine = create_engine(DB_URL)

metadata = MetaData()


