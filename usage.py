import feffery_antd_charts as fact
import requests
import demjson
from dash import html
import math
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
    [
        html.H3('AntdLine 折线图示例'),
        html.Div(
            fact.AntdLine(
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
                        'content': '各财年营收情况',
                        'style': {
                            'fill': '#fff',
                            'fontSize': 18,
                            'textAlign': 'center',
                            'textBaseline': 'middle'
                        },
                    }
                ],
                padding='auto',
                renderer='svg'
            ),
            style={
                'width': '1000px',
                'height': '600px',
                'padding': '30 0 0 0'
            }
        ),
        html.H3('AntdArea 面积图示例'),
        html.Div(
            fact.AntdArea(
                data=data,
                xField='x',
                yField='y',
                seriesField='series',
                isStack=True,
                isPercent=True,
                areaStyle={
                    'fillOpacity': 0.6
                },
                color=['#eccc68', '#ff7f50', '#ff6b81'],
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
                    }
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
                    }
                },
                label={
                    'offset': 20,
                    'position': 'top',
                    'formatter': {
                        'func': '''
                        (item) => {
                            if (item.x % 5 === 0){
                                return item.y.toFixed(2)
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
                                value: item.y.toFixed(2)
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
                        'content': '各财年营收情况',
                        'style': {
                            'fill': '#fff',
                            'fontSize': 18,
                            'textAlign': 'center',
                            'textBaseline': 'middle'
                        },
                    }
                ],
                padding='auto',
                renderer='svg'
            ),
            style={
                'width': '1000px',
                'height': '600px',
                'padding': '30 0 0 0'
            }
        ),
        html.H3('AntdBar 条形图示例'),
        html.Div(
            fact.AntdBar(
                data=requests.get(
                    'https://gw.alipayobjects.com/os/antfincdn/mor%26R5yBI9/stack-group-column.json').json(),
                xField='order_amt',
                yField='product_type',
                isGroup=True,
                isStack=True,
                seriesField='product_sub_type',
                groupField='sex',
                barBackground={
                    'style': {
                        'fill': 'rgba(0,0,0,0.1)'
                    }
                }
            ),
            style={
                'width': '1000px',
                'height': '600px',
                'padding': '30 0 0 0'
            }
        ),
        html.H3('AntdColumn 柱状图示例'),
        html.Div(
            fact.AntdColumn(
                data=requests.get(
                    'https://gw.alipayobjects.com/os/antfincdn/8elHX%26irfq/stack-column-data.json').json(),
                xField='year',
                yField='value',
                seriesField='type',
                isStack=True,
                label={
                    'position': 'middle'
                },
                columnStyle={
                    'radius': 5,
                    'cursor': 'pointer'
                }
            ),
            style={
                'width': '1000px',
                'height': '600px',
                'padding': '30 0 0 0'
            }
        ),
        html.H3('AntdPie 饼图示例'),
        html.Div(
            fact.AntdPie(
                data=demjson.decode('''[
    {
      type: '分类一',
      value: 27,
    },
    {
      type: '分类二',
      value: 25,
    },
    {
      type: '分类三',
      value: 18,
    },
    {
      type: '分类四',
      value: 15,
    },
    {
      type: '分类五',
      value: 10,
    },
    {
      type: '其他',
      value: 5,
    },
  ]'''),
                angleField='value',
                colorField='type',
                padding='auto',
                radius=0.9,
                innerRadius=0.6,
                pieStyle={
                    'lineWidth': 2
                },
                label={
                    'type': 'inner',
                    'content': '{value}',
                    'autoRotate': False,
                    'style': {
                        'fontSize': 16
                    }
                },
                statistic={
                    'title': {
                        'content': '总计'
                    },
                    'content': {
                        'rotate': math.pi,
                        'content': '9999',
                        'style': {
                            'color': 'red',
                            'fontSize': '50px'
                        }
                    }
                }
            ),
            style={
                'width': '1000px',
                'height': '600px',
                'padding': '30 0 0 0'
            }
        ),
        html.H3('AntdScatter 散点气泡图示例'),
        html.Div(
            fact.AntdScatter(
                data=demjson.decode('''[
    {
      city: '上海',
      搜索UV: 1.5,
      端DAU: 6,
      搜索DAU渗透率: 3,
    },
    {
      city: '台北',
      搜索UV: 2,
      端DAU: 5,
      搜索DAU渗透率: 13,
    },
    {
      city: '北京',
      搜索UV: 7,
      端DAU: 3.6,
      搜索DAU渗透率: 16,
    },
    {
      city: '济南',
      搜索UV: 5,
      端DAU: 5,
      搜索DAU渗透率: 16,
    },
    {
      city: '青岛',
      搜索UV: 2,
      端DAU: 1,
      搜索DAU渗透率: 19,
    },
    {
      city: '杭州',
      搜索UV: 7,
      端DAU: 2,
      搜索DAU渗透率: 90,
    },
    {
      city: '广东',
      搜索UV: 7.4,
      端DAU: 1.5,
      搜索DAU渗透率: 30,
    },
    {
      city: '无锡',
      搜索UV: 1,
      端DAU: 1,
      搜索DAU渗透率: 34,
    },
    {
      city: '重庆',
      搜索UV: 7,
      端DAU: 5,
      搜索DAU渗透率: 46,
    },
    {
      city: '成都',
      搜索UV: 3.4,
      端DAU: 2.3,
      搜索DAU渗透率: 49,
    },
    {
      city: '哈尔滨',
      搜索UV: 0.5,
      端DAU: 6.5,
      搜索DAU渗透率: 51,
    },
    {
      city: '内蒙古',
      搜索UV: 2.5,
      端DAU: 5,
      搜索DAU渗透率: 51,
    },
    {
      city: '云南',
      搜索UV: 1,
      端DAU: 5,
      搜索DAU渗透率: 53,
    },
    {
      city: '河北',
      搜索UV: 6,
      端DAU: 5,
      搜索DAU渗透率: 57,
    },
    {
      city: '陕西',
      搜索UV: 2,
      端DAU: 3,
      搜索DAU渗透率: 57,
    },
    {
      city: '苏州',
      搜索UV: 3,
      端DAU: 4.6,
      搜索DAU渗透率: 65,
    },
    {
      city: '四川',
      搜索UV: 6,
      端DAU: 7,
      搜索DAU渗透率: 68,
    },
    {
      city: '贵阳',
      搜索UV: 5,
      端DAU: 3.4,
      搜索DAU渗透率: 68,
    },
    {
      city: '台湾',
      搜索UV: 5,
      端DAU: 2,
      搜索DAU渗透率: 69,
    },
    {
      city: '哈尔滨',
      搜索UV: 2,
      端DAU: 7,
      搜索DAU渗透率: 78,
    },
    {
      city: '天津',
      搜索UV: 4.4,
      端DAU: 5,
      搜索DAU渗透率: 45,
    },
    {
      city: '长沙',
      搜索UV: 3.4,
      端DAU: 7,
      搜索DAU渗透率: 29,
    },
    {
      city: '沧州',
      搜索UV: 3,
      端DAU: 1,
      搜索DAU渗透率: 94,
    },
    {
      city: '宁波',
      搜索UV: 6,
      端DAU: 3,
      搜索DAU渗透率: 99,
    },
  ]'''),
                xField='搜索UV',
                yField='端DAU',
                appendPadding=16,
                sizeField='搜索DAU渗透率',
                size=[12, 30],
                shape='circle',
                pointStyle={
                    'fill': '#D6E3FD',
                    'fillOpacity': 0.6,
                    'stroke': '#6d9bf9'
                },
                label={
                    'formatter': {
                        'func': '''
                        (item) => {
                            return item.city
                        }'''
                    },
                    'offsetY': 12,
                    'style': {
                        'fontSize': 12,
                        'fill': 'rgba(0,0,0,0.85)'
                    }
                },
                yAxis={
                    'min': 0
                },
                annotations=[
                    {
                        'type': 'text',
                        'position': [4, 8],
                        'content': '搜索DAU渗透率',
                        'offsetY': -8,
                        'style': {
                            'fontSize': 12,
                            'textAlign': 'center'
                        }
                    }
                ],
                quadrant={
                    'xBaseline': 4,
                    'yBaseline': 4,
                    'lineStyle': {
                        'lineDash': [4, 2],
                        'lineWidth': 2
                    },
                    'regionStyle': demjson.decode('''[
        {
          fill: '#5bd8a6',
          fillOpacity: 0.1,
        },
        {
          fill: '#667796',
          fillOpacity: 0.1,
        },
        { fill: '#fff' },
        {
          fill: '#f7664e',
          fillOpacity: 0.1,
        },
      ]'''),
                    'labels': demjson.decode('''[
        {
          content: '热门市场',
          position: [7.2, 7],
          style: {
            fill: 'rgba(0,0,0, 0.85)',
            textAlign: 'start',
          },
        },
        {
          content: '潜力市场',
          position: [0.2, 7],
          style: {
            fill: 'rgba(0,0,0, 0.85)',
            textAlign: 'start',
          },
        },
        { content: '' },
        {
          content: '提频市场',
          position: [7.2, 1],
          style: {
            fill: 'rgba(0,0,0, 0.85)',
            textAlign: 'start',
          },
        },
      ]''')
                }
            ),
            style={
                'width': '1000px',
                'height': '600px',
                'padding': '30 0 0 0'
            }
        ),
        html.H3('AntdStock 股票图示例'),
        html.Div(
            fact.AntdStock(
                data=requests.get(
                    'https://gw.alipayobjects.com/os/antfincdn/qtQ9nYfYJe/stock-data.json'
                ).json(),
                # 指定日期字段
                xField='trade_date',
                # 指定开盘价字段, 收盘价字段, 最高价字段, 最低价字段
                yField=['open', 'close', 'high', 'low'],
                # 为个原始字段赋别名
                meta={
                    'vol': {'alias': '成交量'},
                    'open': {'alias': '开盘价'},
                    'close': {'alias': '收盘价'},
                    'high': {'alias': '最高价'},
                    'low': {'alias': '最低价'}
                },
                slider={}, # 开启缩略轴
                legend={
                    'itemName': {
                        'formatter': {
                            'func': '''
                            (name) => {
                                return name === 'up' ? '上涨' : '下跌'
                            }'''
                        }
                    }
                }
            ),
            style={
                'width': '1000px',
                'height': '600px',
                'padding': '30 0 0 0'
            }
        )
    ],
    style={
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'center',
        'alignItems': 'center',
        'paddingBottom': '100px'
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
