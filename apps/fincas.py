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

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

tab_detalles = html.Div(
    id='tab-detalles',
    children=[
        # Campos a visualizar
        html.Div(
            id='div-input-name-f',
            children=[
                dbc.Label(
                    "Nombre de la finca"),
                # Añadir campo Output finca
            ],
            className='six colums'
        ),
        html.Div(
            id='div-dropdown-variedad-f',
            children=[
                dbc.Label("Variedad"),
                # Añadir campo Output variedad
            ], className='six colums'
        ),
        html.Div(
            id='div-input-espaciamiento-f',
            children=[
                dbc.Label('Espaciamiento'),
                # Añadir dos campos Output+H4(m) especiamiento
            ], className='one colums'
        ),
        html.Div(
            id='div-dropdown-suelo-f',
            children=[
                dbc.Label("Tipo de suelo"),
                # Añadir campo Output tipo de suelo
            ], className='six colums'
        ),
        html.Div(
            id='div-checkbox-riego-f',
            children=[
                dbc.Label("Riego"),
                # Añadir checkbox riego (solo opcion de resultado)
            ], className='six columns'
        ),
        html.Div(
            id='div-dropdown-recogida-f',
            children=[
                dbc.Label(
                    "Forma de recogida"),
                # Añadir campo Output forma de recogida
            ], className='six colums'
        ),
        html.Div(
            id='div-dropdown-lugar-f',
            children=[
                dbc.Label("Municipio"),
                # Añadir campo Output tipo de suelo
                dbc.Label('Provincia'),
                # Añadir Output provincia
            ], className='six colums'
        ),
        html.Div(
            id='div-button-eliminar-f',
            children=[
                html.Button(
                    'Eliminar',
                    id='button-eliminar-f'
                )
            ], className='two colums'
        )
    ]
)


app.layout = dbc.Container(
    [
        dcc.Store(id="store"),
        html.H1("Finca i"),
        html.Hr(),
        dbc.Button(
            "Regenerate graphs",
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
        html.Div(id="tab-content", className="p-4"),
    ]
)


@app.callback(
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

@app.callback(Output("store", "data"), [Input("button", "n_clicks")])
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



if __name__ == "__main__":
    app.run_server(debug=True)
