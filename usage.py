import uuid
import feffery_antd_charts as fact
import requests
from dash.dependencies import Input, Output, State
import demjson3
from dash import html
import math
import json
import random
import dash


app = dash.Dash(__name__)


@app.callback(
    Output('antd-line-demo', 'data'),
    Input('antd-line-demo-button-update-data', 'n_clicks'),
    prevent_initial_call=True
)
def antd_line_update_data(n_clicks):

    return [
        {
            'x': str(i),
            'y': 10000 + 5000 * i + random.randint(0, 10000),
            'series': '系列1'
        }
        for i in range(0, 50)
    ]+[
        {
            'x': str(i),
            'y': 10000 + i ** 2 + random.randint(0, 10000),
            'series': '系列2'
        }
        for i in range(0, 50)
    ]+[
        {
            'x': str(i),
            'y': 10000 + i ** 3 + random.randint(0, 10000),
            'series': '系列3'
        }
        for i in range(0, 50)
    ]


@app.callback(
    Output('antd-line-demo', 'point'),
    Input('antd-line-demo-button-update-other-params', 'n_clicks'),
    prevent_initial_call=True
)
def antd_line_update_other_params(n_clicks):

    return {
        'style': {
            'func': f'(item) => {{ return {{ r: Number(item.x) % {random.randint(1, 5)} ? 0 : 5 }}; }}'
        }
    }


init_line_data = [
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
                fact.AntdSankey(
                    data=json.load(open('./samples-data/AntdSankey-alipay.json',
                                        encoding='utf-8')),
                    sourceField='source',
                    targetField='target',
                    weightField='value',
                    nodeWidthRatio=0.008,
                    nodePaddingRatio=0.03,
                    nodeDraggable=True
                ),
                style={
                    'height': '600px',
                    'padding': '25px'
                }
            ),

            html.Div(
                fact.AntdWordCloud(
                    data=json.load(open('./samples-data/AntdWordCloud-demo-douban.json',
                                        encoding='utf-8')),
                    wordField='title',
                    weightField='rate',
                    colorField='tag',
                    # legend={},
                    wordStyle={
                        'fontFamily': 'SimHei',
                        'fontSize': [12, 20],
                    },
                    imageMask='https://gw.alipayobjects.com/zos/antfincdn/Qw7Xbn76kM/53176454-747c-4f0a-a9e5-936aa66a0082.png'
                ),
                style={
                    'height': '600px'
                }
            ),

            html.Div(
                fact.AntdChord(
                    data=json.load(open('./samples-data/AntdChord-demo-pop-flow.json',
                                        encoding='utf-8')),
                    sourceField='source',
                    targetField='target',
                    weightField='value'
                ),
                style={
                    'height': '600px'
                }
            ),

            html.Div(
                fact.AntdSunburst(
                    data=json.load(open('./samples-data/AntdSunburst-demo-hierarchy.json',
                                        encoding='utf-8')),
                    label={
                        'layout': [
                            {
                                'type': 'limit-in-shape',
                            }
                        ]
                    },
                    hierarchyConfig={
                        'field': 'sum'
                    },
                    radius=1,
                    innerRadius=0.2,
                    drilldown={
                        'breadCrumb': {
                            'rootText': '起始节点',
                            'dividerText': '->'
                        }
                    }
                ),
                style={
                    'height': '600px'
                }
            ),


            html.Div(
                [
                    html.Button(
                        'data更新测试', id='antd-line-demo-button-update-data'),
                    html.Button(
                        '其他参数更新测试', id='antd-line-demo-button-update-other-params'),
                ]
            ),
            html.Div(
                [
                    html.Div(
                        html.Div(
                            [
                                html.Button(
                                    '刷新base64',
                                    id='antd-line-refresh-base64'
                                ),
                                fact.AntdLine(
                                    id='antd-line-demo',
                                    data=init_line_data,
                                    xField='x',
                                    yField='y',
                                    seriesField='series',
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
                                        'style': {
                                            'func': '(item) => { return { r: Number(item.x) % 4 ? 0 : 5 }; }'
                                        }
                                    }
                                )
                            ],
                            style={
                                'height': '100%',
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
                                     style={'height': '50%'})
                        ],
                        style={
                            'flex': '1',
                            'height': '100%'
                        }
                    ),
                    html.Div(
                        [
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
                    'height': '500px',
                    'border': '1px dashed grey',
                    'padding': '25px'
                }
            ),

            html.Div(
                [
                    html.Div(
                        html.Div(
                            fact.AntdPie(
                                data=[
                                    {
                                        'type': '分类一',
                                        'value': 27,
                                    },
                                    {
                                        'type': '分类二',
                                        'value': 25,
                                    },
                                    {
                                        'type': '分类三',
                                        'value': 18,
                                    },
                                    {
                                        'type': '分类四',
                                        'value': 15,
                                    },
                                    {
                                        'type': '分类五',
                                        'value': 10,
                                    },
                                    {
                                        'type': '其他',
                                        'value': 5,
                                    },
                                ],
                                angleField='value',
                                colorField='type',
                                radius=0.9,
                                label={
                                    'type': 'inner',
                                    'offset': '-30%',
                                    'style': {
                                        'fontSize': 36,
                                        'textAlign': 'center'
                                    },
                                    'formatter': {
                                        'func': '({ percent }) => `${(percent * 100).toFixed(0)}%`'
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
                        style={
                            'flex': '1',
                            'height': '100%'
                        }
                    )
                ],
                style={
                    'display': 'flex',
                    'height': '700px',
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
            #         'height': '700px',
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

    if recentlyTooltipChangeRecord:

        return json.dumps(recentlyTooltipChangeRecord, indent=4, ensure_ascii=False)

    return 'None'


@app.callback(
    Output('antd-line-demo', 'stringForBase64'),
    Input('antd-line-refresh-base64', 'n_clicks'),
    State('antd-line-demo', 'base64')
)
def refresh_line_base64(n_clicks, base64):

    if n_clicks:
        print('='*100)
        print(base64)
        return str(uuid.uuid4())

    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True, port=8008)
