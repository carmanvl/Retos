import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback
from pages import ajustes


app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.SOLAR])
server = app.server

page_reg = list(dash.page_registry.values())
for x in page_reg:
    print(x)
    print('-------------------------------')

navbar = dbc.NavbarSimple(id='navBar',children=[
    dbc.Row([
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
    brand="OilWeb",
    color="primary",
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

# CALLBACKS
# Boton de ajustes enlace a ajustes.py


if __name__ == "__main__":
    app.run(debug=True)
