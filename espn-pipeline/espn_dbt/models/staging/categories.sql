{{ config(materialized='table') }}

WITH categories_cte AS (
    SELECT
        article_id,
        category_object:id::INT as categoryId,
        category_object:athlete as athlete, -- TODO: Make Athletes Table
        category_object:athleteId::INT as athleteId,
        category_object:contributor as contributor, -- TODO: Make Contributors Table
        category_object:description::STRING as description,
        category_object:event as event,
        category_object:eventId::INT as eventId, -- TODO: Make Events Table
        category_object:guid::STRING as guid,
        category_object:leagueId::STRING as leagueId, -- TODO: Make Leagues Table
        category_object:league as league,
        category_object:sportId::INT as sportId, -- TODO: Find Sports Table
        category_object:teamId::INT as teamId,
        category_object:team as team, -- TODO: Make Teams Table
        category_object:topicId::INT as topicId,
        category_object:slug::STRING as slug,
        category_object:type::STRING as type,
        category_object:uid::STRING as uid,
        created_at
    FROM {{ ref('categories_raw') }})

SELECT DISTINCT * FROM categories_cte 