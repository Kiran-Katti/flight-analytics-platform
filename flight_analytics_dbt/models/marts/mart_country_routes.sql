{{ config(materialized='table') }}

WITH flights AS (

    SELECT *
    FROM {{ ref('stg_flights') }}

),

airports AS (

    SELECT *
    FROM {{ ref('stg_airports') }}

),

countries AS (

    SELECT *
    FROM {{ ref('stg_countries') }}

),

origin_airports AS (

    SELECT
        iata_code,
        iso_country
    FROM airports

),

destination_airports AS (

    SELECT
        iata_code,
        iso_country
    FROM airports

)

SELECT

    oc.name AS origin_country,
    dc.name AS destination_country,

    COUNT(*) AS departure_count,

    AVG(depdelay) AS avg_departure_delay,
    AVG(arrdelay) AS avg_arrival_delay,

    SUM(cancelled) AS cancelled_flights,
    SUM(diverted) AS diverted_flights

FROM flights f

LEFT JOIN origin_airports oa
    ON f.origin = oa.iata_code

LEFT JOIN destination_airports da
    ON f.dest = da.iata_code

LEFT JOIN countries oc
    ON oa.iso_country = oc.code

LEFT JOIN countries dc
    ON da.iso_country = dc.code

GROUP BY
    oc.name,
    dc.name