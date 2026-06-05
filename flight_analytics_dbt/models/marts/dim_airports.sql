{{ config(materialized='table') }}

SELECT DISTINCT

    iata_code,
    name AS airport_name,
    municipality,
    iso_country,
    latitude_deg,
    longitude_deg

FROM {{ ref('stg_airports') }}

WHERE iata_code IS NOT NULL