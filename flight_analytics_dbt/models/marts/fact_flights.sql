{{ config(materialized='table') }}

SELECT

    flight_record_id,

    make_date(
        year,
        month,
        dayofmonth
    ) AS flight_date,

    uniquecarrier AS carrier_code,

    origin,
    dest,

    distance,

    depdelay,
    arrdelay,

    cancelled,
    diverted,

    actualelapsedtime,
    airtime

FROM {{ ref('stg_flights') }}