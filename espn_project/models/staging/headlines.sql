{{ config(materialized='view') }}

SELECT
    headline_object:allowSearch::string            AS allowSearch,
    headline_object:byline::string                 AS byline,
    headline_object:categories::VARIANT            AS categories,
    headline_object:dataSourceIdentifier::string   AS dataSourceIdentifier,
    headline_object:description::string            AS description,
    headline_object:gameId::string                 AS gameId,
    headline_object:headline::string               AS headline,
    headline_object:id::string                     AS id,
    headline_object:images::VARIANT                AS images,
    headline_object:keywords::VARIANT              AS keywords,
    headline_object:lastModified::string           AS lastModified,
    headline_object:linkText::string               AS linkText,
    headline_object:links::VARIANT                 AS links,
    headline_object:metrics::VARIANT               AS metrics,
    headline_object:nowId::string                  AS nowId,
    headline_object:originallyPosted::string       AS originallyPosted,
    headline_object:premium::string                AS premium,
    headline_object:published::string              AS published,
    headline_object:related::VARIANT               AS related,
    headline_object:source::string                 AS source,
    headline_object:story::string                  AS story,
    headline_object:type::string                   AS type,
    headline_object:video::VARIANT                 AS video
FROM {{ref("headlines_raw")}}