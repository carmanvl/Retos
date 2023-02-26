import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Login', path="/")


# Componentes login
correo_u = dbc.Container(
    id='div-input-correo-u',
    children=[
        dcc.Markdown('##### Correo electrónico', className="text-center"),
        dbc.Input(
            id='input-correo-u',
            placeholder='Ej: user@user.com',
            type='email',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba su correo electrónico aquí... ")
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
            n_clicks=0,
            color='#556B2F',
            style={'color':'#FFFAF0', 'background':'#556B2F'},
            className="mb-2 w-50",
            href="/inicio"
        )
    ], className="text-center"  
)

formL = dbc.Form(
    id='form-l',
    children=[
            correo_u,
            html.Hr(className="p-1 bg-transparent"),
            passwd_u,
            html.Hr(className="p-3 bg-transparent"),
            button_login_u
    ], className="form-group ")

formCardL = dbc.Card(
    children=[
        dcc.Markdown('### **Inicio de sesión**', className="text-center", style={'color':'#556B2F'}),
        html.Hr(),
        html.Hr(className="p-2 bg-transparent"),
        formL
        ], style={'background-color':'#dedeb9'}
)

# Componentes registro
correo_r = dbc.Container(
    id='div-input-correo-r',
    children=[
        dcc.Markdown("##### Correo electrónico", className="text-center"),
        dbc.Input(
            id='input-correo-r',
            placeholder='Ej: user@user.com',
            type='email',
            value='',
            className="input-group mb-2 mr-sm-2 form-control"
        ),
        dbc.FormText("Escriba su correo electrónico aquí... ")
    ]
)

passwd_r = dbc.Container(
    id='div-input-passwd-r',
    children=[
        dcc.Markdown("##### Contraseña", className="text-center"),
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
        dcc.Markdown("##### Repetir contraseña", className="text-center"),
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

button_guardar_r = dbc.Container(
    id='div-button-guardar-r',
    children=[
        dbc.Button(
            'Registrarme',
            id='button-guardar-r',
            color='#556B2F',
            style={'color':'#FFFAF0', 'background':'#556B2F'},
            n_clicks=0,
            className="mb-2 w-50",
            href="/"
        )
    ], className="text-center"
)

formR = dbc.Form(children=[
    correo_r,
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

formCardR = dbc.Card(
    children=[
        dcc.Markdown('### **Registro de usuario**', className="text-center", style={'color':'#556B2F'}),
        html.Hr(),
        html.Hr(className="p-2 bg-transparent"),
        formR
        ], className="", style={'background-color':'#dedeb9'} 
)


# Layout página de login
layout = dbc.Container(children=[
    dbc.Row([
        html.Hr(className="p-3 bg-transparent"),
        dbc.Row([formCardL], className="col-8"), 
        dbc.Row([dcc.Markdown('ó', className="text-center fst-italic p-3")], className="col-12"),
        dbc.Row([formCardR], className="col-8")
    ], className="justify-content-center",
)
],
    fluid=True,
    className="container", style={'color': '#556B2F'}
)
