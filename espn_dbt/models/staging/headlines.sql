{{ config(materialized='view') }}

SELECT 
    article_id,
    article_object:byline::string                 AS byline,
    article_object:categories::VARIANT            AS categories,
    article_object:dataSourceIdentifier::string   AS dataSourceIdentifier
    
FROM {{ref("articles_raw")}}