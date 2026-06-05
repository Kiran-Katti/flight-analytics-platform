from etl_utils import load_csv_to_postgres

load_csv_to_postgres(
    source_file="data/raw/airports/countries.csv",
    target_schema="raw",
    target_table="countries"
)