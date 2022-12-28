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
    *[
    {
        'x': i,
        'y': np.random.rand(),
        'series': 'a'
    }
    for i in range(25)
],
*[
    {
        'x': i,
        'y': np.random.rand(),
        'series': 'b'
    }
    for i in range(25)
]
]

app.layout = html.Div(
    [
        html.Div(
            fact.AntdLine(
                id='line-demo',
                data=mock_data,
                xField='x',
                yField='y',
                seriesField='series'
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
    [Input('line-demo', 'recentlyTooltipChangeRecord'),
     Input('line-demo', 'recentlyPointClickRecord'),
     Input('line-demo', 'recentlyLegendInfo')]
)
def demo(recentlyTooltipChangeRecord,
         recentlyPointClickRecord,
         recentlyLegendInfo):

    return json.dumps(
        dict(
            recentlyTooltipChangeRecord=recentlyTooltipChangeRecord,
            recentlyPointClickRecord=recentlyPointClickRecord,
            recentlyLegendInfo=recentlyLegendInfo
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
