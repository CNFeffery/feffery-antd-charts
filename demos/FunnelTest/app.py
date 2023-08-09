if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

demo_data = dict(
    demo1=[
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
)


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H3('迷你漏斗图'),
        html.Div(
            fact.AntdFunnel(
                data=demo_data.get('demo1'),
                xField='stage',
                yField='number',
                legend=False,
                label=False,
                conversionTag=False,
                tooltip=False
            ),
            style={
                'height': 200,
                'width': 300,
                'border': '1px solid #dbdbda'
            }
        )
    ],
    style={
        'margin': '0 auto',
        'padding': '50px',
        'paddingBottom': '50px',
    }
)


if __name__ == '__main__':
    app.run(debug=True)
