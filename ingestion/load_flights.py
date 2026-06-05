from etl_utils import load_large_csv_to_postgres

load_large_csv_to_postgres(
    source_file="data/raw/flights/DelayedFlights.csv",
    target_schema="raw",
    target_table="flights",
    chunksize=50000
)