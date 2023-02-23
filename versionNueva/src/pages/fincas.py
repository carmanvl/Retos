import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from datetime import datetime as dt, time
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Input, Output, callback

# Una página por cada finca registrada
dash.register_page(__name__, name='Finca i', path="/fincai")


tab_detalles = dbc.Container(
    id='tab-detalles-f',
    children=[
        # Campos a visualizar
        dbc.Row(
            id='row-input-name-nf',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Nombre de la finca"),
                    dcc.Input(
                        id='input-name-nf',
                        placeholder='Ej: Nombre',
                        type='text',
                        value='',
                        className="text-start col-12 input-group form-control",
                    )
                ], className='col-12')
            ], className='p-3'
        ),
        dbc.Row(
            id='row-dropdown-variedad-nf',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Variedad"),
                    dcc.Dropdown(   # Multi¿?
                        id='dropdown-variedad-nf',
                        options=[
                                    {'label': 'Variedad1',
                                     'value': 'variedad1'},
                                    {'label': 'Variedad2',
                                     'value': 'variedad2'},
                                    {'label': 'Variedad3',
                                     'value': 'variedad3'}
                        ],
                        value='variedad1',
                        multi=True,
                        className='input-group '
                    )
                ], className='col-12')
            ], className='p-3'
        ),
        dbc.Row(
            id='row-input-espaciamiento-riego-nf',
            children=[
                dbc.Col([
                    dbc.Row(dcc.Markdown("##### Espaciamiento")),
                    dbc.Row([
                        dbc.Col([
                            dcc.Input(
                                id='input-espaciamiento1-nf',
                                type='text',
                                value='',
                                size="20",
                                placeholder="m",
                                className="text-center input-group form-control"
                            )
                        ], className="col-3"),
                        dbc.Col([dcc.Markdown("##### x")],
                                className="col-1 text-center"),
                        dbc.Col([
                            dcc.Input(
                                id='input-espaciamiento2-nf',
                                type='text',
                                value='',
                                size="20",
                                placeholder="m",
                                className="text-center input-group form-control"
                            )
                        ], className="col-3"),
                    ], className="row align-items-start")
                ], className='col-7'),
                dbc.Col([
                    dbc.Col([
                        dcc.Markdown("##### Riego"),
                        dcc.Checklist(
                            id='checklist-riego-nf',
                            options=[
                                {'label': '', 'value': 'riego'}
                            ],
                            value=['riego'],
                            className='input-group',
                            # inputStyle=''
                        )],
                        className='col-1 me-auto',
                        align='start')
                ])
            ], align='start', className='p-3'
        ),
        dbc.Row(
            id='row-dropdown-suelo-nf',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Tipo de suelo"),
                    dcc.Dropdown(   # Multi¿?
                        id='dropdown-suelo-nf',
                        options=[
                                    {'label': 'Suelo1', 'value': 'suelo1'},
                                    {'label': 'Suelo2', 'value': 'suelo2'},
                                    {'label': 'Suelo3', 'value': 'suelo3'}
                        ],
                        value='',
                        multi=True,
                        className='input-group'
                    )
                ], className="col-12")
            ], className='p-3'
        ),
        dbc.Row(
            id='row-dropdown-recogida-nf',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Forma de recogida"),
                    dcc.Dropdown(   # Multi¿?
                        id='dropdown-recogida-nf',
                        options=[
                                    {'label': 'Metodo1',
                                     'value': 'metodo1'},
                                    {'label': 'Metodo2',
                                     'value': 'metodo2'},
                                    {'label': 'Metodo3',
                                     'value': 'metodo3'}
                        ],
                        value='',
                        multi=True,
                        className='input-group'
                    )
                ])
            ], className='p-3'
        ),
        dbc.Row(
            id='row-dropdown-lugar-nf',
            children=[
                dbc.Col(
                    id='col-dropdown-provincia-nf',
                    children=[
                        dcc.Markdown("##### Provincia"),
                        dcc.Dropdown(   # Multi¿?
                            id='dropdown-provincia-nf',
                            options=[
                                        {'label': 'Provincia1',
                                         'value': 'provincia1'},
                                        {'label': 'Provincia2',
                                         'value': 'provincia2'},
                                        {'label': 'Provincia3',
                                         'value': 'provincia3'}
                            ],
                            value='',
                            className='input-group'
                        )
                    ], className='col-5 me-auto'
                ),
                dbc.Col(
                    id='col-dropdown-municipio-nf',
                    children=[
                        dcc.Markdown("##### Municipio"),
                        dcc.Dropdown(   # Multi¿?
                            id='dropdown-municipio-nf',
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
                    ], className='col-5 me-auto'
                )
            ], className='p-3'
        ),
        dbc.Row(
            id='row-button-eliminar-f',
            children=[
                dbc.Button(
                    'Eliminar',
                    id='button-eliminar-f',
                    href="/inicio",  # Eliminar de la BD
                    n_clicks=0,
                    color='#556B2F',
                    style={'color':'#FFFAF0', 'background':'#556B2F'}
                )
            ], style={'padding-top': '2%'}
        )
    ]
)


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Container([
                dcc.Store(id="store"),
                dcc.Markdown("## Finca i", className=""),
                html.Hr(),
                dbc.Button(
                    "Regenerar gráficos",
                    id="button",
                    className="mb-3",
                    color='#556B2F',
                    style={'color':'#FFFAF0', 'background':'#556B2F'}
                ),
                dbc.Tabs(
                    [
                        dbc.Tab(label="Detalles", tab_id="detalles"),
                        dbc.Tab(label="Gráficos", tab_id="graficos"),
                    ],
                    id="tabs",
                    active_tab="detalles",
                ),
                dbc.Container(id="tab-content", className="p-4"),
            ])

        ], className="col-12 justify-content-center")

    ])
], fluid=True, style={'color': '#556B2F'}
)


@callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)
def render_tab_content(active_tab, data):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab is not None:

        if active_tab == "detalles":
            return tab_detalles
        elif active_tab == "graficos":
            return dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=data["hist_1"]), width=6),
                    dbc.Col(dcc.Graph(figure=data["hist_2"]), width=6),
                ]
            )
    return "No tab selected"


@callback(Output("store", "data"), [Input("button", "n_clicks")])
def generate_graphs(n):
    """
    This callback generates three simple graphs from random data.
    """
    if not n:
        # generate empty graphs when app loads
        return {k: go.Figure(data=[]) for k in ["detalles", "hist_1", "hist_2"]}

    # simulate expensive graph generation process
    time.sleep(2)

    # generate 100 multivariate normal samples
    data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)

    scatter = go.Figure(
        data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
    )
    hist_1 = go.Figure(data=[go.Histogram(x=data[:, 0])])
    hist_2 = go.Figure(data=[go.Histogram(x=data[:, 1])])

    # save figures in a dictionary for sending to the dcc.Store
    return {"detalles": scatter, "hist_1": hist_1, "hist_2": hist_2}
