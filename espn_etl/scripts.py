from espn_etl.backend.api_calls import fetch_articles
from espn_etl.scripts.transform import extract_videos
from espn_etl.backend.make_tables import insert_dataframe

jsn = fetch_articles()
video_df = extract_videos(jsn)
insert_dataframe(video_df, "videos")