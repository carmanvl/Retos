from dash import html
import dash

dash.register_page(__name__, name='Ajustes', path="/ajustes")

layout = html.H1("Pagina de ajustes")