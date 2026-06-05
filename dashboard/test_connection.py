# dashboard/test_connection.py

from database.db_connection import run_query

df = run_query("""
SELECT COUNT(*) AS total_flights
FROM analytics.fact_flights
""")

print(df)