import dash
from dash import html, dcc
import plotly.express as px

from database.db_connection import run_query

dash.register_page(
    __name__,
    path="/carrier-performance",
    name="Carrier Performance"
)

df = run_query("""
SELECT *
FROM analytics.mart_carrier_performance
ORDER BY total_flights DESC
""")

flights_fig = px.bar(
    df,
    x="carrier_code",
    y="total_flights",
    title="Flights by Carrier"
)

delay_fig = px.bar(
    df.sort_values("avg_arrival_delay", ascending=False),
    x="carrier_code",
    y="avg_arrival_delay",
    title="Average Arrival Delay (Minutes)"
)

cancel_fig = px.bar(
    df.sort_values("cancellation_rate_pct", ascending=False),
    x="carrier_code",
    y="cancellation_rate_pct",
    title="Cancellation Rate (%)"
)

layout = html.Div([

    html.H2("Carrier Performance"),

    dcc.Graph(figure=flights_fig),

    dcc.Graph(figure=delay_fig),

    dcc.Graph(figure=cancel_fig)

])