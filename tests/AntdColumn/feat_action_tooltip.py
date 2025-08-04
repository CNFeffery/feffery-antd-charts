if True:
    import sys

    sys.path.append('../../')
    import dash
    import random
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Button(
                    '展示tooltip', id='show-tooltip'
                ),
                html.Button(
                    '隐藏tooltip', id='hide-tooltip'
                ),
            ]
        ),
        fact.AntdColumn(
            id='demo-column',
            data=[
                {
                    'date': f'2020-0{i}',
                    'y': random.randint(50, 100),
                }
                for i in range(1, 10)
            ],
            xField='date',
            yField='y',
        ),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('demo-column', 'action'),
    [
        Input('show-tooltip', 'n_clicks'),
        Input('hide-tooltip', 'n_clicks'),
    ],
    prevent_initial_call=True,
)
def tooltip_control(n_clicks_show, n_clicks_hide):
    if dash.ctx.triggered_id == 'show-tooltip':
        return {
            'type': 'tooltip:show',
            'tooltipPositionData': {
                'date': '2020-0{}'.format(
                    random.randint(2, 9)
                ),
                'y': random.randint(50, 100),
            },
        }
    elif dash.ctx.triggered_id == 'hide-tooltip':
        return {'type': 'tooltip:hide'}


if __name__ == '__main__':
    app.run(debug=True)
