import snowflake.connector
import os
from dotenv import load_dotenv

# Returns connection object to snowflake db
def connect_to_schema():

    conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASS"),
    account="wbb71043.us-west-2",   # <-- from CURRENT_ACCOUNT + CURRENT_REGION
    warehouse="espn_wh",
    database="API_DATA_DB",
    schema="RAW_JSON",
)


    return conn



