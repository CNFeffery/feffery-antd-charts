import dash
import random
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdArea(
            data=[
                {
                    'x': i,
                    'y': random.random()
                }
                for i in range(100)
            ],
            pixelRatio=3,
            xField='x',
            yField='y',
            smooth=True
        )
    ],
    style={
        'padding': '50px 100px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
