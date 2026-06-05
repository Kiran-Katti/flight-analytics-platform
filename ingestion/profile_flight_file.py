import pandas as pd

SOURCE_FILE = "data/raw/flights/DelayedFlights.csv"

df = pd.read_csv(
    SOURCE_FILE,
    nrows=1000
)

print("Columns:", len(df.columns))
print("Sample rows:", len(df))

total_rows = sum(1 for _ in open(SOURCE_FILE, encoding="utf-8")) - 1

print("Estimated total rows:", total_rows)