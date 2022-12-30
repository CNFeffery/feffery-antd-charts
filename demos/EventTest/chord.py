if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

mock_data = [
    {
        'source': '北京',
        'target': '天津',
        'value': 30,
    },
    {
        'source': '北京',
        'target': '上海',
        'value': 80,
    },
    {
        'source': '北京',
        'target': '河北',
        'value': 46,
    },
    {
        'source': '北京',
        'target': '辽宁',
        'value': 49,
    },
    {
        'source': '北京',
        'target': '黑龙江',
        'value': 69,
    },
    {
        'source': '北京',
        'target': '吉林',
        'value': 19,
    },
    {
        'source': '天津',
        'target': '河北',
        'value': 62,
    },
    {
        'source': '天津',
        'target': '辽宁',
        'value': 82,
    },
    {
        'source': '天津',
        'target': '上海',
        'value': 16,
    },
    {
        'source': '上海',
        'target': '黑龙江',
        'value': 16,
    },
    {
        'source': '河北',
        'target': '黑龙江',
        'value': 76,
    },
    {
        'source': '河北',
        'target': '内蒙古',
        'value': 24,
    },
    {
        'source': '内蒙古',
        'target': '北京',
        'value': 32,
    },
]

app.layout = html.Div(
    [
        html.Div(
            fact.AntdChord(
                id='chord-demo',
                data=mock_data,
                sourceField='source',
                targetField='target',
                weightField='value'
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
    [Input('chord-demo', 'recentlyTooltipChangeRecord'),
     Input('chord-demo', 'recentlyAreaClickRecord')]
)
def demo(recentlyTooltipChangeRecord,
         recentlyAreaClickRecord):

    return json.dumps(
        dict(
            recentlyTooltipChangeRecord=recentlyTooltipChangeRecord,
            recentlyAreaClickRecord=recentlyAreaClickRecord
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
