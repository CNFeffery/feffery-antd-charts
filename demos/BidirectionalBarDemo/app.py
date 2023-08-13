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
        'country': '乌拉圭',
        '2016年耕地总面积': 13.4,
        '2016年转基因种植面积': 12.3,
    },
    {
        'country': '巴拉圭',
        '2016年耕地总面积': 14.4,
        '2016年转基因种植面积': 6.3,
    },
    {
        'country': '南非',
        '2016年耕地总面积': 18.4,
        '2016年转基因种植面积': 8.3,
    },
    {
        'country': '巴基斯坦',
        '2016年耕地总面积': 34.4,
        '2016年转基因种植面积': 13.8,
    },
    {
        'country': '阿根廷',
        '2016年耕地总面积': 44.4,
        '2016年转基因种植面积': 19.5,
    },
    {
        'country': '巴西',
        '2016年耕地总面积': 24.4,
        '2016年转基因种植面积': 18.8,
    },
    {
        'country': '加拿大',
        '2016年耕地总面积': 54.4,
        '2016年转基因种植面积': 24.7,
    },
    {
        'country': '中国',
        '2016年耕地总面积': 104.4,
        '2016年转基因种植面积': 5.3,
    },
    {
        'country': '美国',
        '2016年耕地总面积': 165.2,
        '2016年转基因种植面积': 72.9,
    },
]

app.layout = html.Div(
    [
        html.Div(
            fact.AntdBidirectionalBar(
                data=mock_data,
                xField='country',
                yField=['2016年耕地总面积', '2016年转基因种植面积'],
                xAxis={
                    'position': 'bottom'
                },
                tooltip={
                    'shared': True,
                    'showMarkers': False
                }
            ),
            style={
                'height': '400px'
            }
        )
    ],
    style={
        'padding': '50px 150px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
