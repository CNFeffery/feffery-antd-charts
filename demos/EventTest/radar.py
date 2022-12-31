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
        "item": "Design",
        "user": "a",
        "score": 70
    },
    {
        "item": "Design",
        "user": "b",
        "score": 30
    },
    {
        "item": "Development",
        "user": "a",
        "score": 60
    },
    {
        "item": "Development",
        "user": "b",
        "score": 70
    },
    {
        "item": "Marketing",
        "user": "a",
        "score": 50
    },
    {
        "item": "Marketing",
        "user": "b",
        "score": 60
    },
    {
        "item": "Users",
        "user": "a",
        "score": 40
    },
    {
        "item": "Users",
        "user": "b",
        "score": 50
    },
    {
        "item": "Test",
        "user": "a",
        "score": 60
    },
    {
        "item": "Test",
        "user": "b",
        "score": 70
    },
    {
        "item": "Language",
        "user": "a",
        "score": 70
    },
    {
        "item": "Language",
        "user": "b",
        "score": 50
    },
    {
        "item": "Technology",
        "user": "a",
        "score": 50
    },
    {
        "item": "Technology",
        "user": "b",
        "score": 40
    },
    {
        "item": "Support",
        "user": "a",
        "score": 30
    },
    {
        "item": "Support",
        "user": "b",
        "score": 40
    },
    {
        "item": "Sales",
        "user": "a",
        "score": 60
    },
    {
        "item": "Sales",
        "user": "b",
        "score": 40
    },
    {
        "item": "UX",
        "user": "a",
        "score": 50
    },
    {
        "item": "UX",
        "user": "b",
        "score": 60
    }
]


app.layout = html.Div(
    [
        html.Div(
            fact.AntdRadar(
                id='radar-demo',
                data=mock_data,
                xField='item',
                yField='score',
                seriesField='user',
                meta={
                    'score': {
                        'alias': '分数',
                        'min': 0,
                        'max': 80
                    },
                },
                xAxis={
                    'line': None,
                    'tickLine': None,
                    'grid': {
                        'line': {
                            'style': {
                                'lineDash': None,
                            },
                        },
                    },
                },
                yAxis={
                    'line': None,
                    'tickLine': None,
                    'grid': {
                        'line': {
                            'type': 'line',
                            'style': {
                                'lineDash': None,
                            },
                        },
                        'alternateColor': 'rgba(0, 0, 0, 0.04)',
                    },
                },
                area={}
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
    [Input('radar-demo', 'recentlyTooltipChangeRecord'),
     Input('radar-demo', 'recentlyAreaClickRecord'),
     Input('radar-demo', 'recentlyLegendInfo')]
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
