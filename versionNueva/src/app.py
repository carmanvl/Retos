import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html


app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.SANDSTONE])
server = app.server


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#556B2F",
}

# Navbar vertical o sidebar
sidebar = dbc.Container([
    html.Img(src=app.get_asset_url('data/OliWeb2.png'), width="200",
             height="200", className=""),
    # Nombre de la app con enlace al inicio, actualmente desactivado         
    # dbc.NavbarBrand('OliWeb', href='/inicio', className="fs-2", style={'color': '#FFFAF0'}),  
    html.Hr(),
    html.P("Información sobre las fincas",
           className="lead", style={'color': ' #FFFAF0'}),
    dbc.Nav(
        [
            dbc.NavLink("Añadir Finca", href="/inicio", active="exact",
                        className="p-2 text-center", style={'color': '#FFFAF0', 'background': '#556B2F'}),
            dbc.DropdownMenu([
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                # El for debe recorrer las fincas registradas en la BD, de momento recorre las páginas registradas
                for page in dash.page_registry.values()
                if page["name"] not in ('Login', 'Ajustes', 'Not found 404', 'Añadir nueva finca')
            ],
                nav=True,
                label="Mis fincas",
                className="p-2 text-center",
                color='#556B2F',
                toggle_style={"color": "#FFFAF0"},
                toggleClassName="",
            )
        ],
        vertical=True,
        pills=True,
    ),
    dbc.Nav([
            dbc.Button(
                'Ajustes',
                id='button-ajustes',
                n_clicks=0,
                className="btn position-absolute bottom-0 start-0 w-100",
                color='#808000',
                style={'color': '#FFFAF0', 'background': '#808000'},
                href="/ajustes",
            )
            ])
],
    style=SIDEBAR_STYLE,
    fluid=True
)

# Layout principal de la aplicación
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            sidebar
        ], className="col-2"),
        dbc.Col([
            html.Hr(className="p-2 bg-transparent"),
            dash.page_container
        ], className="col-10 me-auto")
    ])
],
    style={"background-color": "#FFFAF0"},
    # Foto de fondo, actualmente deshabilitada
    # style={'background-image': 'url(https://media.istockphoto.com/id/185636708/es/foto/olive_grove.jpg?s=612x612&w=0&k=20&c=QqaOsAVy5vJCcG5W3sAyqWfWsMTrS9ETUEnWC-FNTZ0=)',  'background-repeat':'no-repeat', 'background-attachment':'fixed', 'background-size':'cover'},
    fluid=True)


if __name__ == "__main__":
    app.run(debug=True)
