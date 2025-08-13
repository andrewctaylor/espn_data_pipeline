
{{ config(materialized='view') }}
SELECT
    id AS article_id, article.value AS article_object, sport, league
FROM {{ref("stg_news_raw")}},
LATERAL FLATTEN(input => json_blob:articles) AS article
