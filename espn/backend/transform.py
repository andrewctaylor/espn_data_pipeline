import requests
import pandas as pd


def extract_videos(jsn):
    """
    Filters json object with pandas and returns final cleaned video table
    - jsn: JSON object to 
    """
    articles = pd.json_normalize(jsn['headlines']) # Use later for articles
    videos = articles[['id', 'video']].explode('video')
    video_df = pd.json_normalize(videos["video"], sep="_")
    video_df["article_id"] = videos["id"].values

    keep_cols = [
        'id','article_id','headline','caption','duration','premium',
        'lastModified','originalPublishDate','syndicatable',
        'keywords','ad_sport','ad_bundle','source'
    ]
    video_df = video_df[keep_cols]
    video_df = video_df[~video_df['id'].isna()] # remove rows where there's nothing

    return video_df