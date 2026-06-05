import dash
from dash import Dash, html, dcc

app = Dash(
    __name__,
    use_pages=True
)

app.layout = html.Div([
    html.H1("Flight Analytics Dashboard"),

    html.Hr(),

    html.Div([
        dcc.Link("Overview", href="/"),
        html.Br(),

        dcc.Link(
            "Carrier Performance",
            href="/carrier-performance"
        ),
        html.Br(),

        dcc.Link(
            "Airport Analytics",
            href="/airport-analytics"
        ),
    ]),

    html.Hr(),

    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=True)