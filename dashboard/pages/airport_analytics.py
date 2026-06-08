import dash
from dash import html, dcc, Input, Output, callback
import plotly.express as px

from database.db_connection import run_query

dash.register_page(
    __name__,
    path="/airport-analytics",
    name="Airport Analytics"
)

airports_df = run_query("""
SELECT *
FROM analytics.mart_airport_activity
ORDER BY departure_count DESC
""")

layout = html.Div([

    html.H2("Airport Analytics"),

    dcc.Dropdown(
        id="airport-dropdown",
        options=[
            {
                "label": row["iata_code"],
                "value": row["iata_code"]
            }
            for _, row in airports_df.iterrows()
        ],
        value="ATL",
        clearable=False
    ),

    dcc.Graph(id="departure-chart"),

    dcc.Graph(id="delay-chart")

])


@callback(
    Output("departure-chart", "figure"),
    Output("delay-chart", "figure"),
    Input("airport-dropdown", "value")
)
def update_charts(selected_airport):

    airport_row = airports_df[
        airports_df["iata_code"] == selected_airport
    ]

    departure_fig = px.bar(
        airport_row,
        x="iata_code",
        y="departure_count",
        title="Departure Volume"
    )

    delay_fig = px.bar(
        airport_row,
        x="iata_code",
        y="avg_arrival_delay",
        title="Average Arrival Delay"
    )

    return departure_fig, delay_fig