
{{ config(materialized='view') }}
SELECT
    id AS payload_id, article.value AS article_object, sport, league, created_at
FROM {{ref("stg_news_raw")}},
LATERAL FLATTEN(input => json_blob:articles) AS article
