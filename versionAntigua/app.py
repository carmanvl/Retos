import dash
import dash_bootstrap_components as dbc
from . import navBar


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
server = app.server

app.layout = dbc.Container(
    [
        navBar.layout,
    ],
    fluid=False,
)

if __name__ == "__main__":
    app.run_server(debug=True)
