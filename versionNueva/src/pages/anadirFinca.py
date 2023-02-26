import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__, name='Añadir nueva finca', path='/inicio')

# Componentes de una finca
name = dcc.Input(
    id='input-name-nf',
    placeholder='Ej: Nombre',
    type='text',
    value='',
    className="text-start col-12 input-group form-control",
)

variedad = dcc.Dropdown(
    id='dropdown-variedad-nf',
    options=[
        {'label': 'Variedad1',
         'value': 'variedad1'},
        {'label': 'Variedad2',
         'value': 'variedad2'},
        {'label': 'Variedad3',
         'value': 'variedad3'}
    ],
    value='',
    multi=True,  # True para elegir más de una opción, False solo una
    className='input-group '
)

espaciamiento = dbc.Row([
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

riego = dcc.Checklist(
    id='checklist-riego-nf',
    options=[
        {'label': '', 'value': 'riego'}
    ],
    value=['riego'],
    className='input-group justify-content-center',
)

suelo = dcc.Dropdown(  
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

recogida = dcc.Dropdown(
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

provincia = dcc.Dropdown(
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

municipio = dcc.Dropdown(  
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

# Guarda en la BD los valores de la finca y actualiza la página
boton_guardar = dbc.Button(
    'Guardar',
    id='button-guardar-nf',
    href="/inicio",
    n_clicks=0,
    color='#556B2F',
    style={'color': '#FFFAF0', 'background': '#556B2F'}
)

# Estructura general del layout
fincas_layout = dbc.Container(
    [
        dcc.Markdown('## **Añadir nueva finca**', className="text-center"),
        dbc.Container(
            id='div-nf',
            children=[
                dbc.Row(
                    id='row-input-name-nf',
                    children=[
                        dbc.Col([
                            dcc.Markdown("##### Nombre de la finca"),
                            name
                        ], className='col-12')
                    ], className='p-3'
                ),
                dbc.Row(
                    id='row-dropdown-variedad-nf',
                    children=[
                        dbc.Col([
                            dcc.Markdown("##### Variedad"),
                            variedad
                        ], className='col-12')
                    ], className='p-3'
                ),
                dbc.Row(
                    id='row-input-espaciamiento-riego-nf',
                    children=[
                        dbc.Col([
                            dbc.Row(dcc.Markdown("##### Espaciamiento")),
                            espaciamiento
                        ], className='col-7'),
                        dbc.Col([
                            dbc.Col([
                                dcc.Markdown("##### Riego"),
                                riego
                            ],
                                className='col-2 me-auto',
                                align='start')
                        ])
                    ], align='start', className='p-3'
                ),
                dbc.Row(
                    id='row-dropdown-suelo-nf',
                    children=[
                        dbc.Col([
                            dcc.Markdown("##### Tipo de suelo"),
                            suelo
                        ], className="col-12")
                    ], className='p-3'
                ),
                dbc.Row(
                    id='row-dropdown-recogida-nf',
                    children=[
                        dbc.Col([
                            dcc.Markdown("##### Forma de recogida"),
                            recogida
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
                                provincia
                            ], className='col-5 me-auto'
                        ),
                        dbc.Col(
                            id='col-dropdown-municipio-nf',
                            children=[
                                dcc.Markdown("##### Municipio"),
                                municipio
                            ], className='col-5 me-auto'
                        )
                    ], className='p-3'
                ),
                dbc.Row(
                    id='row-button-guardar-nf',
                    children=[
                        boton_guardar
                    ], className='p-3'
                )
            ], fluid=True
        )
    ], fluid=True)


# Layout de la página Anadir Finca
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Form(fincas_layout)
        ], className='col-11')
    ], className='justify-content-center', style={'color': '#556B2F'})
], fluid=True)
