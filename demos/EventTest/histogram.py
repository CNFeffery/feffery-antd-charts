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
        "value": 1.2
    },
    {
        "value": 3.4
    },
    {
        "value": 3.7
    },
    {
        "value": 4.3
    },
    {
        "value": 5.2
    },
    {
        "value": 5.8
    },
    {
        "value": 6.1
    },
    {
        "value": 6.5
    },
    {
        "value": 6.8
    },
    {
        "value": 7.1
    },
    {
        "value": 7.3
    },
    {
        "value": 7.7
    },
    {
        "value": 8.3
    },
    {
        "value": 8.6
    },
    {
        "value": 8.8
    },
    {
        "value": 9.1
    },
    {
        "value": 9.2
    },
    {
        "value": 9.4
    },
    {
        "value": 9.5
    },
    {
        "value": 9.7
    },
    {
        "value": 10.5
    },
    {
        "value": 10.7
    },
    {
        "value": 10.8
    },
    {
        "value": 11
    },
    {
        "value": 11
    },
    {
        "value": 11.1
    },
    {
        "value": 11.2
    },
    {
        "value": 11.3
    },
    {
        "value": 11.4
    },
    {
        "value": 11.4
    },
    {
        "value": 11.7
    },
    {
        "value": 12
    },
    {
        "value": 12.9
    },
    {
        "value": 12.9
    },
    {
        "value": 13.3
    },
    {
        "value": 13.7
    },
    {
        "value": 13.8
    },
    {
        "value": 13.9
    },
    {
        "value": 14
    },
    {
        "value": 14.2
    },
    {
        "value": 14.5
    },
    {
        "value": 15
    },
    {
        "value": 15.2
    },
    {
        "value": 15.6
    },
    {
        "value": 16
    },
    {
        "value": 16.3
    },
    {
        "value": 17.3
    },
    {
        "value": 17.5
    },
    {
        "value": 17.9
    },
    {
        "value": 18
    },
    {
        "value": 18
    },
    {
        "value": 20.6
    },
    {
        "value": 21
    },
    {
        "value": 23.4
    }
]

app.layout = html.Div(
    [
        html.Div(
            fact.AntdHistogram(
                id='histogram-demo',
                data=mock_data,
                binField='value',
                binWidth=2
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
    [Input('histogram-demo', 'recentlyTooltipChangeRecord'),
     Input('histogram-demo', 'recentlyAreaClickRecord'),
     Input('histogram-demo', 'recentlyLegendInfo')]
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
