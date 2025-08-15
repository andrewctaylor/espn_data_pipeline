{{ config(materialized='view') }}

WITH categories_raw_cte AS(
    SELECT
        article_object:id as article_id,
        flattened.value as category_object
    FROM {{ ref('articles_raw') }},
    LATERAL FLATTEN(input => article_object:categories) AS flattened
    )
SELECT DISTINCT * FROM categories_raw_cte 