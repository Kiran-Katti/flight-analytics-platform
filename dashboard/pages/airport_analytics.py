import dash
from dash import html

dash.register_page(
    __name__,
    path="/airport-analytics"
)

layout = html.Div([
    html.H2("Airport Analytics")
])