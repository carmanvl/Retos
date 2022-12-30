import dash
import dash_bootstrap_components as dbc
from dash import html
# from pages import login, registro     # Error: dash.register_page()` must be called after app instantiation


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SOLAR])
server = app.server


navBarI = dbc.Navbar(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
        ],
        nav=True,
        label="Mis fincas",
    ),
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [
        navBarI,
        # login.layout,
        dash.page_container,
        
    ],
    fluid=False,
)

if __name__ == "__main__":
    app.run_server(debug=True)