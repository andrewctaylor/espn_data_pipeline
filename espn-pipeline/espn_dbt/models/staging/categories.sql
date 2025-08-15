{{ config(materialized='table') }}

WITH categories_cte AS (
    SELECT
        article_id,
        category_object:id::INT as categoryId,
        category_object:athlete as athlete, -- Make Athletes Table
        category_object:athleteId::INT as athleteId,
        category_object:contributor as contributor, -- Make Contributors Table
        category_object:description::STRING as description,
        category_object:event as event,
        category_object:eventId::INT as eventId, -- Make Events Table
        category_object:guid::STRING as guid,
        category_object:leagueId::STRING as leagueId, -- Make Leagues Table
        category_object:league as league,
        category_object:sportId::INT as sportId, -- Find Sports Table
        category_object:teamId::INT as teamId,
        category_object:team as team, -- Make Teams Table
        category_object:topicId::INT as topicId,
        category_object:slug::STRING as slug,
        category_object:type::STRING as type,
        category_object:uid::STRING as uid,
    FROM {{ ref('categories_raw') }})

SELECT DISTINCT * FROM categories_cte 