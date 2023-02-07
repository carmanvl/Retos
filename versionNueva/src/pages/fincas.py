import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from datetime import datetime as dt, time
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Input, Output, callback


dash.register_page(__name__, name='Finca i', path="/fincai")


tab_detalles = dbc.Container(
    id='tab-detalles-f',
    children=[
        # Campos a visualizar
        dbc.Row(
            id='row-input-name-f',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Nombre de la finca"),
                    dcc.Input(
                        id='input-name-f',
                        type='text',
                        value='',  # valor recogido de la BD
                        readOnly=True
                    )
                ])
            ]
        ),
        dbc.Row(
            id='row-input-variedad-f',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Variedad"),
                    dcc.Input(
                        id='input-variedad-f',
                        type='text',
                        value='',  # valor recogido de la BD
                        readOnly=True
                    )
                ])
            ]
        ),
        dbc.Row(
            id='row-input-espaciamiento-f',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Espaciamiento m x m"),
                    dbc.Row([
                        dbc.Col([
                            dcc.Input(
                                id='input-espaciamiento1-f',
                                type='text',
                                value='',  # valor recogido de la BD
                                readOnly=True,
                                size='10',
                            ),
                            dcc.Markdown("##### x"),
                            dcc.Input(
                                id='input-espaciamiento2-f',
                                type='text',
                                value='',  # valor recogido de la BD
                                readOnly=True,
                                size='10',
                                className='position-relative start'
                            )
                        ]),
                    ])
                ])
            ], align='start'
        ),
        dbc.Row(
            id='row-input-suelo-f',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Tipo de suelo"),
                    dcc.Input(
                        id='input-suelo-f',
                        type='text',
                        value='',  # valor recogido de la BD
                        readOnly=True
                    )
                ])
            ]
        ),
        dbc.Row(
            id='row-checklist-riego-f',
            children=[
                dbc.Col([dcc.Markdown("##### Riego")]),
                dbc.Col([
                    dcc.Checklist(
                        id='checklist-riego-nf',
                        options=[
                            {'label': '', 'value': 'riego'}
                        ],
                        value=['riego'],  # valor cogido de la BD
                    )
                ])
            ], className='row'
        ),
        dbc.Row(
            id='row-input-recogida-f',
            children=[
                dbc.Col([
                    dcc.Markdown("##### Forma de recogida"),
                    dcc.Input(
                        id='input-recogida-f',
                        type='text',
                        value='',  # valor recogido de la BD
                        readOnly=True
                    )
                ])
            ], className='row'
        ),
        dbc.Row(
            id='row-lugar-f',
            children=[
                dbc.Col(
                    id='col-dropdown-provincia-f',
                    children=[
                        dcc.Markdown("##### Provincia"),
                        dcc.Input(
                            id='input-provincia-f',
                            type='text',
                            value='',  # valor recogido de la BD
                            readOnly=True
                        )
                    ], className='six colums'
                ),
                dbc.Col(
                    id='col-input-municipio-f',
                    children=[
                        dcc.Markdown("##### Municipio"),
                        dcc.Input(
                            id='input-municipio-f',
                            type='text',
                            value='',  # valor recogido de la BD
                            readOnly=True
                        )
                    ], className='six colums'
                )
            ], className='six colums'
        ),
        dbc.Row(
            id='row-button-eliminar-f',
            children=[
                dbc.Button(
                    'Eliminar',
                    id='button-eliminar-f',
                    href="/inicio",  # Eliminar de la BD
                    n_clicks=0
                )
            ], style={'padding-top': '2%'}
        )
    ]
)


layout = dbc.Container(
    [
        dcc.Store(id="store"),
        dcc.Markdown("## Finca i", className="text-success"),
        html.Hr(),
        dbc.Button(
            "Regenerar gráficos",
            color="primary",
            id="button",
            className="mb-3",
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
    ], fluid=True
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
