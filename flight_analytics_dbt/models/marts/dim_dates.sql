{{ config(materialized='table') }}

SELECT DISTINCT

    year,
    month,
    dayofmonth,
    dayofweek,

    make_date(
        year,
        month,
        dayofmonth
    ) AS flight_date

FROM {{ ref('stg_flights') }}