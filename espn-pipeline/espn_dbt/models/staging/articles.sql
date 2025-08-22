{{ config(materialized='table') }}

WITH articles_cte AS (
  SELECT 
      article_object:id::INT                      AS article_id,
      article_object:byline::STRING               AS byline,
      article_object:dataSourceIdentifier::STRING AS dataSourceIdentifier,
      article_object:description::STRING          AS description,
      article_object:headline::STRING             AS headline,
      article_object:lastModified::TIMESTAMP_NTZ  AS lastModified,
      league,
      article_object:nowId::STRING                AS nowId,
      article_object:premium::BOOLEAN             AS premium,
      article_object:published::TIMESTAMP_NTZ     AS published,
      sport,                                       
      article_object:type::STRING                 AS type,
      created_at
  FROM {{ ref('articles_raw') }}
)

SELECT DISTINCT * FROM articles_cte   -- handling exact duplicates