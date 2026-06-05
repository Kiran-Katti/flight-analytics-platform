WITH source AS (

    SELECT *
    FROM {{ source('raw', 'airports') }}

)

SELECT *

FROM source