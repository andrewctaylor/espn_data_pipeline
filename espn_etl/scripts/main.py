from espn_etl.scripts.load_videos import load_insert_raw

def main():
    # Loads then inserts raw JSON into Snowflake DB
    load_insert_raw()



if __name__ == "__main__":
    main()