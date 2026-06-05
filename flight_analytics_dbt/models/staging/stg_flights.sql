WITH source AS (

    SELECT *
    FROM {{ source('raw', 'flights') }}

)

SELECT

    flight_record_id,

    year,
    month,
    dayofmonth,
    dayofweek,

    origin,
    dest,

    uniquecarrier,
    flightnum,
    tailnum,

    deptime,
    arrtime,

    crsdeptime,
    crsarrtime,

    depdelay,
    arrdelay,

    airtime,
    actualelapsedtime,

    distance,

    cancelled,
    diverted,

    carrierdelay,
    weatherdelay,
    nasdelay,
    securitydelay,
    lateaircraftdelay,

    source_file,
    load_timestamp

FROM source