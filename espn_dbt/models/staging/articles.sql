{{ config(materialized='table') }}

WITH articles_cte AS (
  SELECT 
      article_object:byline::STRING               AS byline,
      article_object:categories                   AS categories,
      article_object:dataSourceIdentifier::STRING AS dataSourceIdentifier,
      article_object:description::STRING          AS description,
      article_object:headline::STRING             AS headline,
      article_object:id::INT                      AS article_id,
      article_object:images                       AS images,
      article_object:lastModified::TIMESTAMP_NTZ  AS lastModified,
      article_object:links                        AS links,
      article_object:nowId::STRING                AS nowId,
      article_object:premium::BOOLEAN             AS premium,
      article_object:published::TIMESTAMP_NTZ     AS published,
      article_object:type::STRING                 AS type
  FROM {{ ref('articles_raw') }}
)

SELECT DISTINCT * FROM articles_cte   -- handling exact duplicates