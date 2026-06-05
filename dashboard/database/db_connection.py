# dashboard/database/db_connection.py

from sqlalchemy import create_engine
import pandas as pd


DB_URL = (
    "postgresql+psycopg2://"
    "postgres:postgres@localhost:5432/flight_analytics"
)

engine = create_engine(DB_URL)


def run_query(query):
    return pd.read_sql(query, engine)