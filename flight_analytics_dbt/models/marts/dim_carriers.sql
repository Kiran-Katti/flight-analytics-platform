{{ config(materialized='table') }}

SELECT DISTINCT

    uniquecarrier AS carrier_code

FROM {{ ref('stg_flights') }}

WHERE uniquecarrier IS NOT NULL