if True:
    import sys
    sys.path.append('../..')
    import dash
    import math
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

data = [
    {"type": "分类一", "value": 27},
    {"type": "分类二", "value": 25},
    {"type": "分类三", "value": 18},
    {"type": "分类四", "value": 15},
    {"type": "分类五", "value": 10},
    {"type": "分类六", "value": 10},
    {"type": "分类七", "value": 10},
    {"type": "分类八", "value": 20},
    {"type": "分类九", "value": 20},
    {"type": "其他", "value": 5}
]

app.layout = html.Div(
    [
        fact.AntdPie(
            appendPadding=10,
            data=data,
            angleField='value',
            colorField='type',
            radius=1,
            startAngle=math.pi,
            endAngle=math.pi * 1.5,
            label={
                'type': 'inner',
                'offset': '-8%',
                'content': '{name}',
                'style': {
                    'fontSize': 18,
                },
            },
            pieStyle={
                'lineWidth': 0,
            },
            legend={
                'position': 'bottom',
                'maxWidth': 400,
                'flipPage': False
            }
        )
    ],
    style={
        'padding': '25px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
