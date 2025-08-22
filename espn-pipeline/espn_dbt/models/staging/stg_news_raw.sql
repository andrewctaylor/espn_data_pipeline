{{ config(materialized='view') }}

with base as (
  select
    id,
    json_blob,
    sport,
    league,
    created_at,
    sha2(to_json(json_blob), 256) as json_hash
  from RAW_JSON.NEWS_RAW
),
ranked as (
  select
    *,
    row_number() over (
      partition by json_hash
      order by created_at desc, id desc
    ) as rn
  from base
)
select
  id,
  json_blob,
  sport,
  league,
  created_at,
  json_hash
from ranked
where rn = 1
