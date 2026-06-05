{{ config(materialized='table') }}

SELECT

    uniquecarrier AS carrier_code,

    COUNT(*) AS total_flights,

    SUM(cancelled) AS cancelled_flights,

    ROUND(
        100.0 * SUM(cancelled) / COUNT(*),
        2
    ) AS cancellation_rate_pct,

    ROUND(
        AVG(depdelay),
        2
    ) AS avg_departure_delay,

    ROUND(
        AVG(arrdelay),
        2
    ) AS avg_arrival_delay

FROM {{ ref('stg_flights') }}

GROUP BY uniquecarrier