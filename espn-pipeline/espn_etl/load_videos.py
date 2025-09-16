import json
import uuid
import requests
from espn_etl.snowflake_connect import connect_to_schema

sports_leagues = [
    ("basketball", "nba"),
    ("basketball", "mens-college-basketball"),
    ("football", "nfl"),
    ("football", "college-football"),
    ("baseball", "mlb"),
    ("hockey", "nhl"),
    ("soccer", "usa.1"), 
    ("mma", "ufc"),
    ("golf", "pga"),
    ("tennis", "atp")
]


def load_insert_raw(): 
    conn = connect_to_schema()
    cur = conn.cursor()
    cur.execute("SELECT CURRENT_ACCOUNT(), CURRENT_ROLE(), CURRENT_WAREHOUSE(), CURRENT_DATABASE(), CURRENT_SCHEMA()")
    print("ctx:", cur.fetchone())

    # Insert TABLE into Snowflake if not there
    cur.execute("""
            CREATE TABLE IF NOT EXISTS news_raw (
            id STRING DEFAULT UUID_STRING(),
            json_blob VARIANT,
            sport STRING,
            league STRING,
            created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP());
                    """)
    
    
    # Iterates over every sports/league combination
    rows = []
    for sport, league in sports_leagues:
        print("working on",sport,league)
        jsn = api_call(sport, league, "news")
        if jsn in (None, [], {}):
            continue
        rows.append((json.dumps(jsn), str(sport), str(league)))

    if not rows:
        print("Nothing to insert.")
    else:
        placeholders = ", ".join(["(%s, %s, %s)"] * len(rows)) # "json, sport, league"
        params = [item for row in rows for item in row]

        sql = f"""
            INSERT INTO news_raw (json_blob, sport, league)
            SELECT TRY_PARSE_JSON(v.js), v.sp, v.lg
            FROM (VALUES {placeholders}) AS v(js, sp, lg)
        """
        cur.execute(sql, params)
        conn.commit()

    cur.execute("SELECT * FROM news_raw")
    #print("fetch all -> ", cur.fetchall())

    cur.close()
    conn.close()


# API Call -> custom API Call
def api_call(sport,league,type):
    url = f"https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/{type}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"{sport}/{league} call successful")
        return data
    else:
        print(f"Request failed for {sport}/{league} with status: {response.status_code}") 
        

# API Call -> default json object of espn news
def fetch_articles():
    url = "http://now.core.api.espn.com/v1/sports/news"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()