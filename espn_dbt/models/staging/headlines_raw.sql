
{{ config(materialized='view') }}
SELECT
    headline.value AS headline_object
FROM {{ref("base_news_data")}},
LATERAL FLATTEN(input => json_blob:headlines) AS headline
