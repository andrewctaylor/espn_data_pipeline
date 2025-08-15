import snowflake.connector
import os
from dotenv import load_dotenv

# Returns connection object to snowflake db
def connect_to_schema():
    load_dotenv()
    conn = snowflake.connector.connect(
        user = os.getenv("SNOWFLAKE_USER"),
        password = os.getenv("SNOWFLAKE_PASS"),
        account = os.getenv("SNOWFLAKE_ACC"),
        warehouse="espn_wh",
        database="API_DATA_DB",
        schema="RAW_JSON"
    )
    return conn



