from dash import html
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Ajustes', path="/ajustes")

layout = dbc.Container([html.H1("   Pagina de ajustes")], fluid=True)