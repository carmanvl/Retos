import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__, name='Inicio', path='/inicio')

fincas_layout = dbc.Container(
    [
        dcc.Markdown('## Añadir nueva finca', className="text-center"),
        dbc.Container(
            id='div-nf',
            children=[
                dbc.Row(
                    id='row-input-name-nf',
                    children=[
                        dbc.Col([
                            dcc.Markdown("##### Nombre de la finca"),
                            dcc.Input(
                                id='input-name-nf',
                                placeholder='Ej: Nombre',
                                type='text',
                                value=''
                            )
                        ])                       
                    ]
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
                                multi=True
                            )
                        ]) 
                    ]
                ),
                dbc.Row(
                    id='row-input-espaciamiento-nf',
                    children=[
                        dbc.Col([
                            dcc.Markdown("##### Espaciamiento m x m"),
                            dbc.Row([
                                dbc.Col([
                                    dcc.Input(
                                        id='input-espaciamiento1-nf',
                                        type='text',
                                        value=''
                                    )
                                ]),                               
                                dbc.Col([dcc.Markdown("##### x")], className="one colums g-0"),
                                dbc.Col([
                                    dcc.Input(
                                        id='input-espaciamiento2-nf',
                                        type='text',
                                        value=''
                                    )
                                ],className="two colums g-0"),                                
                            ])
                        ])                        
                    ], align='start'
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
                                multi=True
                            )
                        ])                        
                    ]
                ),
                dbc.Row(
                    id='row-checklist-riego-nf',
                    children=[
                        dbc.Col([dcc.Markdown("##### Riego")]),
                        dbc.Col([
                            dcc.Checklist(
                                id='checklist-riego-nf',
                                options=[
                                    {'label': '', 'value': 'riego'}
                                ],
                                value=['riego']
                            )
                        ])                      
                    ], className='row'
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
                                multi=True
                            )
                        ])                       
                    ], className='row'
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
                                    value=''
                                )
                            ], className='six colums'
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
                            ], className='six colums'
                        )
                    ], className='six colums'
                ),
                dbc.Row(
                    id='row-button-guardar-nf',
                    children=[
                        dbc.Button(
                            'Guardar',
                            id='button-guardar-nf',
                            href="/inicio",
                            n_clicks=0
                        )
                    ], style={'padding-top': '2%'}
                )
            ]
        )
    ])


layout = dbc.Container(fincas_layout, fluid=True)
