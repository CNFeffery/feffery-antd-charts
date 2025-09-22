if True:
    import sys

    sys.path.append('../../')
    import json
    import dash
    import random
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fact.AntdDualAxes(
            id='chart',
            data=[
                # 左轴数据
                [
                    {
                        'date': f'2020-0{i}',
                        'y1': random.randint(50, 100),
                    }
                    for i in range(1, 10)
                ],
                # 右轴数据
                [
                    {
                        'date': f'2020-0{i}',
                        'y2': random.randint(100, 1000),
                    }
                    for i in range(1, 10)
                ],
            ],
            xField='date',
            yField=['y1', 'y2'],
            geometryOptions=[
                {'geometry': 'line'},
                {'geometry': 'line'},
            ],
        ),
        html.Pre(id='event-output'),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('event-output', 'children'),
    Input('chart', 'recentlyClickRecord'),
)
def show_event(recentlyClickRecord):
    return json.dumps(
        {'recentlyClickRecord': recentlyClickRecord},
        indent=4,
        ensure_ascii=False,
    )


if __name__ == '__main__':
    app.run(debug=True)
