import dash
from dash import html

app = dash.Dash(__name__, compress=True)

app.layout = html.Div()

if __name__ == '__main__':
    app.run(debug=True)
