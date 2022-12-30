import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from datetime import datetime as dt, time
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Input, Output
from flask import render_template

dash.register_page(__name__, name='añadirFinca', path='/')

fincas_layout = dbc.Container(
    [
        html.H3("Añadir finca"),
        dbc.Container(
            id='div-row1-f',
            children=[
                dbc.Row(
                    id='div-input-name-f',
                    children=[
                        html.H3("Nombre de la finca"),
                        dcc.Input(
                            id='input-name-f',
                            placeholder='Ej: Nombre',
                            type='text',
                            value=''
                        )
                    ], className='six colums'
                ),
                dbc.Row(
                    id='div-dropdown-variedad-f',
                    children=[
                        html.H3("Variedad"),
                        dcc.Dropdown(   # Multi¿?
                            id='dropdown-variedad-f',
                            options=[
                                {'label': 'Variedad1',
                                 'value': 'variedad1'},
                                {'label': 'Variedad2',
                                 'value': 'variedad2'},
                                {'label': 'Variedad3',
                                 'value': 'variedad3'}
                            ],
                            value='variedad1'
                        )
                    ], className='six colums'
                ),
                dbc.Row(
                    id='div-input-espaciamiento-f',
                    children=[
                        html.H3('Espaciamiento'),
                        # Añadir dos campos Input+H4(m) especiamiento
                        dcc.Input(
                            id='input-espaciamiento1-f',
                            type='text',
                            value=''
                        ),
                        html.H3('m x'),
                        dcc.Input(
                            id='input-espaciamiento2-f',
                            type='text',
                            value=''
                        ),
                        html.H3('m')
                    ], className='four colums'
                ),
                dbc.Row(
                    id='div-dropdown-suelo-f',
                    children=[
                        html.H3("Tipo de suelo"),
                        dcc.Dropdown(   # Multi¿?
                            id='dropdown-suelo-f',
                            options=[
                                {'label': 'Suelo1', 'value': 'suelo1'},
                                {'label': 'Suelo2', 'value': 'suelo2'},
                                {'label': 'Suelo3', 'value': 'suelo3'}
                            ],
                            value=''
                        )
                    ], className='six colums'
                ),
                dbc.Row(
                    id='div-checklist-riego-f',
                    children=[
                        html.H3("Riego"),
                        dcc.Checklist(
                            id='checklist-riego-f',
                            options=[
                                {'label': 'Riego', 'value': 'riego'}
                            ],
                            value=['riego']
                        )
                    ], className='row'
                ),
                dbc.Row(
                    id='div-dropdown-recogida-f',
                    children=[
                        html.H3("Forma de recogida"),
                        dcc.Dropdown(   # Multi¿?
                            id='dropdown-recogida-f',
                            options=[
                                {'label': 'Metodo1',
                                 'value': 'metodo1'},
                                {'label': 'Metodo2',
                                 'value': 'metodo2'},
                                {'label': 'Metodo3',
                                 'value': 'metodo3'}
                            ],
                            value=''
                        )
                    ], className='row'
                ),
                dbc.Row(
                    id='div-dropdown-lugar-f',
                    children=[
                        dbc.Col(
                            id='div-dropdown-provincia-f',
                            children=[
                                html.H3('Provincia'),
                                dcc.Dropdown(   # Multi¿?
                                    id='dropdown-provincia-f',
                                    options=[
                                        {'label': 'Provincia1',
                                         'value': 'provincia1'},
                                        {'label': 'Provincia2',
                                         'value': 'provincia2'},
                                        {'label': 'Provincia3',
                                         'value': 'provincia3'}
                                    ],
                                    value=''
                                )
                            ], className='six colums'
                        ),
                        dbc.Col(
                            id='div-dropdown-municipio-f',
                            children=[
                                html.H3("Municipio"),
                                dcc.Dropdown(   # Multi¿?
                                    id='dropdown-municipio-f',
                                    options=[
                                        {'label': 'Municipio1',
                                         'value': 'municipio1'},
                                        {'label': 'Municipio2',
                                         'value': 'municipio2'},
                                        {'label': 'Municipio3',
                                         'value': 'municipio3'}
                                    ],
                                    value=''
                                )
                            ], className='six colums'
                        )
                    ], className='six colums'
                ),
                dbc.Row(
                    id='div-button-guardar-f',
                    children=[
                        html.Button(
                            'Guardar',
                            id='button-guardar-f'
                        )
                    ], className='two colums', style={'padding-top': '2%'}
                )
            ]
        )
    ])


layout = dbc.Container(fincas_layout, fluid=True)
