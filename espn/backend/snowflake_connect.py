import snowflake.connector
import os

# warehouse -> database -> schema
def connect_to_schema():
    conn = snowflake.connector.connect(
        user = os.getenv("SNOWFLAKE_USER"),
        password = os.getenv("SNOWFLAKE_PASS"),
        account = os.getenv("SNOWFLAKE_ACC"),
        warehouse="espn_wh",
        database="API_DATA_DB",
        schema="RAW"
    )
    return conn



