{{ config(materialized='view') }}

SELECT
    id,
    json_blob,
    created_at
FROM RAW.NEWS_RAW
