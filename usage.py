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
                                data=requests.get(
                                    'https://gw.alipayobjects.com/os/bmw-prod/55424a73-7cb8-4f79-b60d-3ab627ac5698.json').json(),
                                xField='year',
                                yField='value',
                                seriesField='category',
                                color=[
                                    '#5B8FF9',
                                    '#5AD8A6',
                                    '#5D7092',
                                    '#F6BD16',
                                    '#E8684A',
                                    '#6DC8EC',
                                    '#9270CA',
                                    '#FF9D4D',
                                    '#269A99',
                                    '#FF99C3',
                                ],
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
                                point={
                                    'shape': {
                                        'func': """( {category} ) => {return {category} === 'Gas fuel' ? 'square' : 'circle';}"""
                                    },
                                    'style': {
                                        'func': '''
                                                                        ( {year} ) => {
                                        return {
                                          r: Number(year) % 4 ? 0 : 5, // 4 个数据示一个点标记
                                        };
                                      }
                                                                        '''
                                    }
                                }
                            ),
                            style={
                                'height': '100%',
                                # 'width': '800px',
                                'padding': '25px'
                            }
                        ),
                        style={
                            'flex': '2',
                            'height': '100%'
                        }
                    ),

                    html.Div(
                        [
                            html.Pre(id='antd-line-output1',
                                     style={'height': '50%'}),
                            html.Pre(id='antd-line-output2',
                                     style={'height': '50%'})
                        ],
                        style={
                            'flex': '1',
                            'height': '100%'
                        }
                    )
                ],
                style={
                    'display': 'flex',
                    'height': '1000px',
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
    )
)


@app.callback(
    Output('antd-line-output1', 'children'),
    Input('antd-line-demo', 'recentlyPointClickRecord')
)
def antd_line_callback_demo1(recentlyPointClickRecord):

    print(recentlyPointClickRecord)

    if recentlyPointClickRecord:

        return json.dumps(recentlyPointClickRecord, indent=4, ensure_ascii=False)

    return 'None'


@app.callback(
    Output('antd-line-output2', 'children'),
    Input('antd-line-demo', 'recentlyTooltipChangeRecord')
)
def antd_line_callback_demo2(recentlyTooltipChangeRecord):

    print(recentlyTooltipChangeRecord)

    if recentlyTooltipChangeRecord:

        return json.dumps(recentlyTooltipChangeRecord, indent=4, ensure_ascii=False)

    return 'None'


if __name__ == '__main__':
    app.run_server(debug=True, port=8008)
