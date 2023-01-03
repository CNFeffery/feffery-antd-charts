if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            fact.AntdBullet(
                data=[
                    {
                        'title': '满意度',
                        'ranges': [100],
                        'measures': [80],
                        'target': 85,
                    },
                ],
                measureField='measures',
                rangeField='ranges',
                targetField='target',
                xField='title',
                color={
                    'range': '#f0efff',
                    'measure': '#5B8FF9',
                    'target': '#3D76DD',
                },
                xAxis={
                    'line': None
                },
                legend={
                    'custom': True,
                    'position': 'bottom',
                    'items': [
                        {
                            'value': '实际值',
                            'name': '实际值',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#5B8FF9',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '目标值',
                            'name': '目标值',
                            'marker': {
                                'symbol': 'line',
                                'style': {
                                    'stroke': '#3D76DD',
                                    'r': 5,
                                },
                            },
                        }
                    ]
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdBullet(
                data=[
                    {
                        'title': '满意度',
                        'ranges': [100],
                        'measures': [80],
                        'target': 85,
                    },
                ],
                measureField='measures',
                rangeField='ranges',
                targetField='target',
                xField='title',
                color={
                    'range': '#f0efff',
                    'measure': '#5B8FF9',
                    'target': '#3D76DD',
                },
                xAxis={
                    'line': None
                },
                yAxis=False,
                layout='vertical',
                label={
                    'measure': {
                        'position': 'middle',
                        'style': {
                            'fill': '#fff',
                        },
                    }
                },
                legend={
                    'custom': True,
                    'position': 'bottom',
                    'items': [
                        {
                            'value': '实际值',
                            'name': '实际值',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#5B8FF9',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '目标值',
                            'name': '目标值',
                            'marker': {
                                'symbol': 'line',
                                'style': {
                                    'stroke': '#3D76DD',
                                    'r': 5,
                                },
                            },
                        }
                    ]
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdBullet(
                data=[
                    {
                        'title': '满意度',
                        'ranges': [40, 70, 100],
                        'measures': [80],
                        'target': 85,
                    },
                ],
                measureField='measures',
                rangeField='ranges',
                targetField='target',
                xField='title',
                color={
                    'range': ['#FFbcb8', '#FFe0b0', '#bfeec8'],
                    'measure': '#5B8FF9',
                    'target': '#39a3f4',
                },
                xAxis={
                    'line': None
                },
                yAxis=False,
                label={
                    'target': True
                },
                legend={
                    'custom': True,
                    'position': 'bottom',
                    'items': [
                        {
                            'value': '差',
                            'name': '差',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#FFbcb8',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '良',
                            'name': '良',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#FFe0b0',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '优',
                            'name': '优',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#bfeec8',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '实际值',
                            'name': '实际值',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#5B8FF9',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '目标值',
                            'name': '目标值',
                            'marker': {
                                'symbol': 'line',
                                'style': {
                                    'stroke': '#39a3f4',
                                    'r': 5,
                                },
                            },
                        },
                    ]
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdBullet(
                data=[
                    {
                        'title': '满意度',
                        'ranges': [40, 70, 100],
                        'measures': [30, 50],
                        'target': 85,
                    },
                ],
                measureField='measures',
                rangeField='ranges',
                targetField='target',
                xField='title',
                color={
                    'range': ['#FFbcb8', '#FFe0b0', '#bfeec8'],
                    'measure': ['#5B8FF9', '#61DDAA'],
                    'target': '#39a3f4',
                },
                xAxis={
                    'line': None
                },
                yAxis=False,
                label={
                    'measure': {
                        'position': 'middle',
                        'style': {
                            'fill': '#fff',
                        },
                    },
                },
                tooltip={
                    'showMarkers': False,
                    'shared': True,
                },
                legend={
                    'custom': True,
                    'position': 'bottom',
                    'items': [
                        {
                            'value': '差',
                            'name': '差',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#FFbcb8',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '良',
                            'name': '良',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#FFe0b0',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '优',
                            'name': '优',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#bfeec8',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '第一季度',
                            'name': '第一季度',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#5B8FF9',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '第二季度',
                            'name': '第二季度',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': ' #61DDAA',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '目标值',
                            'name': '目标值',
                            'marker': {
                                'symbol': 'line',
                                'style': {
                                    'stroke': '#39a3f4',
                                    'r': 5,
                                },
                            },
                        },
                    ]
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdBullet(
                data=[
                    {
                        'title': '重庆',
                        'ranges': [30, 90, 120],
                        'measures': [65],
                        'target': 80,
                    },
                    {
                        'title': '杭州',
                        'ranges': [30, 90, 120],
                        'measures': [50],
                        'target': 100,
                    },
                    {
                        'title': '广州',
                        'ranges': [30, 90, 120],
                        'measures': [40],
                        'target': 85,
                    },
                    {
                        'title': '深圳',
                        'ranges': [30, 90, 120],
                        'measures': [50],
                        'target': 100,
                    },
                ],
                measureField='measures',
                rangeField='ranges',
                targetField='target',
                xField='title',
                color={
                    'range': ['#FFbcb8', '#FFe0b0', '#bfeec8'],
                    'measure': '#5B8FF9',
                    'target': '#39a3f4',
                },
                xAxis={
                    'line': None
                },
                yAxis=False,
                label={
                    'measure': {
                        'position': 'middle',
                        'style': {
                            'fill': '#fff',
                        },
                    },
                },
                tooltip={
                    'showMarkers': False,
                    'shared': True,
                },
                legend={
                    'custom': True,
                    'position': 'bottom',
                    'items': [
                        {
                            'value': '差',
                            'name': '差',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#FFbcb8',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '良',
                            'name': '良',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#FFe0b0',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '优',
                            'name': '优',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#bfeec8',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '实际值',
                            'name': '实际值',
                            'marker': {
                                'symbol': 'square',
                                'style': {
                                    'fill': '#5B8FF9',
                                    'r': 5,
                                },
                            },
                        },
                        {
                            'value': '目标值',
                            'name': '目标值',
                            'marker': {
                                'symbol': 'line',
                                'style': {
                                    'stroke': '#39a3f4',
                                    'r': 5,
                                },
                            },
                        },
                    ]
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
