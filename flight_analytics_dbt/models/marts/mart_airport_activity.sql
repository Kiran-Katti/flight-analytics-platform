{{ config(materialized='table') }}

SELECT

    a.iata_code,
    a.airport_name,
    a.municipality,
    a.iso_country,

    COUNT(*) AS departure_count,

    AVG(f.depdelay) AS avg_departure_delay,
    AVG(f.arrdelay) AS avg_arrival_delay

FROM {{ ref('stg_flights') }} f

INNER JOIN {{ ref('dim_airports') }} a
    ON f.origin = a.iata_code

GROUP BY
    a.iata_code,
    a.airport_name,
    a.municipality,
    a.iso_country