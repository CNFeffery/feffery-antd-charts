import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdArea(
            data=[{'x': i, 'y': i} for i in range(1, 11)],
            xField='x',
            yField='y',
            meta={
                'x': {
                    'type': 'linear',
                    'formatter': {
                        'func': '''e => "测试"'''
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
