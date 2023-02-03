import dash
import dash_bootstrap_components as dbc
from dash import html


app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# page_reg = list(dash.page_registry.values())
#for x in page_reg:
#    print(x)
#    print('-------------------------------')

navbar = dbc.NavbarSimple(id='navBar',children=[
    dbc.Row([
        # Añadir columna con nombre y logo
        dbc.Col([ dbc.NavbarBrand('OilWeb', className='ml-2')]),
        dbc.Col ([html.Img(src=app.get_asset_url('data/oliva.png'), width="75", height="50")]),
        dbc.Col([
            dbc.DropdownMenu(  # De momento tiene todas las páginas, el objetivo es que tenga solo las fincas registradas
                [
                    dbc.DropdownMenuItem(page["name"], href=page["path"])
                    for page in dash.page_registry.values()
                ],
                nav=True,
                label="Mis fincas",
            )
        ]),
        dbc.Col([
            dbc.Button(
            'Ajustes',
            id='button-ajustes',
            color="Primary",
            n_clicks=0,
            className="btn btn-secondary mb-2",
            href="/ajustes"
        )
        ])
    ]),
],
    # brand="OilWeb",
    color="green",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [
        navbar,
        dash.page_container
    ],
    fluid=False,
)


if __name__ == "__main__":
    app.run(debug=True)
