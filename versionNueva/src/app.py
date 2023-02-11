import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html


app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.FLATLY])
server = app.server


navbar = dbc.Navbar([
    dbc.Container([
        dbc.Col([
                html.Img(src=app.get_asset_url('data/oliva.png'), width="75",
                         height="50"),
                dbc.NavbarBrand('OilWeb', href='/inicio', className="m-4 fs-3"),
                ], className='col-auto me-auto'),
        dbc.Col([
                dbc.DropdownMenu([
                    dbc.DropdownMenuItem(page["name"], href=page["path"])
                    for page in dash.page_registry.values()
                    if page["name"] not in ('Login', 'Ajustes', 'Not found 404')
                ],
                    nav=True,
                    label="Mis fincas",
                )
                ], className='col-auto me-auto'),
        dbc.Col([
                dbc.Button(
                    'Ajustes',
                    id='button-ajustes',
                    color="Primary",
                    n_clicks=0,
                    className="btn btn-secondary mb-2",
                    href="/ajustes"
                )
                ], className='col-auto')
    ])

],
    color="#003300",
    dark=True,
    className="rounded-bottom col-12"
)

navbarV = dbc.Container(children=[
    dbc.Col([
        dbc.Row([
            html.Img(src=app.get_asset_url('data/oliva.png'), width="100",
                     height="75"),
                dbc.NavbarBrand('OilWeb', href='/inicio', className="m-2 fs-2")
                ]),
        dbc.Row([
            dbc.DropdownMenu([
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                for page in dash.page_registry.values()
                if page["name"] not in ('Login', 'Ajustes', 'Not found 404')
            ],
                nav=True,
                label="Mis fincas",
            )
        ]),
        dbc.Row([
            dbc.Button(
                'Ajustes',
                id='button-ajustes',
                color="Primary",
                n_clicks=0,
                className="btn btn-secondary mb-2",
                href="/ajustes"
            )
        ])
    ])
])

app.layout = dbc.Container(
    [
        dbc.Row([
                navbar
                ], className='justify-content-center',),
        html.Hr(className="p-2 bg-transparent"),
        dbc.Row([
                dash.page_container
                ], className='border border-5 justify-content-center'),

    ],
    fluid=True,
    className="bg-white",
    style={'color': '#003300'}


)


if __name__ == "__main__":
    app.run(debug=True)
