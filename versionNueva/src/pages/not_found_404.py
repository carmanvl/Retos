from dash import html
import dash
import dash_bootstrap_components as dbc


dash.register_page(__name__, path="/404")


layout = dbc.Container([html.H1("Custom 404")], fluid=True)