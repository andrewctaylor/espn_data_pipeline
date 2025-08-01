import snowflake.connector

# warehouse -> database -> schema
def connect_to_schema():
    conn = snowflake.connector.connect(
        user="andrewctaylor",
        password="Ucberktwins41442845!",
        account="ggjmket-vqb12267", 
        warehouse="espn_wh",
        database="API_DATA_DB",
        schema="RAW"
    )
    return conn



