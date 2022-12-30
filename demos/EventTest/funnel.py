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
        'stage': '简历筛选',
        'number': 253,
    },
    {
        'stage': '初试人数',
        'number': 151,
    },
    {
        'stage': '复试人数',
        'number': 113,
    },
    {
        'stage': '录取人数',
        'number': 87,
    },
    {
        'stage': '入职人数',
        'number': 59,
    },
]

app.layout = html.Div(
    [
        html.Div(
            fact.AntdFunnel(
                id='funnel-demo',
                data=mock_data,
                xField='stage',
                yField='number'
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
    [Input('funnel-demo', 'recentlyTooltipChangeRecord'),
     Input('funnel-demo', 'recentlyAreaClickRecord'),
     Input('funnel-demo', 'recentlyLegendInfo')]
)
def demo(recentlyTooltipChangeRecord,
         recentlyAreaClickRecord,
         recentlyLegendInfo):

    return json.dumps(
        dict(
            recentlyTooltipChangeRecord=recentlyTooltipChangeRecord,
            recentlyAreaClickRecord=recentlyAreaClickRecord,
            recentlyLegendInfo=recentlyLegendInfo
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
