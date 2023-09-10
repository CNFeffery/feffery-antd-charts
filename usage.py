import math
import dash
import random
import demjson3
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

mock_xy = [
    {
        'x': i,
        'y': round(random.uniform(0, 1), 2)
    }
    for i in range(15)
]

app.layout = html.Div(
    [
        # 异步资源加载测试
        html.Div(
            fact.AntdDecompositionTree(
                data={
                    'id': 'A0',
                    'value': {'title': '订单金额', 'items': [{'text': '3031万'}]},
                    'children': [{'id': 'A1',
                                  'value': {'title': '华南',
                                            'items': [{'text': '1152万'}, {'text': '占比', 'value': '30%'}]},
                                  'children': [{'id': 'A11',
                                                'value': {'title': '广东',
                                                          'items': [{'text': '1152万'}, {'text': '占比', 'value': '30%'}]}},
                                               {'id': 'A12',
                                                'value': {'title': '广西',
                                                          'items': [{'text': '1152万'}, {'text': '占比', 'value': '30%'}]}},
                                               {'id': 'A13',
                                                'value': {'title': '海南',
                                                          'items': [{'text': '1152万'}, {'text': '占比', 'value': '30%'}]}}]},
                                 {'id': 'A2',
                                  'value': {'title': '华北',
                                            'items': [{'text': '595万'}, {'text': '占比-非常非常非常非常非常长', 'value': '30%'}]}}]
                },
                autoFit=False,
                nodeCfg={
                    'autoWidth': True,
                    'items': {
                        'layout': 'follow'
                    },
                },
                layout={
                    'direction': 'LR',
                    'type': 'indented',
                    'dropCap': False,
                    'indent': 300
                },
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node']
            ),
            style={
                'height': '500px',
                'border': '1px solid #dbdbda'
            }
        ),
        html.Div(
            fact.AntdFundFlow(
                data={'nodes': [{'id': '1',
                      'value': {'text': 'Company1'}},
                    {'id': '2', 'value': {'text': 'Company2'}},
                    {'id': '3', 'value': {'text': 'Company3'}},
                    {'id': '4', 'value': {'text': 'Company4'}},
                    {'id': '5', 'value': {'text': 'Company5'}},
                    {'id': '6', 'value': {'text': 'Company6'}},
                    {'id': '7', 'value': {'text': 'Company7'}},
                    {'id': '8', 'value': {'text': 'Company8'}},
                    {'id': '9', 'value': {'text': 'Company9'}}],
                    'edges': [{'source': '1',
                               'target': '2',
                               'value': {'text': '100,000 Yuan', 'subText': '2019-08-03'}},
                              {'source': '1',
                               'target': '3',
                               'value': {'text': '100,000 Yuan', 'subText': '2019-08-03'}},
                              {'source': '2',
                               'target': '5',
                               'value': {'text': '100,000 Yuan', 'subText': '2019-08-03'}},
                              {'source': '5',
                               'target': '6',
                               'value': {'text': '100,000 Yuan', 'subText': '2019-08-03'}},
                              {'source': '3',
                               'target': '4',
                               'value': {'text': '100,000 Yuan', 'subText': '2019-08-03'}},
                              {'source': '4',
                               'target': '7',
                               'value': {'text': '100,000 Yuan', 'subText': '2019-08-03'}},
                              {'source': '1',
                               'target': '8',
                               'value': {'text': '100,000 Yuan', 'subText': '2019-08-03'}},
                              {'source': '1',
                               'target': '9',
                               'value': {'text': '100,000 Yuan', 'subText': '2019-08-03'}}]},
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node']
            ),
            style={
                'height': '500px',
                'border': '1px solid #dbdbda'
            }
        ),
        fact.AntdArea(
            data=mock_xy,
            xField='x',
            yField='y',
            smooth=True
        ),
        fact.AntdBar(
            data=mock_xy,
            xField='y',
            yField='x'
        ),
        html.Div(
            fact.AntdBidirectionalBar(
                data=[
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
                ],
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
        ),
        fact.AntdBox(
            data=[
                {
                    'Species': 'I. setosa',
                    'type': 'SepalLength',
                    'value': 5.1,
                    '_bin': [4.3, 4.8, 5, 5.2, 5.8],
                },
                {
                    'Species': 'I. setosa',
                    'type': 'SepalWidth',
                    'value': 3.5,
                    '_bin': [2.3, 3.2, 3.4, 3.7, 4.4],
                },
                {
                    'Species': 'I. setosa',
                    'type': 'PetalLength',
                    'value': 1.4,
                    '_bin': [1, 1.4, 1.5, 1.6, 1.9],
                },
                {
                    'Species': 'I. setosa',
                    'type': 'PetalWidth',
                    'value': 0.2,
                    '_bin': [0.1, 0.2, 0.2, 0.3, 0.6],
                },
                {
                    'Species': 'I. versicolor',
                    'type': 'SepalLength',
                    'value': 7,
                    '_bin': [4.9, 5.6, 5.9, 6.3, 7],
                },
                {
                    'Species': 'I. versicolor',
                    'type': 'SepalWidth',
                    'value': 3.2,
                    '_bin': [2, 2.5, 2.8, 3, 3.4],
                },
                {
                    'Species': 'I. versicolor',
                    'type': 'PetalLength',
                    'value': 4.7,
                    '_bin': [3, 4, 4.35, 4.6, 5.1],
                },
                {
                    'Species': 'I. versicolor',
                    'type': 'PetalWidth',
                    'value': 1.4,
                    '_bin': [1, 1.2, 1.3, 1.5, 1.8],
                },
                {
                    'Species': 'I. virginica',
                    'type': 'SepalLength',
                    'value': 6.3,
                    '_bin': [4.9, 6.2, 6.5, 6.9, 7.9],
                },
                {
                    'Species': 'I. virginica',
                    'type': 'SepalWidth',
                    'value': 3.3,
                    '_bin': [2.2, 2.8, 3, 3.2, 3.8],
                },
                {
                    'Species': 'I. virginica',
                    'type': 'PetalLength',
                    'value': 6,
                    '_bin': [4.5, 5.1, 5.55, 5.9, 6.9],
                },
                {
                    'Species': 'I. virginica',
                    'type': 'PetalWidth',
                    'value': 2.5,
                    '_bin': [1.4, 1.8, 2, 2.3, 2.5],
                }
            ],
            xField='type',
            yField='_bin',
            groupField='Species'
        ),
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
        fact.AntdChord(
            data=[
                {
                    'source': '北京',
                    'target': '天津',
                    'value': 30,
                },
                {
                    'source': '北京',
                    'target': '上海',
                    'value': 80,
                },
                {
                    'source': '北京',
                    'target': '河北',
                    'value': 46,
                },
                {
                    'source': '北京',
                    'target': '辽宁',
                    'value': 49,
                },
                {
                    'source': '北京',
                    'target': '黑龙江',
                    'value': 69,
                },
                {
                    'source': '北京',
                    'target': '吉林',
                    'value': 19,
                },
                {
                    'source': '天津',
                    'target': '河北',
                    'value': 62,
                },
                {
                    'source': '天津',
                    'target': '辽宁',
                    'value': 82,
                },
                {
                    'source': '天津',
                    'target': '上海',
                    'value': 16,
                },
                {
                    'source': '上海',
                    'target': '黑龙江',
                    'value': 16,
                },
                {
                    'source': '河北',
                    'target': '黑龙江',
                    'value': 76,
                },
                {
                    'source': '河北',
                    'target': '内蒙古',
                    'value': 24,
                },
                {
                    'source': '内蒙古',
                    'target': '北京',
                    'value': 32,
                },
            ],
            sourceField='source',
            targetField='target',
            weightField='value'
        ),
        fact.AntdColumn(
            data=mock_xy,
            xField='x',
            yField='y'
        ),
        fact.AntdDualAxes(
            data=[
                demjson3.decode('''
[
    {
      year: '1991',
      value: 3,
      count: 10,
    },
    {
      year: '1992',
      value: 4,
      count: 4,
    },
    {
      year: '1993',
      value: 3.5,
      count: 5,
    },
    {
      year: '1994',
      value: 5,
      count: 5,
    },
    {
      year: '1995',
      value: 4.9,
      count: 4.9,
    },
    {
      year: '1996',
      value: 6,
      count: 35,
    },
    {
      year: '1997',
      value: 7,
      count: 7,
    },
    {
      year: '1998',
      value: 9,
      count: 1,
    },
    {
      year: '1999',
      value: 13,
      count: 20,
    },
]
''')
            ] * 2,
            xField='year',
            yField=['value', 'count'],
            geometryOptions=[
                {
                    'geometry': 'line',
                    'color': '#5B8FF9',
                    'smooth': True
                },
                {
                    'geometry': 'line',
                    'color': '#5AD8A6',
                    'smooth': True
                }
            ],
            tooltip={
                'customItems': {
                    'func': '''(e) => {
                            for (let i = 0;i < e.length;i++) {
                              e[i].value = `${e[i].value}测试`
                            }
                            return e
                          }'''
                }
            },
            slider={}
        ),
        fact.AntdFunnel(
            data=[
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
            ],
            xField='stage',
            yField='number'
        ),
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
        fact.AntdHistogram(
            data=[
                {
                    "value": 1.2
                },
                {
                    "value": 3.4
                },
                {
                    "value": 3.7
                },
                {
                    "value": 4.3
                },
                {
                    "value": 5.2
                },
                {
                    "value": 5.8
                },
                {
                    "value": 6.1
                },
                {
                    "value": 6.5
                },
                {
                    "value": 6.8
                },
                {
                    "value": 7.1
                },
                {
                    "value": 7.3
                },
                {
                    "value": 7.7
                },
                {
                    "value": 8.3
                },
                {
                    "value": 8.6
                },
                {
                    "value": 8.8
                },
                {
                    "value": 9.1
                },
                {
                    "value": 9.2
                },
                {
                    "value": 9.4
                },
                {
                    "value": 9.5
                },
                {
                    "value": 9.7
                },
                {
                    "value": 10.5
                },
                {
                    "value": 10.7
                },
                {
                    "value": 10.8
                },
                {
                    "value": 11
                },
                {
                    "value": 11
                },
                {
                    "value": 11.1
                },
                {
                    "value": 11.2
                },
                {
                    "value": 11.3
                },
                {
                    "value": 11.4
                },
                {
                    "value": 11.4
                },
                {
                    "value": 11.7
                },
                {
                    "value": 12
                },
                {
                    "value": 12.9
                },
                {
                    "value": 12.9
                },
                {
                    "value": 13.3
                },
                {
                    "value": 13.7
                },
                {
                    "value": 13.8
                },
                {
                    "value": 13.9
                },
                {
                    "value": 14
                },
                {
                    "value": 14.2
                },
                {
                    "value": 14.5
                },
                {
                    "value": 15
                },
                {
                    "value": 15.2
                },
                {
                    "value": 15.6
                },
                {
                    "value": 16
                },
                {
                    "value": 16.3
                },
                {
                    "value": 17.3
                },
                {
                    "value": 17.5
                },
                {
                    "value": 17.9
                },
                {
                    "value": 18
                },
                {
                    "value": 18
                },
                {
                    "value": 20.6
                },
                {
                    "value": 21
                },
                {
                    "value": 23.4
                }
            ],
            binField='value',
            binWidth=2
        ),
        fact.AntdLine(
            data=mock_xy,
            xField='x',
            yField='y',
            smooth=True
        ),
        fact.AntdLiquid(
            percent=0.25,
            outline={
                'border': 4,
                'distance': 8,
            },
            wave={
                'length': 128,
            },
        ),
        fact.AntdPie(
            appendPadding=10,
            data=[
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
            ],
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
        ),
        fact.AntdRadar(
            data=[
                {
                    "item": "Design",
                    "user": "a",
                    "score": 70
                },
                {
                    "item": "Design",
                    "user": "b",
                    "score": 30
                },
                {
                    "item": "Development",
                    "user": "a",
                    "score": 60
                },
                {
                    "item": "Development",
                    "user": "b",
                    "score": 70
                },
                {
                    "item": "Marketing",
                    "user": "a",
                    "score": 50
                },
                {
                    "item": "Marketing",
                    "user": "b",
                    "score": 60
                },
                {
                    "item": "Users",
                    "user": "a",
                    "score": 40
                },
                {
                    "item": "Users",
                    "user": "b",
                    "score": 50
                },
                {
                    "item": "Test",
                    "user": "a",
                    "score": 60
                },
                {
                    "item": "Test",
                    "user": "b",
                    "score": 70
                },
                {
                    "item": "Language",
                    "user": "a",
                    "score": 70
                },
                {
                    "item": "Language",
                    "user": "b",
                    "score": 50
                },
                {
                    "item": "Technology",
                    "user": "a",
                    "score": 50
                },
                {
                    "item": "Technology",
                    "user": "b",
                    "score": 40
                },
                {
                    "item": "Support",
                    "user": "a",
                    "score": 30
                },
                {
                    "item": "Support",
                    "user": "b",
                    "score": 40
                },
                {
                    "item": "Sales",
                    "user": "a",
                    "score": 60
                },
                {
                    "item": "Sales",
                    "user": "b",
                    "score": 40
                },
                {
                    "item": "UX",
                    "user": "a",
                    "score": 50
                },
                {
                    "item": "UX",
                    "user": "b",
                    "score": 60
                }
            ],
            xField='item',
            yField='score',
            seriesField='user',
            meta={
                'score': {
                    'alias': '分数',
                    'min': 0,
                    'max': 80
                },
            },
            xAxis={
                'line': None,
                'tickLine': None,
                'grid': {
                    'line': {
                        'style': {
                            'lineDash': None,
                        },
                    },
                },
            },
            yAxis={
                'line': None,
                'tickLine': None,
                'grid': {
                    'line': {
                        'type': 'line',
                        'style': {
                                'lineDash': None,
                        },
                    },
                    'alternateColor': 'rgba(0, 0, 0, 0.04)',
                },
            },
            area={}
        ),
        fact.AntdRose(
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
            xField='type',
            yField='value',
            seriesField='type',
            radius=0.9,
            legend={
                'position': 'bottom'
            }
        )
    ][::-1],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
