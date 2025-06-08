if True:
    import sys

    sys.path.append('../../')
    import dash
    import json
    import random
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
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
        ),
        html.Pre(id='output'),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('output', 'children'),
    Input('demo-area', 'recentlySliderRange'),
    prevent_initial_call=True,
)
def show_slider_event(recentlySliderRange):
    return json.dumps(
        recentlySliderRange, indent=4, ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
