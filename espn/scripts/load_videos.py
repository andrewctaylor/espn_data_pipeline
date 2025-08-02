import json
import uuid
from espn.backend.api import fetch_articles
from espn.backend.snowflake_connect import connect_to_schema

def load_raw_data(loc='postgres'): 
    jsn = fetch_articles()
    if loc == 'snowflake':
        conn = connect_to_schema()
        cur = conn.cursor()
        # Insert into Snowflake
        cur.execute("""
            CREATE TABLE IF NOT EXISTS news_raw (
                id STRING,
                json_blob VARIANT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                    """)
        

        new_id = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO news_raw (id, json_blob)
            SELECT %s, PARSE_JSON(%s)
            """, (new_id, json.dumps(jsn))
            )
        conn.commit()
        

        cur.execute("SELECT * FROM news_raw")
        print(cur.fetchall())

        cur.close()
        conn.close()