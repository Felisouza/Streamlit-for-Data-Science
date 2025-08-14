from dash import Dash, html
import dash_bootstrap_components as dbc

# Inicializa o app Dash com tema e ícones
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])

# Cria um card com valores
card = dbc.Card(
    dbc.CardBody([
        html.H1("Sales"),
        html.H3("$104.2M")
    ])
)

# Define o layout do app
app.layout = dbc.Container(card)

# Executa o servidor
if __name__ == "__main__":
    app.run(debug=False)