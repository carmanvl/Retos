import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
from datetime import datetime as dt
import plotly.graph_objects as go

# STYLE
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page(__name__)

# COMPONENTEs
name_r = dbc.Container(
    id='div-input-name-r',
    children=[
        dcc.Markdown('##### Nombre de usuario', className="font-weight-bold"),
        dbc.Input(
            id='input-name-r',
            placeholder='Escriba aquí...',
            type='text',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba su nombre aquí... Ej: Nombre")
        # Añadir validaciones de entrada con "valid"
    ]
)

apellidos_r = dbc.Container(
    id='div-input-apellidos-r',
    children=[
        dcc.Markdown('##### Apellidos'),
        dbc.Input(
            id='input-apellidos-r',
            placeholder='Ej: Apellido1 Apellido2',
            type='text',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba su apellido aquí... Ej: Nombre")
    ]
)

correo_r = dbc.Container(
    id='div-input-correo-r',
    children=[
        dcc.Markdown("##### Correo electrónico"),
        dbc.Input(
            id='input-correo-r',
            placeholder='Ej: user@user.com',
            type='email',
            value='',
            className="input-group mb-2 mr-sm-2 form-control w-75"
        ),
        dbc.FormText("Escriba su correo electrónico aquí... ")
    ]
)

dni_r = dbc.Container(
    id='div-input-dni-r',
    children=[
        dcc.Markdown("##### DNI"),
        dbc.Input(
            id='input-dni-r',
            placeholder='Ej: 09000032K',
            type='text',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba su DNI aquí... ")
    ]
)

passwd_r = dbc.Container(
    id='div-input-passwd-r',
    children=[
        dcc.Markdown("##### Contraseña"),
        dbc.Input(
            id='input-passwd-r',
            placeholder='Ej: ksSF8Jcas7',
            type='password',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba su contraseña aquí... ")
    ]
)

repetir_passwd_r = dbc.Container(
    id='div-input-passwd-r',
    children=[
        dcc.Markdown("##### Repetir contraseña"),
        dbc.Input(
            id='input-passwd-r',
            placeholder='Ej: ksSF8Jcas7',
            type='password',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba de nuevo su contraseña aquí... ")
    ]
)


telefono_r = dbc.Container(
    id='div-input-telefono-r',
    children=[
        dcc.Markdown("##### Teléfono"),
        dbc.Input(
            id='input-telefono-r',
            placeholder='Ej: 685413244',  # Tipo¿?
            type='text',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba su teléfono aquí... ")
    ]
)
# Repetir la contraseña y verificar que es la misma

button_guardar_r = dbc.Container(
    id='div-button-guardar-r',
    children=[
        dbc.Button(
            'Registrarme',
            id='button-guardar-r',
            color='primary',
            n_clicks=0,
            className="btn btn-success mb-2 w-25"
        )
    ], className="text-center"
)

logo = dbc.Container(
    id='div-logo-u',
    children=[
        dcc.Markdown('# **Oilweb**', className="text-left pb-5 pt-2")
    ]
)

# Componente FORM
form = dbc.Form(children=[
    dbc.Row(children=[
        dbc.Col(name_r),
        dbc.Col(apellidos_r)
    ]),
    html.Hr(className="p-1 bg-transparent"),
    dbc.Row(children=[
        dbc.Col(dni_r),
        dbc.Col(telefono_r)
    ]),
    html.Hr(className="p-1 bg-transparent"),
    dbc.Row(children=[
        dbc.Col(correo_r)
    ]),
    html.Hr(className="p-1 bg-transparent"),
    dbc.Row(children=[
        dbc.Col(passwd_r),
        dbc.Col(repetir_passwd_r)
    ]),
    html.Hr(className="p-3 bg-transparent"),
    dbc.Row(children=[
        button_guardar_r
    ], className="pad-row")

])


# LAYOUT
app.layout = dbc.Container(
    children=[
        logo,
        dcc.Markdown('### **Registro de nuevo usuario**',
                     className="text-center pb-5 pt-2"),
        form
    ],
    fluid=True,
    className="container",
    style={'backgroundColor': 'white'}
)

# MAIN
if __name__ == "__main__":
    app.run_server(debug=True)
