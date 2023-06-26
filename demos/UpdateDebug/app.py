if True:
    import sys
    sys.path.append('../..')
    import dash
    import random
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '刷新数据',
            id='refresh-data'
        ),

        html.Div(
            id='column-container'
        )
    ],
    style={
        'padding': '100px'
    }
)


@app.callback(
    Output('column-container', 'children'),
    Input('refresh-data', 'n_clicks')
)
def refresh_column(n_clicks):

    return fact.AntdColumn(
        id='column-demo',
        data=[
            {
                'type': f'种类{i}',
                'value': random.randint(3, 11)
            }
            for i in range(1, 11)
        ],
        xField='type',
        yField='value',
        style={
            'height': 300
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
