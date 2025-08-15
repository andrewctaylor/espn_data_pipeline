{{ config(materialized='table') }}

WITH src AS (
    SELECT
        article_object:id::INT AS article_id,
        article_object:links  AS links
    FROM {{ ref('articles_raw') }}
    WHERE article_object:id IS NOT NULL
),

links_cte AS(
    SELECT
        article_id,
        links:api:self:href::STRING as api,
        links:app:sportscenter:href::STRING as app,
        links:mobile:href::STRING as mobile,
        links:web:self:href::STRING as web
    FROM src
)

SELECT DISTINCT * FROM links_cte 