import dash
from dash import html, dcc
import plotly.express as px

from database.db_connection import run_query

dash.register_page(
    __name__,
    path="/",
    name="Overview"
)

# =========================
# KPI DATA
# =========================

kpis = run_query("""
SELECT
    (SELECT COUNT(*) FROM analytics.fact_flights) AS total_flights,
    (SELECT COUNT(*) FROM analytics.dim_airports) AS total_airports,
    (SELECT COUNT(*) FROM analytics.dim_carriers) AS total_carriers,
    (SELECT COUNT(*) FROM analytics.dim_dates) AS total_dates
""")

# =========================
# CHART DATA
# =========================

carrier_df = run_query("""
SELECT
    carrier_code,
    total_flights
FROM analytics.mart_carrier_performance
ORDER BY total_flights DESC
""")

carrier_fig = px.bar(
    carrier_df,
    x="carrier_code",
    y="total_flights",
    title="Flights by Carrier"
)

# =========================
# LAYOUT
# =========================

layout = html.Div([

    html.H2("Executive Overview"),

    html.Br(),

    # KPI SECTION

    html.Div([

        html.Div([
            html.H3(f"{kpis['total_flights'][0]:,}"),
            html.P("Total Flights")
        ],
        style={
            "display": "inline-block",
            "width": "23%",
            "textAlign": "center",
            "border": "1px solid lightgray",
            "padding": "10px",
            "margin": "5px"
        }),

        html.Div([
            html.H3(f"{kpis['total_airports'][0]:,}"),
            html.P("Airports")
        ],
        style={
            "display": "inline-block",
            "width": "23%",
            "textAlign": "center",
            "border": "1px solid lightgray",
            "padding": "10px",
            "margin": "5px"
        }),

        html.Div([
            html.H3(f"{kpis['total_carriers'][0]:,}"),
            html.P("Carriers")
        ],
        style={
            "display": "inline-block",
            "width": "23%",
            "textAlign": "center",
            "border": "1px solid lightgray",
            "padding": "10px",
            "margin": "5px"
        }),

        html.Div([
            html.H3(f"{kpis['total_dates'][0]:,}"),
            html.P("Dates")
        ],
        style={
            "display": "inline-block",
            "width": "23%",
            "textAlign": "center",
            "border": "1px solid lightgray",
            "padding": "10px",
            "margin": "5px"
        }),

    ]),

    html.Br(),
    html.Hr(),
    html.Br(),

    # CHART

    dcc.Graph(
        figure=carrier_fig
    )

])