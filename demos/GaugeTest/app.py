if True:
    import sys
    sys.path.append('../..')
    import dash
    import math
    from dash import html
    import feffery_antd_charts as fact

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            fact.AntdGauge(
                percent=0.75,
                range={
                    'color': '#30BF78'
                },
                indicator={
                    'pointer': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                    'pin': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                },
                axis={
                    'subTickLine': {
                        'count': 3,
                    },
                    'label': {
                        'formatter': {
                            'func': '''(v) => Number(v) * 100'''
                        }
                    }
                },
                statistic={
                    'content': {
                        'formatter': {
                            'func': '({ percent }) => `Rate: ${(percent * 100).toFixed(0)}%`'
                        },
                        'style': {
                            'color': 'rgba(0,0,0,0.65)',
                            'fontSize': 48,
                        },
                    },
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdGauge(
                percent=0.75,
                radius=0.75,
                range={
                    'color': '#30BF78',
                    'width': 12,
                },
                indicator={
                    'pointer': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                    'pin': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                },
                statistic={
                    'content': {
                        'formatter': {
                            'func': '({ percent }) => `Rate: ${(percent * 100).toFixed(0)}%`'
                        },
                    },
                    'style': {
                        'fontSize': 60,
                    },
                },
                gaugeStyle={
                    'lineCap': 'round',
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdGauge(
                percent=0.75,
                range={
                    'color': 'l(0) 0:#B8E1FF 1:#3D76DD',
                },
                startAngle=math.pi,
                endAngle=2 * math.pi,
                indicator=None,
                statistic={
                    'title': {
                        'offsetY': -36,
                        'style': {
                            'fontSize': '36px',
                            'color': '#4B535E',
                        },
                        'formatter': {
                            'func': "() => '70%'"
                        },
                    },
                    'content': {
                        'style': {
                            'fontSize': '24px',
                            'lineHeight': '44px',
                            'color': '#4B535E',
                        },
                        'formatter': {
                            'func': "() => '加载进度'"
                        },
                    },
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdGauge(
                percent=0.75,
                range={
                    'ticks': [0, 1 / 3, 2 / 3, 1],
                    'color': ['#F4664A', '#FAAD14', '#30BF78'],
                },
                indicator={
                    'pointer': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                    'pin': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                },
                statistic={
                    'content': {
                        'style': {
                            'fontSize': '36px',
                            'lineHeight': '36px',
                        },
                    },
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdGauge(
                percent=0.75,
                range={
                    'ticks': [0, 1],
                    'color': ['l(0) 0:#F4664A 0.5:#FAAD14 1:#30BF78'],
                },
                indicator={
                    'pointer': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                    'pin': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                },
                statistic={
                    'content': {
                        'style': {
                            'fontSize': '36px',
                            'lineHeight': '36px',
                        },
                    },
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdGauge(
                percent=0.75,
                type='meter',
                innerRadius=0.75,
                range={
                    'ticks': [0, 1 / 3, 2 / 3, 1],
                    'color': ['#F4664A', '#FAAD14', '#30BF78'],
                },
                indicator={
                    'pointer': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                    'pin': {
                        'style': {
                            'stroke': '#D0D0D0',
                        },
                    },
                },
                statistic={
                    'content': {
                        'style': {
                            'fontSize': '36px',
                            'lineHeight': '36px',
                        },
                    },
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdGauge(
                percent=0.78,
                range={
                    'color': '#30BF78',
                },
                indicator={
                    'shape': 'cursor',
                    'pointer': {
                        'style': {
                            'stroke': '#D0D0D0',
                            'lineWidth': 1,
                            'fill': '#D0D0D0',
                        },
                    },
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdGauge(
                percent=0.78,
                range={
                    'color': '#30BF78',
                },
                indicator={
                    'shape': 'ring-cursor',
                    'pointer': {
                        'style': {
                            'stroke': '#D0D0D0',
                            'lineWidth': 1,
                            'fill': '#D0D0D0',
                        },
                    },
                    'pin': {
                        'style': {
                            'lineWidth': 2,
                            'stroke': '#D0D0D0',
                            'fill': '#D0D0D0',
                        },
                    }
                }
            ),
            style={
                'height': '400px'
            }
        ),

        html.Div(
            fact.AntdGauge(
                percent=0.78,
                range={
                    'color': '#30BF78',
                },
                indicator={
                    'shape': 'simple',
                    'pointer': {
                        'style': {
                            'fill': '#30BF78',
                        },
                    },
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
