from espn.backend.api import fetch_articles
from espn.backend.transform import extract_videos
from espn.backend.make_tables import insert_dataframe

def load_videos(): 
    jsn = fetch_articles()
    video_df = extract_videos(jsn)
    insert_dataframe(video_df, "videos")