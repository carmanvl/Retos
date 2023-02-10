import dash
import dash_bootstrap_components as dbc
from dash import html


app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.FLATLY])
server = app.server

navbar = dbc.NavbarSimple(id='navBar', children=[
    dbc.Row([
        dbc.Col([
            html.Img(src=app.get_asset_url('data/oliva.png'), width="100",
                     height="75", className="position-relative top"),
            dbc.NavbarBrand('OilWeb', href='/inicio', className="m-2 fs-2")
        ], className='m-2 position-absolute start-0 col-4 border'),
        dbc.Col([
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem(page["name"], href=page["path"])
                    for page in dash.page_registry.values()
                    if page["name"] not in ('Login', 'Ajustes', 'Not found 404')
                ],
                nav=True,
                label="Mis fincas",
            )
        ], className='position-relative start col-3 border'),
        dbc.Col([
            dbc.Button(
                'Ajustes',
                id='button-ajustes',
                color="Primary",
                n_clicks=0,
                className="btn btn-secondary mb-2",
                href="/ajustes"
            )
        ], className='position-relative end col-3 border')
    ], className='justify-content-center'),
],
    color="green",
    dark=True,
    className="mb-5 rounded-bottom",
    fluid=True
)


navbar2 = dbc.Navbar([
    dbc.Container([
        dbc.Col([
                html.Img(src=app.get_asset_url('data/oliva.png'), width="100",
                     height="75", className="position-relative top"),
                dbc.NavbarBrand('OilWeb', href='/inicio', className="m-2 fs-2")
                ], className='border col-4'),
        dbc.Col([
                dbc.DropdownMenu([
                    dbc.DropdownMenuItem(page["name"], href=page["path"])
                    for page in dash.page_registry.values()
                    if page["name"] not in ('Login', 'Ajustes', 'Not found 404')
                ],
                    nav=True,
                    label="Mis fincas",
                )
                ], className='border'),
        dbc.Col([
                dbc.Button(
                    'Ajustes',
                    id='button-ajustes',
                    color="Primary",
                    n_clicks=0,
                    className="btn btn-secondary mb-2",
                    href="/ajustes"
                )
                ], className='border col-2')
    ])

],
    color="green",
    dark=True,
    className="mb-5 rounded-bottom col-12"
)


app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                navbar2,
                dash.page_container
            ], className='col-12 border border-5',)
        ], className='justify-content-center'
        )
    ],
    fluid=True,
    className="bg-white",
    style={'color': '#00ff00', 'background': 'green'}

)


if __name__ == "__main__":
    app.run(debug=True)
