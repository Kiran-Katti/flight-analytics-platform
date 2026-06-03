CREATE TABLE IF NOT EXISTS raw.flights (

    flight_record_id BIGSERIAL PRIMARY KEY,

    year INTEGER,
    month INTEGER,
    dayofmonth INTEGER,
    dayofweek INTEGER,

    deptime NUMERIC,
    crsdeptime INTEGER,

    arrtime NUMERIC,
    crsarrtime INTEGER,

    uniquecarrier VARCHAR(10),
    flightnum INTEGER,
    tailnum VARCHAR(20),

    actualelapsedtime NUMERIC,
    crselapsedtime NUMERIC,
    airtime NUMERIC,

    arrdelay NUMERIC,
    depdelay NUMERIC,

    origin VARCHAR(10),
    dest VARCHAR(10),

    distance INTEGER,

    taxiin NUMERIC,
    taxiout NUMERIC,

    cancelled INTEGER,
    cancellationcode VARCHAR(10),

    diverted INTEGER,

    carrierdelay NUMERIC,
    weatherdelay NUMERIC,
    nasdelay NUMERIC,
    securitydelay NUMERIC,
    lateaircraftdelay NUMERIC,

    source_file VARCHAR(255),
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raw.airports (

    airport_record_id BIGSERIAL PRIMARY KEY,

    id BIGINT,

    ident VARCHAR(50),
    type VARCHAR(100),
    name VARCHAR(255),

    latitude_deg NUMERIC,
    longitude_deg NUMERIC,

    elevation_ft INTEGER,

    continent VARCHAR(20),

    iso_country VARCHAR(10),
    iso_region VARCHAR(50),

    municipality VARCHAR(255),

    scheduled_service VARCHAR(10),

    icao_code VARCHAR(20),
    iata_code VARCHAR(20),

    gps_code VARCHAR(20),
    local_code VARCHAR(20),

    home_link TEXT,
    wikipedia_link TEXT,

    keywords TEXT,

    source_file VARCHAR(255),
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raw.countries (

    country_record_id BIGSERIAL PRIMARY KEY,

    id INTEGER,

    code VARCHAR(10),
    name VARCHAR(255),
    continent VARCHAR(50),

    wikipedia_link TEXT,
    keywords TEXT,

    source_file VARCHAR(255),
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS audit.etl_execution_log (

    run_id BIGSERIAL PRIMARY KEY,

    source_name VARCHAR(100),

    records_loaded INTEGER,

    start_time TIMESTAMP,
    end_time TIMESTAMP,

    status VARCHAR(50),

    error_message TEXT
);