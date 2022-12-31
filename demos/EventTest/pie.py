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
        'type': '分类一',
        'value': 27,
    },
    {
        'type': '分类二',
        'value': 25,
    },
    {
        'type': '分类三',
        'value': 18,
    },
    {
        'type': '分类四',
        'value': 15,
    },
    {
        'type': '分类五',
        'value': 10,
    },
    {
        'type': '其他',
        'value': 5,
    },
]

app.layout = html.Div(
    [
        html.Div(
            fact.AntdPie(
                id='pie-demo',
                data=mock_data,
                angleField='value',
                colorField='type',
                radius=0.75,
                label={
                    'type': 'spider',
                    'content': '{name}\n{percentage}',
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


@app.callback(
    Output('output', 'children'),
    [Input('pie-demo', 'recentlyTooltipChangeRecord'),
     Input('pie-demo', 'recentlySectorClickRecord'),
     Input('pie-demo', 'recentlyLegendInfo')]
)
def demo(recentlyTooltipChangeRecord,
         recentlySectorClickRecord,
         recentlyLegendInfo):

    return json.dumps(
        dict(
            recentlyTooltipChangeRecord=recentlyTooltipChangeRecord,
            recentlySectorClickRecord=recentlySectorClickRecord,
            recentlyLegendInfo=recentlyLegendInfo
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
