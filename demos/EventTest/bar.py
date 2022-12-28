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
        'value': 38,
    },
    {
        'year': '1952 年',
        'value': 52,
    },
    {
        'year': '1956 年',
        'value': 61,
    },
    {
        'year': '1957 年',
        'value': 145,
    },
    {
        'year': '1958 年',
        'value': 48,
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
                seriesField='year'
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
    [Input('bar-demo', 'recentlyTooltipChangeRecord'),
     Input('bar-demo', 'recentlyBarClickRecord'),
     Input('bar-demo', 'recentlyLegendInfo')]
)
def demo(recentlyTooltipChangeRecord,
         recentlyBarClickRecord,
         recentlyLegendInfo):

    return json.dumps(
        dict(
            recentlyTooltipChangeRecord=recentlyTooltipChangeRecord,
            recentlyBarClickRecord=recentlyBarClickRecord,
            recentlyLegendInfo=recentlyLegendInfo
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
