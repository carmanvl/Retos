
# PAGINA DE INICIO POST LOGIN

import dash
import dash_bootstrap_components as dbc
import dash_labs as dl
from dash import html
from pages import anadirFinca

app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[
                dbc.themes.BOOTSTRAP])
server = app.server

for x in dash.page_registry.values():
    print(x)

navBarI = dbc.NavbarSimple(
    dbc.Container([
        dbc.Row([
            dbc.Col([
                #html.Img(src=app.get_asset_url('logo.jpg'), height="30px"),
                dbc.NavbarBrand("OilWeb", className="ms-2")
            ],
                width={"size": "auto"}
            )
        ],
            align="center",
            className="g-0"
        ),

        dbc.Row([
            dbc.Col([
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Añadir nueva finca", href="/")),
                    # Por cada finca de la lista de fincas
                    dbc.NavItem(dbc.NavLink("Finca i", href="/fincai")),
                    #
                    dbc.NavItem(
                        dbc.DropdownMenu(children=[
                            # Por cada finca de la lista de fincas
                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if page["module"] != "pages.not_found_404"
                        ],
                            nav=True,
                            #in_navbar=True,
                            label="Mis fincas"))
                ],
                    navbar=True)
            ],
                width={"size": "auto"})
        ],
            align="center"
        ),
        dbc.Row([
            dbc.Col([
                # BOTON DE AJUSTES
            ])
        ])
    ]
    ),
    color="light",
    dark=False
)


app.layout = dbc.Container([navBarI, dl.plugins.page_container],
                           fluid=True)


if __name__ == "__main__":
    app.run_server(debug=True)
