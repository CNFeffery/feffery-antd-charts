if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_antd_charts as fact
    from palettable.colorbrewer.sequential import Blues_7_r

demo_data = [
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
demo_data = [{**item, 'opacity': 1 - 0.1*i}
             for i, item in enumerate(demo_data)]


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            fact.AntdFunnel(
                data=demo_data,
                xField='stage',
                yField='number',
                legend=False,
                label={
                    'formatter': {
                        'func': '''e => e.stage'''
                    }
                },
                conversionTag=False,
                tooltip=False,
                theme={
                    'colors10': Blues_7_r.hex_colors
                }
            ),
            style={
                'width': 400,
                'height': 175
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
