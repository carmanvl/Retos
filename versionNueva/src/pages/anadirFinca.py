import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__, name='Añadir nueva finca', path='/inicio')

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
                                value='',
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
                                    className='input-group justify-content-center',
                                )],
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
                    id='row-button-guardar-nf',
                    children=[
                        dbc.Button(
                            'Guardar',
                            id='button-guardar-nf',
                            href="/inicio",
                            n_clicks=0,
                            color='#556B2F',
                            style={'color':'#FFFAF0', 'background':'#556B2F'}
                        )
                    ], className='p-3'
                )
            ], fluid=True
        )
    ], fluid=True)


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Form(fincas_layout)
        ], className='col-10')
    ], className='justify-content-center', style={'color':'#556B2F'})
], fluid=True)
