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
        ),
        fact.AntdSankey(
            data=[
                {
                    'source': '首次打开',
                    'target': '首页 UV',
                    'value': 160,
                },
                {
                    'source': '结果页',
                    'target': '首页 UV',
                    'value': 40,
                },
                {
                    'source': '验证页',
                    'target': '首页 UV',
                    'value': 10,
                },
                {
                    'source': '我的',
                    'target': '首页 UV',
                    'value': 10,
                },
                {
                    'source': '朋友',
                    'target': '首页 UV',
                    'value': 8,
                },
                {
                    'source': '其他来源',
                    'target': '首页 UV',
                    'value': 27,
                },
                {
                    'source': '首页 UV',
                    'target': '理财',
                    'value': 30,
                },
                {
                    'source': '首页 UV',
                    'target': '扫一扫',
                    'value': 40,
                },
                {
                    'source': '首页 UV',
                    'target': '服务',
                    'value': 35,
                },
                {
                    'source': '首页 UV',
                    'target': '蚂蚁森林',
                    'value': 25,
                },
                {
                    'source': '首页 UV',
                    'target': '跳失',
                    'value': 10,
                },
                {
                    'source': '首页 UV',
                    'target': '借呗',
                    'value': 30,
                },
                {
                    'source': '首页 UV',
                    'target': '花呗',
                    'value': 40,
                },
                {
                    'source': '首页 UV',
                    'target': '其他流向',
                    'value': 45,
                },
            ],
            sourceField='source',
            targetField='target',
            weightField='value',
            nodeWidthRatio=0.008,
            nodePaddingRatio=0.03
        ),
        fact.AntdScatter(
            data=[
                {
                    "H/A": "A",
                    "Team": "Torino",
                    "xG conceded": 0.62,
                    "Shot conceded": 10,
                    "Result": "3"
                },
                {
                    "H/A": "H",
                    "Team": "Atalanta",
                    "xG conceded": 2.35,
                    "Shot conceded": 23,
                    "Result": "1"
                },
                {
                    "H/A": "A",
                    "Team": "Milan",
                    "xG conceded": 1.89,
                    "Shot conceded": 26,
                    "Result": "0"
                },
                {
                    "H/A": "H",
                    "Team": "Chievo",
                    "xG conceded": 1.4,
                    "Shot conceded": 13,
                    "Result": "1"
                },
                {
                    "H/A": "A",
                    "Team": "Bologna",
                    "xG conceded": 1.02,
                    "Shot conceded": 11,
                    "Result": 0
                },
                {
                    "H/A": "H",
                    "Team": "Frosinone",
                    "xG conceded": 0.56,
                    "Shot conceded": 11,
                    "Result": "3"
                },
                {
                    "H/A": "H",
                    "Team": "Lazio",
                    "xG conceded": 1.01,
                    "Shot conceded": 16,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "Empoli",
                    "xG conceded": 1.56,
                    "Shot conceded": 20,
                    "Result": "3"
                },
                {
                    "H/A": "H",
                    "Team": "Spal",
                    "xG conceded": 1.8,
                    "Shot conceded": 6,
                    "Result": "0"
                },
                {
                    "H/A": "A",
                    "Team": "Napoli",
                    "xG conceded": 2.49,
                    "Shot conceded": 26,
                    "Result": "1"
                },
                {
                    "H/A": "A",
                    "Team": "Fiorentina",
                    "xG conceded": 1.3,
                    "Shot conceded": 14,
                    "Result": "1"
                },
                {
                    "H/A": "H",
                    "Team": "Sampdoria",
                    "xG conceded": 1.2,
                    "Shot conceded": 8,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "Udinese",
                    "xG conceded": 1.22,
                    "Shot conceded": 9,
                    "Result": "0"
                },
                {
                    "H/A": "H",
                    "Team": "Inter",
                    "xG conceded": 2.68,
                    "Shot conceded": 17,
                    "Result": "1"
                },
                {
                    "H/A": "A",
                    "Team": "Cagliari",
                    "xG conceded": 2.1,
                    "Shot conceded": 16,
                    "Result": "1"
                },
                {
                    "H/A": "H",
                    "Team": "Genoa",
                    "xG conceded": 1.84,
                    "Shot conceded": 15,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "Juventus",
                    "xG conceded": 2.12,
                    "Shot conceded": 20,
                    "Result": "0"
                },
                {
                    "H/A": "H",
                    "Team": "Sassuolo",
                    "xG conceded": 0.72,
                    "Shot conceded": 10,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "Parma",
                    "xG conceded": 0.58,
                    "Shot conceded": 6,
                    "Result": "3"
                },
                {
                    "H/A": "H",
                    "Team": "Torino",
                    "xG conceded": 1.87,
                    "Shot conceded": 10,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "Atalanta",
                    "xG conceded": 2.68,
                    "Shot conceded": 23,
                    "Result": "1"
                },
                {
                    "H/A": "H",
                    "Team": "Milan",
                    "xG conceded": 0.85,
                    "Shot conceded": 8,
                    "Result": "1"
                },
                {
                    "H/A": "A",
                    "Team": "Chievo",
                    "xG conceded": 0.84,
                    "Shot conceded": 16,
                    "Result": "3"
                },
                {
                    "H/A": "H",
                    "Team": "Bologna",
                    "xG conceded": 2.69,
                    "Shot conceded": 20,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "Frosinone",
                    "xG conceded": 1.51,
                    "Shot conceded": 11,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "Lazio",
                    "xG conceded": 1.77,
                    "Shot conceded": 13,
                    "Result": "0"
                },
                {
                    "H/A": "H",
                    "Team": "Empoli",
                    "xG conceded": 0.14,
                    "Shot conceded": 5,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "Real Madrid",
                    "xG conceded": 3.58,
                    "Shot conceded": 30,
                    "Result": "0"
                },
                {
                    "H/A": "H",
                    "Team": "Viktoria Plzen",
                    "xG conceded": 0.33,
                    "Shot conceded": 7,
                    "Result": 3
                },
                {
                    "H/A": "H",
                    "Team": "CSKA Moscow",
                    "xG conceded": 0.73,
                    "Shot conceded": 13,
                    "Result": "3"
                },
                {
                    "H/A": "A",
                    "Team": "CSKA Moscow",
                    "xG conceded": 1.1,
                    "Shot conceded": 14,
                    "Result": "3"
                },
                {
                    "H/A": "H",
                    "Team": "Real Madrid",
                    "xG conceded": 1.87,
                    "Shot conceded": 12,
                    "Result": "0"
                },
                {
                    "H/A": "A",
                    "Team": "Viktoria Plzen",
                    "xG conceded": 1.85,
                    "Shot conceded": 13,
                    "Result": "0"
                },
                {
                    "H/A": "A",
                    "Team": "Porto",
                    "xG conceded": 3.71,
                    "Shot conceded": 31,
                    "Result": "0"
                },
                {
                    "H/A": "H",
                    "Team": "Porto",
                    "xG conceded": 0.56,
                    "Shot conceded": 7,
                    "Result": "3"
                }
            ],
            xField='xG conceded',
            yField='Shot conceded',
            colorField='Result',
            size=5,
            shape='circle'
        ),
        fact.AntdStock(
            data=[
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-13",
                    "close": 2906.0735,
                    "open": 2927.1443,
                    "high": 2935.406,
                    "low": 2901.2425,
                    "vol": 274804844,
                    "amount": 334526327.4
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-14",
                    "close": 2917.0077,
                    "open": 2899.8659,
                    "high": 2926.9427,
                    "low": 2899.5739,
                    "vol": 250650627,
                    "amount": 308080368.7
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-17",
                    "close": 2983.6224,
                    "open": 2924.9913,
                    "high": 2983.6371,
                    "low": 2924.9913,
                    "vol": 313198007,
                    "amount": 367014340.1
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-18",
                    "close": 2984.9716,
                    "open": 2981.4097,
                    "high": 2990.6003,
                    "low": 2960.7751,
                    "vol": 311665913,
                    "amount": 374998562.6
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-19",
                    "close": 2975.4019,
                    "open": 2979.5223,
                    "high": 2998.2718,
                    "low": 2971.8219,
                    "vol": 315141151,
                    "amount": 381331160.4
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-20",
                    "close": 3030.1542,
                    "open": 2981.8802,
                    "high": 3031.3706,
                    "low": 2968.4451,
                    "vol": 345732881,
                    "amount": 413761364.1
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-21",
                    "close": 3039.6692,
                    "open": 3022.2455,
                    "high": 3058.898,
                    "low": 3020.141,
                    "vol": 364557276,
                    "amount": 445062076.7
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-24",
                    "close": 3031.2333,
                    "open": 3027.8925,
                    "high": 3042.1821,
                    "low": 3007.3557,
                    "vol": 370430044,
                    "amount": 451601363.1
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-25",
                    "close": 3013.0501,
                    "open": 2982.0696,
                    "high": 3016.9458,
                    "low": 2943.7168,
                    "vol": 441622762,
                    "amount": 513128644.6
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-26",
                    "close": 2987.9287,
                    "open": 2978.4195,
                    "high": 3028.7788,
                    "low": 2974.9423,
                    "vol": 469049552,
                    "amount": 495341447.3
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-27",
                    "close": 2991.3288,
                    "open": 2992.4919,
                    "high": 3009.4575,
                    "low": 2980.4774,
                    "vol": 350523658,
                    "amount": 395955641.5
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-02-28",
                    "close": 2880.3038,
                    "open": 2924.6407,
                    "high": 2948.1261,
                    "low": 2878.5443,
                    "vol": 401216914,
                    "amount": 432657775
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-02",
                    "close": 2970.9312,
                    "open": 2899.31,
                    "high": 2982.5068,
                    "low": 2899.31,
                    "vol": 367333369,
                    "amount": 397244201.2
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-03",
                    "close": 2992.8968,
                    "open": 3006.8888,
                    "high": 3026.842,
                    "low": 2976.623,
                    "vol": 410108047,
                    "amount": 447053681.5
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-04",
                    "close": 3011.6657,
                    "open": 2981.806,
                    "high": 3012.0035,
                    "low": 2974.3583,
                    "vol": 353338278,
                    "amount": 389893917.5
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-05",
                    "close": 3071.6771,
                    "open": 3036.1545,
                    "high": 3074.2571,
                    "low": 3022.9262,
                    "vol": 445425806,
                    "amount": 482770471.4
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-06",
                    "close": 3034.5113,
                    "open": 3039.9395,
                    "high": 3052.4439,
                    "low": 3029.4632,
                    "vol": 362061533,
                    "amount": 377388542.7
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-09",
                    "close": 2943.2907,
                    "open": 2987.1805,
                    "high": 2989.2051,
                    "low": 2940.7138,
                    "vol": 414560736,
                    "amount": 438143854.6
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-10",
                    "close": 2996.7618,
                    "open": 2918.9347,
                    "high": 3000.2963,
                    "low": 2904.7989,
                    "vol": 393296648,
                    "amount": 425017184.8
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-11",
                    "close": 2968.5174,
                    "open": 3001.7616,
                    "high": 3010.0286,
                    "low": 2968.5174,
                    "vol": 352470970,
                    "amount": 378766619
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-12",
                    "close": 2923.4856,
                    "open": 2936.0163,
                    "high": 2944.4651,
                    "low": 2906.2838,
                    "vol": 307778457,
                    "amount": 328209202.4
                },
                {
                    "ts_code": "000001.SH",
                    "trade_date": "2020-03-13",
                    "close": 2887.4265,
                    "open": 2804.2322,
                    "high": 2910.8812,
                    "low": 2799.9841,
                    "vol": 366450436,
                    "amount": 393019665.2
                }
            ],
            xField='trade_date',
            yField=['open', 'close', 'high', 'low'],
            slider={}
        ),
        fact.AntdSunburst(
            data={
                "label": "root",
                "children": [
                    {
                        "label": "类别 1",
                        "children": [
                            {
                                "label": "类别 1.1",
                                "children": [
                                    {
                                        "label": "类别 1.1.1",
                                        "children": [
                                            {
                                                "label": "类别 1.1.1.1",
                                                "children": [
                                                    {
                                                        "label": "类别 1.1.1.1.1",
                                                        "children": None,
                                                        "uv": 1,
                                                        "sum": 1,
                                                        "count": 0
                                                    }
                                                ],
                                                "uv": 0,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 1,
                                        "count": 0
                                    }
                                ],
                                "uv": 0,
                                "sum": 1,
                                "count": 0
                            }
                        ],
                        "uv": 0,
                        "sum": 1,
                        "count": 0
                    },
                    {
                        "label": "类别 2",
                        "children": [
                            {
                                "label": "类别 2.1",
                                "children": [
                                    {
                                        "label": "类别 2.1.1",
                                        "children": [
                                            {
                                                "label": "类别 2.1.1.1",
                                                "children": [
                                                    {
                                                        "label": "类别 2.1.1.1.1",
                                                        "value": "口碑-本地生活事业部-东成西就大区-大中台-运营",
                                                        "children": [
                                                            {
                                                                "label": "类别 2.1.1.1.1.1",
                                                                "children": None,
                                                                "uv": 1,
                                                                "sum": 1,
                                                                "count": 0
                                                            },
                                                            {
                                                                "label": "类别 2.1.1.1.1.2",
                                                                "children": None,
                                                                "uv": 1,
                                                                "sum": 1,
                                                                "count": 0
                                                            }
                                                        ],
                                                        "uv": 1,
                                                        "sum": 3,
                                                        "count": 0
                                                    }
                                                ],
                                                "uv": 1,
                                                "sum": 4,
                                                "count": 0
                                            },
                                            {
                                                "label": "类别 2.1.1.2",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 5,
                                        "count": 0
                                    },
                                    {
                                        "label": "类别 2.1.2",
                                        "children": [
                                            {
                                                "label": "类别 2.1.2.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            },
                                            {
                                                "label": "类别 2.1.2.2",
                                                "children": [
                                                    {
                                                        "label": "类别 2.1.2.2.1",
                                                        "children": None,
                                                        "uv": 1,
                                                        "sum": 1,
                                                        "count": 0
                                                    }
                                                ],
                                                "uv": 0,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 2,
                                        "count": 0
                                    },
                                    {
                                        "label": "类别 2.1.3",
                                        "children": [
                                            {
                                                "label": "类别 2.1.3.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 1,
                                        "count": 0
                                    },
                                    {
                                        "label": "类别 2.1.4",
                                        "children": [
                                            {
                                                "label": "类别 2.1.4.1",
                                                "children": None,
                                                "uv": 2,
                                                "sum": 2,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 2,
                                        "count": 0
                                    },
                                    {
                                        "label": "类别 2.1.5",
                                        "children": None,
                                        "uv": 1,
                                        "sum": 1,
                                        "count": 0
                                    }
                                ],
                                "uv": 1,
                                "sum": 12,
                                "count": 0
                            },
                            {
                                "label": "类别 2.2",
                                "children": [
                                    {
                                        "label": "类别 2.2.1",
                                        "children": None,
                                        "uv": 1,
                                        "sum": 1,
                                        "count": 0
                                    }
                                ],
                                "uv": 1,
                                "sum": 2,
                                "count": 0
                            },
                            {
                                "label": "类别 2.3",
                                "children": None,
                                "uv": 1,
                                "sum": 1,
                                "count": 0
                            },
                            {
                                "label": "类别 2.4",
                                "children": [
                                    {
                                        "label": "类别 2.4.1",
                                        "children": [
                                            {
                                                "label": "类别 2.4.1.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 1,
                                        "count": 0
                                    }
                                ],
                                "uv": 0,
                                "sum": 1,
                                "count": 0
                            },
                            {
                                "label": "类别 2.5",
                                "children": [
                                    {
                                        "label": "类别 2.5.1",
                                        "children": None,
                                        "uv": 3,
                                        "sum": 3,
                                        "count": 0
                                    }
                                ],
                                "uv": 0,
                                "sum": 3,
                                "count": 0
                            }
                        ],
                        "uv": 1,
                        "sum": 20,
                        "count": 0
                    },
                    {
                        "label": "类别 3",
                        "children": [
                            {
                                "label": "类别 3.1",
                                "children": [
                                    {
                                        "label": "类别 3.1.1",
                                        "children": [
                                            {
                                                "label": "类别 3.1.1.1",
                                                "children": [
                                                    {
                                                        "label": "类别 3.1.1.1.1",
                                                        "children": [
                                                            {
                                                                "label": "类别 3.1.1.1.1.1",
                                                                "children": None,
                                                                "uv": 1,
                                                                "sum": 1,
                                                                "count": 0
                                                            }
                                                        ],
                                                        "uv": 0,
                                                        "sum": 1,
                                                        "count": 0
                                                    }
                                                ],
                                                "uv": 0,
                                                "sum": 1,
                                                "count": 0
                                            },
                                            {
                                                "label": "类别 3.1.1.2",
                                                "children": [
                                                    {
                                                        "label": "类别 3.1.1.2.1",
                                                        "children": [
                                                            {
                                                                "label": "类别 3.1.1.2.1.1",
                                                                "children": None,
                                                                "uv": 2,
                                                                "sum": 2,
                                                                "count": 0
                                                            }
                                                        ],
                                                        "uv": 0,
                                                        "sum": 2,
                                                        "count": 0
                                                    }
                                                ],
                                                "uv": 1,
                                                "sum": 3,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 4,
                                        "count": 0
                                    },
                                    {
                                        "label": "类别 3.1.2",
                                        "children": [
                                            {
                                                "label": "类别 3.1.2.1",
                                                "children": None,
                                                "uv": 3,
                                                "sum": 3,
                                                "count": 0
                                            },
                                            {
                                                "label": "类别 3.1.2.2",
                                                "children": [
                                                    {
                                                        "_id": "数据产品&运营",
                                                        "label": "数据产品&运营",
                                                        "value": "蚂蚁金服-平台数据技术事业群-数据平台部-数据资产平台-数据产品&运营",
                                                        "children": None,
                                                        "uv": 1,
                                                        "sum": 1,
                                                        "count": 0
                                                    }
                                                ],
                                                "uv": 0,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 4,
                                        "count": 0
                                    }
                                ],
                                "uv": 0,
                                "sum": 8,
                                "count": 0
                            },
                            {
                                "label": "类别 3.2",
                                "children": [
                                    {
                                        "label": "类别 3.2.1",
                                        "children": [
                                            {
                                                "label": "类别 3.2.1.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            },
                                            {
                                                "label": "类别 3.2.1.2",
                                                "children": [
                                                    {
                                                        "label": "类别 3.2.1.2.1",
                                                        "children": None,
                                                        "uv": 1,
                                                        "sum": 1,
                                                        "count": 0
                                                    },
                                                    {
                                                        "label": "类别 3.2.1.2.2",
                                                        "children": [
                                                            {
                                                                "_id": "城市民生运营",
                                                                "label": "城市民生运营",
                                                                "value": "蚂蚁金服-支付宝事业群-商家服务及开放平台事业部-公共服务部-运营部-城市民生运营",
                                                                "children": None,
                                                                "uv": 1,
                                                                "sum": 1,
                                                                "count": 0
                                                            }
                                                        ],
                                                        "uv": 0,
                                                        "sum": 1,
                                                        "count": 0
                                                    }
                                                ],
                                                "uv": 1,
                                                "sum": 3,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 4,
                                        "count": 0
                                    }
                                ],
                                "uv": 0,
                                "sum": 4,
                                "count": 0
                            },
                            {
                                "label": "类别 3.3",
                                "children": [
                                    {
                                        "label": "类别 3.3.1",
                                        "children": [
                                            {
                                                "label": "类别 3.3.1.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 1,
                                        "count": 0
                                    }
                                ],
                                "uv": 1,
                                "sum": 2,
                                "count": 0
                            },
                            {
                                "label": "类别 3.4",
                                "children": [
                                    {
                                        "label": "类别 3.4.1",
                                        "children": [
                                            {
                                                "label": "类别 3.4.1.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            },
                                            {
                                                "label": "3.4.1.2",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 2,
                                        "count": 0
                                    },
                                    {
                                        "label": "类别 3.4.2",
                                        "children": None,
                                        "uv": 1,
                                        "sum": 1,
                                        "count": 0
                                    },
                                    {
                                        "label": "类别 3.4.3",
                                        "children": [
                                            {
                                                "label": "类别 3.4.3.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 1,
                                        "count": 0
                                    }
                                ],
                                "uv": 0,
                                "sum": 4,
                                "count": 0
                            },
                            {
                                "label": "类别 3.5",
                                "children": [
                                    {
                                        "label": "类别 3.5.1",
                                        "children": [
                                            {
                                                "label": "类别 3.5.1.1",
                                                "children": None,
                                                "uv": 2,
                                                "sum": 2,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 2,
                                        "count": 0
                                    },
                                    {
                                        "label": "类别 3.5.2",
                                        "children": [
                                            {
                                                "label": "类别 3.5.2.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 1,
                                        "count": 0
                                    }
                                ],
                                "uv": 0,
                                "sum": 3,
                                "count": 0
                            },
                            {
                                "label": "类别 3.6",
                                "children": [
                                    {
                                        "label": "类别 3.6.1",
                                        "children": [
                                            {
                                                "label": "类别 3.6.1.1",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            },
                                            {
                                                "label": "类别 3.6.1.2",
                                                "children": None,
                                                "uv": 1,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 2,
                                        "count": 0
                                    }
                                ],
                                "uv": 1,
                                "sum": 3,
                                "count": 0
                            },
                            {
                                "label": "类别 3.7",
                                "children": [
                                    {
                                        "label": "类别 3.7.1",
                                        "children": [
                                            {
                                                "label": "类别 3.7.1.1",
                                                "children": [
                                                    {
                                                        "label": "类别 3.7.1.1.1",
                                                        "children": None,
                                                        "uv": 1,
                                                        "sum": 1,
                                                        "count": 0
                                                    }
                                                ],
                                                "uv": 0,
                                                "sum": 1,
                                                "count": 0
                                            }
                                        ],
                                        "uv": 0,
                                        "sum": 1,
                                        "count": 0
                                    }
                                ],
                                "uv": 0,
                                "sum": 1,
                                "count": 0
                            }
                        ],
                        "uv": 0,
                        "sum": 25,
                        "count": 0
                    }
                ]
            },
            innerRadius=0.3,
            hierarchyConfig={
                'field': 'sum',
            },
            drilldown={
                'breadCrumb': {
                    'rootText': '起始',
                },
            }
        ),
        fact.AntdTinyLine(
            data=[
                264, 417, 438, 887, 309, 397, 550, 575, 563, 430, 525, 592, 492, 467, 513, 546, 983, 340, 539, 243, 226, 192,
            ],
            smooth=True
        ),
        fact.AntdTreemap(
            data={
                'name': 'root',
                'children': [
                        {
                            'name': '分类 1',
                            'value': 560,
                        },
                    {
                            'name': '分类 2',
                            'value': 500,
                    },
                    {
                            'name': '分类 3',
                            'value': 150,
                    },
                    {
                            'name': '分类 4',
                            'value': 140,
                    },
                    {
                            'name': '分类 5',
                            'value': 115,
                    },
                    {
                            'name': '分类 6',
                            'value': 95,
                    },
                    {
                            'name': '分类 7',
                            'value': 90,
                    },
                    {
                            'name': '分类 8',
                            'value': 75,
                    },
                    {
                            'name': '分类 9',
                            'value': 98,
                    },
                    {
                            'name': '分类 10',
                            'value': 60,
                    },
                    {
                            'name': '分类 11',
                            'value': 45,
                    },
                    {
                            'name': '分类 12',
                            'value': 40,
                    },
                    {
                            'name': '分类 13',
                            'value': 40,
                    },
                    {
                            'name': '分类 14',
                            'value': 35,
                    },
                    {
                            'name': '分类 15',
                            'value': 40,
                    },
                    {
                            'name': '分类 16',
                            'value': 40,
                    },
                    {
                            'name': '分类 17',
                            'value': 40,
                    },
                    {
                            'name': '分类 18',
                            'value': 30,
                    },
                    {
                            'name': '分类 19',
                            'value': 28,
                    },
                    {
                            'name': '分类 20',
                            'value': 16,
                    },
                ],
            },
            colorField='name'
        ),
        fact.AntdWordCloud(
            data=[
                {
                    "value": 9,
                    "name": "AntV"
                },
                {
                    "value": 8,
                    "name": "F2"
                },
                {
                    "value": 8,
                    "name": "G2"
                },
                {
                    "value": 8,
                    "name": "G6"
                },
                {
                    "value": 8,
                    "name": "DataSet"
                },
                {
                    "value": 8,
                    "name": "墨者学院"
                },
                {
                    "value": 6,
                    "name": "Analysis"
                },
                {
                    "value": 6,
                    "name": "Data Mining"
                },
                {
                    "value": 6,
                    "name": "Data Vis"
                },
                {
                    "value": 6,
                    "name": "Design"
                },
                {
                    "value": 6,
                    "name": "Grammar"
                },
                {
                    "value": 6,
                    "name": "Graphics"
                },
                {
                    "value": 6,
                    "name": "Graph"
                },
                {
                    "value": 6,
                    "name": "Hierarchy"
                },
                {
                    "value": 6,
                    "name": "Labeling"
                },
                {
                    "value": 6,
                    "name": "Layout"
                },
                {
                    "value": 6,
                    "name": "Quantitative"
                },
                {
                    "value": 6,
                    "name": "Relation"
                },
                {
                    "value": 6,
                    "name": "Statistics"
                },
                {
                    "value": 6,
                    "name": "可视化"
                },
                {
                    "value": 6,
                    "name": "数据"
                },
                {
                    "value": 6,
                    "name": "数据可视化"
                },
                {
                    "value": 4,
                    "name": "Arc Diagram"
                },
                {
                    "value": 4,
                    "name": "Bar Chart"
                },
                {
                    "value": 4,
                    "name": "Canvas"
                },
                {
                    "value": 4,
                    "name": "Chart"
                },
                {
                    "value": 4,
                    "name": "DAG"
                },
                {
                    "value": 4,
                    "name": "DG"
                },
                {
                    "value": 4,
                    "name": "Facet"
                },
                {
                    "value": 4,
                    "name": "Geo"
                },
                {
                    "value": 4,
                    "name": "Line"
                },
                {
                    "value": 4,
                    "name": "MindMap"
                },
                {
                    "value": 4,
                    "name": "Pie"
                },
                {
                    "value": 4,
                    "name": "Pizza Chart"
                },
                {
                    "value": 4,
                    "name": "Punch Card"
                },
                {
                    "value": 4,
                    "name": "SVG"
                },
                {
                    "value": 4,
                    "name": "Sunburst"
                },
                {
                    "value": 4,
                    "name": "Tree"
                },
                {
                    "value": 4,
                    "name": "UML"
                },
                {
                    "value": 3,
                    "name": "Chart"
                },
                {
                    "value": 3,
                    "name": "View"
                },
                {
                    "value": 3,
                    "name": "Geom"
                },
                {
                    "value": 3,
                    "name": "Shape"
                },
                {
                    "value": 3,
                    "name": "Scale"
                },
                {
                    "value": 3,
                    "name": "Animate"
                },
                {
                    "value": 3,
                    "name": "Global"
                },
                {
                    "value": 3,
                    "name": "Slider"
                },
                {
                    "value": 3,
                    "name": "Connector"
                },
                {
                    "value": 3,
                    "name": "Transform"
                },
                {
                    "value": 3,
                    "name": "Util"
                },
                {
                    "value": 3,
                    "name": "DomUtil"
                },
                {
                    "value": 3,
                    "name": "MatrixUtil"
                },
                {
                    "value": 3,
                    "name": "PathUtil"
                },
                {
                    "value": 3,
                    "name": "G"
                },
                {
                    "value": 3,
                    "name": "2D"
                },
                {
                    "value": 3,
                    "name": "3D"
                },
                {
                    "value": 3,
                    "name": "Line"
                },
                {
                    "value": 3,
                    "name": "Area"
                },
                {
                    "value": 3,
                    "name": "Interval"
                },
                {
                    "value": 3,
                    "name": "Schema"
                },
                {
                    "value": 3,
                    "name": "Edge"
                },
                {
                    "value": 3,
                    "name": "Polygon"
                },
                {
                    "value": 3,
                    "name": "Heatmap"
                },
                {
                    "value": 3,
                    "name": "Render"
                },
                {
                    "value": 3,
                    "name": "Tooltip"
                },
                {
                    "value": 3,
                    "name": "Axis"
                },
                {
                    "value": 3,
                    "name": "Guide"
                },
                {
                    "value": 3,
                    "name": "Coord"
                },
                {
                    "value": 3,
                    "name": "Legend"
                },
                {
                    "value": 3,
                    "name": "Path"
                },
                {
                    "value": 3,
                    "name": "Helix"
                },
                {
                    "value": 3,
                    "name": "Theta"
                },
                {
                    "value": 3,
                    "name": "Rect"
                },
                {
                    "value": 3,
                    "name": "Polar"
                },
                {
                    "value": 3,
                    "name": "Dsv"
                },
                {
                    "value": 3,
                    "name": "Csv"
                },
                {
                    "value": 3,
                    "name": "Tsv"
                },
                {
                    "value": 3,
                    "name": "GeoJSON"
                },
                {
                    "value": 3,
                    "name": "TopoJSON"
                },
                {
                    "value": 3,
                    "name": "Filter"
                },
                {
                    "value": 3,
                    "name": "Map"
                },
                {
                    "value": 3,
                    "name": "Pick"
                },
                {
                    "value": 3,
                    "name": "Rename"
                },
                {
                    "value": 3,
                    "name": "Filter"
                },
                {
                    "value": 3,
                    "name": "Map"
                },
                {
                    "value": 3,
                    "name": "Pick"
                },
                {
                    "value": 3,
                    "name": "Rename"
                },
                {
                    "value": 3,
                    "name": "Reverse"
                },
                {
                    "value": 3,
                    "name": "sort"
                },
                {
                    "value": 3,
                    "name": "Subset"
                },
                {
                    "value": 3,
                    "name": "Partition"
                },
                {
                    "value": 3,
                    "name": "Imputation"
                },
                {
                    "value": 3,
                    "name": "Fold"
                },
                {
                    "value": 3,
                    "name": "Aggregate"
                },
                {
                    "value": 3,
                    "name": "Proportion"
                },
                {
                    "value": 3,
                    "name": "Histogram"
                },
                {
                    "value": 3,
                    "name": "Quantile"
                },
                {
                    "value": 3,
                    "name": "Treemap"
                },
                {
                    "value": 3,
                    "name": "Hexagon"
                },
                {
                    "value": 3,
                    "name": "Binning"
                },
                {
                    "value": 3,
                    "name": "kernel"
                },
                {
                    "value": 3,
                    "name": "Regression"
                },
                {
                    "value": 3,
                    "name": "Density"
                },
                {
                    "value": 3,
                    "name": "Sankey"
                },
                {
                    "value": 3,
                    "name": "Voronoi"
                },
                {
                    "value": 3,
                    "name": "Projection"
                },
                {
                    "value": 3,
                    "name": "Centroid"
                },
                {
                    "value": 3,
                    "name": "H5"
                },
                {
                    "value": 3,
                    "name": "Mobile"
                },
                {
                    "value": 3,
                    "name": "K线图"
                },
                {
                    "value": 3,
                    "name": "关系图"
                },
                {
                    "value": 3,
                    "name": "烛形图"
                },
                {
                    "value": 3,
                    "name": "股票图"
                },
                {
                    "value": 3,
                    "name": "直方图"
                },
                {
                    "value": 3,
                    "name": "金字塔图"
                },
                {
                    "value": 3,
                    "name": "分面"
                },
                {
                    "value": 3,
                    "name": "南丁格尔玫瑰图"
                },
                {
                    "value": 3,
                    "name": "饼图"
                },
                {
                    "value": 3,
                    "name": "线图"
                },
                {
                    "value": 3,
                    "name": "点图"
                },
                {
                    "value": 3,
                    "name": "散点图"
                },
                {
                    "value": 3,
                    "name": "子弹图"
                },
                {
                    "value": 3,
                    "name": "柱状图"
                },
                {
                    "value": 3,
                    "name": "仪表盘"
                },
                {
                    "value": 3,
                    "name": "气泡图"
                },
                {
                    "value": 3,
                    "name": "漏斗图"
                },
                {
                    "value": 3,
                    "name": "热力图"
                },
                {
                    "value": 3,
                    "name": "玉玦图"
                },
                {
                    "value": 3,
                    "name": "直方图"
                },
                {
                    "value": 3,
                    "name": "矩形树图"
                },
                {
                    "value": 3,
                    "name": "箱形图"
                },
                {
                    "value": 3,
                    "name": "色块图"
                },
                {
                    "value": 3,
                    "name": "螺旋图"
                },
                {
                    "value": 3,
                    "name": "词云"
                },
                {
                    "value": 3,
                    "name": "词云图"
                },
                {
                    "value": 3,
                    "name": "雷达图"
                },
                {
                    "value": 3,
                    "name": "面积图"
                },
                {
                    "value": 3,
                    "name": "马赛克图"
                },
                {
                    "value": 3,
                    "name": "盒须图"
                },
                {
                    "value": 3,
                    "name": "坐标轴"
                },
                {
                    "value": 3,
                    "name": ""
                },
                {
                    "value": 3,
                    "name": "Jacques Bertin"
                },
                {
                    "value": 3,
                    "name": "Leland Wilkinson"
                },
                {
                    "value": 3,
                    "name": "William Playfair"
                },
                {
                    "value": 3,
                    "name": "关联"
                },
                {
                    "value": 3,
                    "name": "分布"
                },
                {
                    "value": 3,
                    "name": "区间"
                },
                {
                    "value": 3,
                    "name": "占比"
                },
                {
                    "value": 3,
                    "name": "地图"
                },
                {
                    "value": 3,
                    "name": "时间"
                },
                {
                    "value": 3,
                    "name": "比较"
                },
                {
                    "value": 3,
                    "name": "流程"
                },
                {
                    "value": 3,
                    "name": "趋势"
                },
                {
                    "value": 2,
                    "name": "亦叶"
                },
                {
                    "value": 2,
                    "name": "再飞"
                },
                {
                    "value": 2,
                    "name": "完白"
                },
                {
                    "value": 2,
                    "name": "巴思"
                },
                {
                    "value": 2,
                    "name": "张初尘"
                },
                {
                    "value": 2,
                    "name": "御术"
                },
                {
                    "value": 2,
                    "name": "有田"
                },
                {
                    "value": 2,
                    "name": "沉鱼"
                },
                {
                    "value": 2,
                    "name": "玉伯"
                },
                {
                    "value": 2,
                    "name": "画康"
                },
                {
                    "value": 2,
                    "name": "祯逸"
                },
                {
                    "value": 2,
                    "name": "绝云"
                },
                {
                    "value": 2,
                    "name": "罗宪"
                },
                {
                    "value": 2,
                    "name": "萧庆"
                },
                {
                    "value": 2,
                    "name": "董珊珊"
                },
                {
                    "value": 2,
                    "name": "陆沉"
                },
                {
                    "value": 2,
                    "name": "顾倾"
                },
                {
                    "value": 2,
                    "name": "Domo"
                },
                {
                    "value": 2,
                    "name": "GPL"
                },
                {
                    "value": 2,
                    "name": "PAI"
                },
                {
                    "value": 2,
                    "name": "SPSS"
                },
                {
                    "value": 2,
                    "name": "SYSTAT"
                },
                {
                    "value": 2,
                    "name": "Tableau"
                },
                {
                    "value": 2,
                    "name": "D3"
                },
                {
                    "value": 2,
                    "name": "Vega"
                },
                {
                    "value": 2,
                    "name": "统计图表"
                }
            ],
            wordField='name',
            weightField='value',
            colorField='name',
            wordStyle={
                'fontFamily': 'Verdana',
                'fontSize': [8, 32],
                'rotation': 0
            },
            legend={},
            randomState=0.5
        )
    ][::-1],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
