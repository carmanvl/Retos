import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
from datetime import datetime as dt
import plotly.graph_objects as go
from dash import Input, Output, State, callback
from pages import registro

# STYLE
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page(__name__, name='login', path="/login")


# COMPONENTS
# Componentes simples
correo_u = dbc.Container(
    id='div-input-correo-u',
    children=[
        dcc.Markdown('##### Correo electrónico', className="text-center"),
        dbc.Input(
            id='input-correo-u',
            placeholder='Escriba aquí...',
            type='email',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba su correo aquí... Ej: user@user.com")
    ]
)

passwd_u = dbc.Container(
    id='div-input-passwd-u',
    children=[
        dcc.Markdown('##### Contraseña', className="text-center"),
        dbc.Input(
            id='input-passwd-u',
            placeholder='Ej: ksSF8Jcas7',
            type='password',
            value='',
            className="input-group form-control"
        ),
        dbc.FormText("Escriba su contraseña aquí... ")
    ], 
)

button_login_u = dbc.Container(
    id='div-button-login-u',
    children=[
        dbc.Button(
            'Iniciar sesión',
            id='button-login-u',
            color="Primary",
            n_clicks=0,
            className="btn btn-success mb-2 w-25"
        )
    ], className="text-center"   # Aqui cogeria el div entero el formato
)

button_registro_u = dbc.Container(
    id='div-button-registro-u',
    children=[
        dbc.Button(
            # dcc.Link('Registrarme', href=dash.page_registry['pages.registro']['path']),
            'Registrarme',
            id='button-registro-u',
            color="Primary",
            n_clicks=0,
            className="btn btn-secondary mb-2 w-25",
            href="/registro"
        )
    ], className="text-center"
)


logo = dbc.Container(
    id='div-logo-u',
    children=[
        dcc.Markdown('# **Oilweb**', className="text-left pb-5 pt-2")
    ]
)

# Componente Formulario
formU = dbc.Form(
    id='form-u',
    children=[
            correo_u,
            html.Hr(className="p-1 bg-transparent"),
            passwd_u,
            html.Hr(className="p-3 bg-transparent"),
            button_login_u,
            dcc.Markdown('*or*', className="text-black-50 text-center"),
            button_registro_u
    ], className="form-group ")

formCard = dbc.Card(
    children=[
        dcc.Markdown('### **Inicio de sesión**', className="text-center bg-secondary text-white"),
        html.Hr(className="p-2 bg-transparent"),
        formU
        ], className="bg-light" # d-inline-block ¿?¿?
)

# LAYOUT
layout = dbc.Container(children=[
    logo,
    formCard
],
    fluid=True,
    className="container",
    #style={'backgroundColor': 'white'}
)

# CALLBACKS

@callback(
    Output("div-logo-u", "children"),
    [Input("button-registro-u", "n_clicks")]
)
def click_registro(n):
    if n is 1:
        return registro.layout