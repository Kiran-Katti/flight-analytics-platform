import pandas as pd

df = pd.read_csv(
    "data/raw/flights/DelayedFlights.csv",
    nrows=5
)

print("\nColumns:\n")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nDtypes:")
print(df.dtypes)