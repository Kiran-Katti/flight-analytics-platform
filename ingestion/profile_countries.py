import pandas as pd

df = pd.read_csv(
    "data/raw/airports/countries.csv",
    nrows=5
)

print(df.columns.tolist())
print(df.dtypes)