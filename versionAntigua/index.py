# PAGINA EN LA QUE SE ENCUENTRAN LOS ENLACES Y URLS

# NO SIRVE SI NO USO TEMPLATES

import dash
import dash_bootstrap_components as dbc
from flask import Flask
from dash import html
import dash_core_components as dcc
from apps import anadirFinca, fincas, home, login, registro
from app import app
from dash import Input, Output

url_content_layout = dbc.Container([
    dcc.Location(id="url", refresh=False),
    dbc.Container(id="output-div")
])

app.layout = url_content_layout

app.validation_layout = dbc.Container([
    url_content_layout,
    login.login_layout,
    home.home_layout

])

# CALLBACKS
@app.callback(Output(component_id="output-div", component_property="children"), Input(component_id="url", component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/login":
        return login.login_layout
    elif pathname == "/anadirfinca":
        return anadirFinca.fincas_layout
    else: 
        return home.home_layout

# MAIN
if __name__ == "__main__":
    app.run_server(debug=True) 