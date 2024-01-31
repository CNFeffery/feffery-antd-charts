import dash
import random
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdPie(
            data=[
                {
                    'type': f'类型{i}',
                    'value': random.randint(0, 100)
                }
                for i in range(1, 6)
            ],
            colorField='type',
            angleField='value',
            interactions=[
                {
                    'type': 'element-active'
                },
                {
                    'type': 'element-single-selected'
                }
            ],
            state={
                'active': {
                    'style': {
                        'fillOpacity': 0.5,
                        'lineWidth': 0
                    }
                },
                'selected': {
                    'style': {
                        'stroke': 'red',
                        'lineWidth': 4
                    }
                }
            }
        )
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
