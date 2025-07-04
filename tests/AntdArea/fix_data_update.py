if True:
    import sys

    sys.path.append('../../')
    import dash
    import random
    from dash import html
    import feffery_antd_charts as fact
    from feffery_dash_utils.style_utils import style
    from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Button('更新数据', id='update-data'),
                html.Button(
                    '下载图表', id='download-chart'
                ),
            ]
        ),
        fact.AntdArea(
            id='demo-area',
            data=[
                {
                    'date': f'2020-0{i}',
                    'y': random.randint(50, 100),
                }
                for i in range(1, 10)
            ],
            xField='date',
            yField='y',
            slider={},
            color='red',
        ),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('demo-area', 'data'),
    Output('demo-area', 'color'),
    Input('update-data', 'n_clicks'),
    State('demo-area', 'color'),
    prevent_initial_call=True,
)
def update_data(n_clicks, color):
    return [
        [
            {
                'date': f'2020-0{i}',
                'y': random.randint(50, 100),
            }
            for i in range(1, 10)
        ],
        (
            dash.no_update
            if n_clicks % 2 == 1
            else ('red' if color == 'blue' else 'blue')
        ),
    ]


@app.callback(
    Output('demo-area', 'downloadTrigger'),
    Input('download-chart', 'n_clicks'),
    prevent_initial_call=True,
)
def download_chart(n_clicks):
    return str(n_clicks)


if __name__ == '__main__':
    app.run(debug=True)
