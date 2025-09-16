from .load_videos import load_insert_raw

if __name__ == "__main__":
    # Loads then inserts raw JSON into Snowflake DB (One batch insertion)
    print("[main] imported")
    load_insert_raw()
    print("[main] done")