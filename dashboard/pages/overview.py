import dash
from dash import html
from database.db_connection import run_query

dash.register_page(
    __name__,
    path="/",
    name="Overview"
)

kpis = run_query("""
SELECT
    (SELECT COUNT(*) FROM analytics.fact_flights) AS total_flights,
    (SELECT COUNT(*) FROM analytics.dim_airports) AS total_airports,
    (SELECT COUNT(*) FROM analytics.dim_carriers) AS total_carriers,
    (SELECT COUNT(*) FROM analytics.dim_dates) AS total_dates
""")

layout = html.Div([

    html.H2("Executive Overview"),

    html.Div([
        html.H3(f"{kpis['total_flights'][0]:,}"),
        html.P("Total Flights")
    ]),

    html.Div([
        html.H3(f"{kpis['total_airports'][0]:,}"),
        html.P("Airports")
    ]),

    html.Div([
        html.H3(f"{kpis['total_carriers'][0]:,}"),
        html.P("Carriers")
    ]),

    html.Div([
        html.H3(f"{kpis['total_dates'][0]:,}"),
        html.P("Dates")
    ]),
])