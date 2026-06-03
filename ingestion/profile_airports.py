import pandas as pd

df = pd.read_csv(
    "data/raw/airports/airports.csv",
    nrows=5
)

print("\nColumns:\n")
print(df.columns.tolist())

print("\nDtypes:")
print(df.dtypes)