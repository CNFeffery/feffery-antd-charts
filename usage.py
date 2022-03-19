import feffery_antd_charts as fact
import requests
from dash.dependencies import Input, Output
import demjson3
from dash import html
import math
import json
import dash


app = dash.Dash(__name__)


data = [
    {
        'x': str(i),
        'y': 10000 + 5000 * i,
        'series': '系列1'
    }
    for i in range(0, 50)
]+[
    {
        'x': str(i),
        'y': 10000 + i ** 2,
        'series': '系列2'
    }
    for i in range(0, 50)
]+[
    {
        'x': str(i),
        'y': 10000 + i ** 3,
        'series': '系列3'
    }
    for i in range(0, 50)
]

app.layout = html.Div(
    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        html.Div(
                            fact.AntdLine(
                                id='antd-line-demo',
                                data=data,
                                xField='x',
                                yField='y',
                                seriesField='series',
                                smooth=True,
                                isStack=False,
                                color={
                                    'func': '''
                            (ref) => {
                                if (ref.series === '系列1') {
                                    return '#eccc68'
                                } else if (ref.series == '系列2') {
                                    return '#ff7f50'
                                }
                                return '#ff6b81'
                            }
                            '''
                                },
                                lineStyle={
                                    'func': '''
                            (ref) => {
                                if (ref.series === '系列1') {
                                    return {
                                        lineDash: [5, 5],
                                        cursor: 'pointer'
                                    }
                                } else if (ref.series == '系列2') {
                                    return {
                                        lineDash: [10, 5],
                                        cursor: 'pointer'
                                    }
                                }
                                return {
                                    lineDash: [0, 0],
                                    cursor: 'pointer'
                                }
                            }'''
                                },
                                point={
                                    'shape': {
                                        'func': '''
                            (ref) => {
                                if (ref.series === '系列1') {
                                    return 'circle'
                                } else if (ref.series == '系列2') {
                                    return 'diamond'
                                }
                                return 'square'
                            }'''
                                    },
                                    'style': {
                                        'r': 4,
                                        'lineWidth': 1,
                                        'fillOpacity': 1,
                                        'cursor': 'pointer'
                                    },
                                    'color': ['#eccc68', '#ff7f50', '#ff6b81']
                                },
                                xAxis={
                                    'title': {
                                        'text': 'x轴测试',
                                        'position': 'center',
                                        'style': {
                                                'fontSize': 18,
                                                'fontFamily': 'SimHei'
                                        }
                                    },
                                    'label': {
                                        'rotate': 3 * math.pi / 2,
                                        'offsetX': -8,
                                        'offsetY': -8,
                                        'style': {
                                            'fontFamily': 'Times New Roman',
                                            'fontSize': 16
                                        },
                                        'formatter': {
                                            'func': '''
                                    (value) => {
                                        return value < 10 ? `0${value}` : value
                                    }'''
                                        }
                                    },
                                    'line': {
                                        'style': {
                                            'opacity': 0
                                        }
                                    },
                                    'grid': {
                                        'line': {
                                            'style': {
                                                'stroke': 'black',
                                                'lineDash': [5, 5]
                                            }
                                        },
                                        'alternateColor': '#f1f2f6',
                                        'alignTick': False
                                    },
                                    'tickLine': {
                                        'length': 5
                                    },
                                    'tickInterval': 5
                                },
                                yAxis={
                                    'title': {
                                        'text': 'y轴测试',
                                        'style': {
                                                'fontSize': 18,
                                                'fontFamily': 'SimHei'
                                        }
                                    },
                                    'label': {
                                        'style': {
                                            'fontFamily': 'Times New Roman',
                                            'fontSize': 16
                                        }
                                    },
                                    'line': {
                                        'style': {
                                            'opacity': 0
                                        }
                                    },
                                    'grid': {
                                        'alignTick': False
                                    },
                                    'tickLine': {
                                        'length': 5
                                    },
                                    'tickInterval': 20000
                                },
                                legend={
                                    'position': 'right',
                                    'offsetX': -10,
                                    'itemHeight': 20,
                                    'title': {
                                        'text': '图例标题测试',
                                        'style': {
                                                'fontSize': 16
                                        }
                                    },
                                    'selected': {
                                        '系列1': False
                                    }
                                },
                                label={
                                    'offset': 20,
                                    'position': 'top',
                                    'formatter': {
                                        'func': '''
                                (item) => {
                                    if (item.x % 5 === 0){
                                        return item.y + '万'
                                    }
                                }'''
                                    }
                                },
                                tooltip={
                                    'formatter': {
                                        'func': '''
                                (item) => {
                                    return {
                                        name: `${item.series}于第${item.x}财年营收`,
                                        value: `${item.y / 10000}亿元`
                                    }
                                }'''
                                    },
                                    'enterable': True,
                                    'showTitle': True,
                                    'title': '营收情况',
                                    'marker': {
                                        'r': 5
                                    },
                                    'domStyles': {
                                        'g2-tooltip-title': {
                                            'font-size': '18px'
                                        },
                                        'g2-tooltip': {
                                            'background-color': 'rgba(255, 255, 255, 0.8)'
                                        }
                                    }
                                },
                                slider={
                                    'start': 0,
                                    'end': 1
                                },
                                annotations=[
                                    {
                                        'type': 'region',
                                        'start': ['0%', '0%'],
                                        'end': ['20%', '7.5%'],
                                        'top': True,
                                        'style': {
                                            'fill': '#1890ff',
                                            'fillOpacity': 1,
                                            'opacity': 0.6,
                                        },
                                    },
                                    {
                                        'type': 'text',
                                        'position': ['10%', '3.5%'],
                                        'content': 'AntdLine示例',
                                        'style': {
                                                'fill': '#fff',
                                                'fontSize': 18,
                                                'textAlign': 'center',
                                                'textBaseline': 'middle'
                                        },
                                    }
                                ],
                                padding='auto',
                                renderer='svg',
                            ),
                            style={
                                'height': '100%',
                                'width': '800px',
                                'padding': '25px'
                            }
                        ),
                        style={
                            'flex': 'none',
                            'height': '100%'
                        }
                    ),

                    html.Div(
                        html.Pre(id='antd-line-output'),
                        style={
                            'flex': 'auto',
                            'height': '100%'
                        }
                    )
                ],
                style={
                    'display': 'flex',
                    'height': '600px',
                    'border': '1px dashed grey',
                    'padding': '25px'
                }
            ),

            # html.H3('AntdStock 股票图示例', id='AntdStock-demo'),
            # html.Div(
            #     fact.AntdStock(
            #         data=requests.get(
            #             'https://gw.alipayobjects.com/os/antfincdn/qtQ9nYfYJe/stock-data.json'
            #         ).json(),
            #         # 指定日期字段
            #         xField='trade_date',
            #         # 指定开盘价字段, 收盘价字段, 最高价字段, 最低价字段
            #         yField=['open', 'close', 'high', 'low'],
            #         # 为个原始字段赋别名
            #         meta={
            #             'vol': {'alias': '成交量'},
            #             'open': {'alias': '开盘价'},
            #             'close': {'alias': '收盘价'},
            #             'high': {'alias': '最高价'},
            #             'low': {'alias': '最低价'}
            #         },
            #         slider={},  # 开启缩略轴
            #         legend={
            #             'itemName': {
            #                 'formatter': {
            #                     'func': '''
            #                 (name) => {
            #                     return name === 'up' ? '上涨' : '下跌'
            #                 }'''
            #                 }
            #             }
            #         }
            #     ),
            #     style={
            #         'width': '1000px',
            #         'height': '600px',
            #         'padding': '30 0 0 0'
            #     }
            # )
        ]
    ),
    style={
        'padding': '100px'
    }
)


@app.callback(
    Output('antd-line-output', 'children'),
    Input('antd-line-demo', 'recentlyPlotClickRecord')
)
def antd_line_callback_demo(recentlyPlotClickRecord):

    print(recentlyPlotClickRecord)

    if recentlyPlotClickRecord:

        return json.dumps(recentlyPlotClickRecord, indent=4, ensure_ascii=False)

    return 'None'


if __name__ == '__main__':
    app.run_server(debug=True, port=8008)
