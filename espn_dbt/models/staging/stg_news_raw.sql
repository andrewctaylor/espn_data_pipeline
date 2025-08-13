{{ config(materialized='view') }}

SELECT
    id,
    json_blob,
    sport,
    league,
    created_at
FROM RAW_JSON.NEWS_RAW
