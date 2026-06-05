WITH source AS (

    SELECT *
    FROM {{ source('raw', 'countries') }}

)

SELECT *

FROM source