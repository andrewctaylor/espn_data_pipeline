import snowflake.connector
import os
from dotenv import load_dotenv, find_dotenv

# Returns connection object to snowflake db
load_dotenv(find_dotenv(), override=True)


def connect_to_schema():
    print("using account:", os.getenv("SNOWFLAKE_ACC"))
    print("using PAT token for authentication")
    return snowflake.connector.connect(
        user="AIRFLOW_ESPN_NAMED",
        password=os.getenv("SNOWFLAKE_PAT_TOKEN"),
        account="ggjmket-vqb12267",
        warehouse="ESPN_WH",
        database="API_DATA_DB",
        schema="RAW_JSON",
        login_timeout=15,
        network_timeout=20,
        ocsp_fail_open=True,
    )



