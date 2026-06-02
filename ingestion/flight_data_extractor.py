# Importing dependencies
import pandas as pd
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

# Setting connection to OpenSky api
url = "https://opensky-network.org/api/states/all"
response = requests.get(url)
data = response.json()

# Column names for state vectors
columns = [
    "icao24",
    "callsign",
    "origin_country",
    "time_position",
    "last_contact",
    "longitude",
    "latitude",
    "baro_altitude",
    "on_ground",
    "velocity",
    "true_track",
    "vertical_rate",
    "sensors",
    "geo_altitude",
    "squawk",
    "spi",
    "position_source"
]

# Creating DataFrame
df = pd.DataFrame(data['states'], columns=columns)
# Adding unix timestamp as a new column
df['unix_timestamp'] = data['time']

# Debugging
print(df.head())

timestamp = data['time']

dt_ist = datetime.fromtimestamp(
    timestamp,
    tz=ZoneInfo("Asia/Kolkata")
)

print(dt_ist)