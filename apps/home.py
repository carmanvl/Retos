import dash
import dash_bootstrap_components as dbc
from dash import html
# from app import app  # Mal importado 

navBarI = dbc.Navbar(
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
                    dbc.NavItem(dbc.DropdownMenu(children=[
                        dbc.DropdownMenuItem("Más fincas", header=True),
                        # Por cada finca de la lista de fincas
                        dbc.DropdownMenuItem("Otra finca", href="/otrafinca")
                    ],
                        nav=True,
                        in_navbar=True,
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

            ])
        ])
    ]
    ),
    color="light",
    dark=False
)


app.layout = dbc.Container(navBarI)


if __name__ == "__main__":
    app.run_server(debug=True)
