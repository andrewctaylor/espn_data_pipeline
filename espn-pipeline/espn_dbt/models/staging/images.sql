{{ config(materialized='table') }}

WITH src AS (
    SELECT
        article_object:id::INT AS article_id,
        article_object:images  AS images,
        created_at
    FROM {{ ref('articles_raw') }}
    WHERE article_object:id IS NOT NULL
),

images_cte AS (
    SELECT
        images[0]:id::STRING as image_id,
        article_id,
        images[0]:alt::STRING as alt,
        images[0]:caption::STRING as caption,
        images[0]:credit::STRING as credit,
        images[0]:height::INT as height,
        images[0]:dataSourceIdentifier::STRING as imagedataSourceIdentifier,
        images[0]:name::STRING as name,
        images[0]:type::STRING as type,
        images[0]:url::STRING as url,
        images[0]:width::INT as width,
        created_at
    FROM src
)

SELECT DISTINCT * FROM images_cte