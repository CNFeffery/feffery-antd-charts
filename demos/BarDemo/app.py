if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    import numpy as np
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

mock_data = [
    {
        'year': '1951 年',
        'value': 0.38,
    },
    {
        'year': '1952 年',
        'value': 0.52,
    },
    {
        'year': '1956 年',
        'value': 0.61,
    },
    {
        'year': '1957 年',
        'value': 0.145,
    },
    {
        'year': '1958 年',
        'value': 0.48,
    },
]

app.layout = html.Div(
    [
        html.Div(
            fact.AntdBar(
                id='bar-demo',
                data=mock_data,
                xField='value',
                yField='year',
                maxBarWidth=50,
                label={
                    'formatter': {
                        'func': '''(e) => `${(e.value * 100).toFixed(2)}%`'''
                    },
                    'position': 'right'
                }
            ),
            style={
                'height': '400px'
            }
        ),
        html.Pre(
            id='output'
        )
    ],
    style={
        'padding': '50px 150px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
