if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

demo_data = dict(
    demo1={'nodes': [{'id': '1',
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
    demo2={
        'nodes': [
            {
                'id': '任务A',
                'value': {
                    'text': '任务A',
                    'status': 'success',
                    'start_datetime': '2022-09-27 10:00:00',
                    'end_datetime': '2022-09-27 10:02:00'
                }
            },
            {
                'id': '任务B',
                'value': {
                    'text': '任务B',
                    'status': 'processing',
                    'start_datetime': '2022-09-27 10:02:02'
                }
            },
            {
                'id': '任务C',
                'value': {
                    'text': '任务C',
                    'status': 'error',
                    'start_datetime': '2022-09-27 10:02:05'
                }
            },
            {
                'id': '任务D',
                'value': {
                    'text': '任务D',
                    'status': 'default'
                }
            },
            {
                'id': '任务E',
                'value': {
                    'text': '任务E',
                    'status': 'default'
                }
            },
            {
                'id': '任务F',
                'value': {
                    'text': '任务F',
                    'status': 'default'
                }
            }
        ],
        'edges': [
            {
                'source': '任务A',
                'target': '任务B'
            },
            {
                'source': '任务A',
                'target': '任务C'
            },
            {
                'source': '任务B',
                'target': '任务D'
            },
            {
                'source': '任务C',
                'target': '任务E'
            },
            {
                'source': '任务D',
                'target': '任务F'
            },
            {
                'source': '任务E',
                'target': '任务F'
            }
        ]
    }
)


app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.H3('资金流向图'),
        html.Div(
            fact.AntdFundFlow(
                data=demo_data.get('demo1'),
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node']
            ),
            style={
                'height': '500px',
                'border': '1px solid #dbdbda'
            }
        ),
        html.H3('资金流向图-格式化设置'),
        html.Div(
            fact.AntdFundFlow(
                data=demo_data.get('demo1'),
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node'],
                markerCfg={
                    'func': '''
(cfg) => {
    const { edges } = data;
    return {
    position: 'right',
    show: edges.find((item) => item.source === cfg.id),
    collapsed: !edges.find((item) => item.source === cfg.id),
    };
}
'''
                }
            ),
            style={
                'height': '500px',
                'border': '1px solid #dbdbda'
            }
        ),
        html.H3('资金流向图-自由流向'),
        html.Div(
            fact.AntdFundFlow(
                data=demo_data.get('demo2'),
                behaviors=['drag-canvas', 'zoom-canvas'],
                nodeCfg={
                    'style': {
                        'func': '''
(e) => {
    if (e.value.status === "success") {
        return {
            stroke: 'green'
        }
    } else if (e.value.status === "error") {
        return {
            stroke: "red"
        }
    } else if (e.value.status === "processing") {
        return {
            stroke: "#40a9ff"
        }
    } else if (e.value.status === "default") {
        return {
            stroke: "#c8c6c4"
        }
    } 
}'''
                    },
                    'nodeStateStyles': False
                },
                edgeCfg={
                    'style': {
                        'stroke': '#c8c6c4'
                    },
                    'endArrow': {
                        'fill': '#c8c6c4'
                    },
                    'edgeStateStyles': False
                }
            ),
            style={
                'height': '500px',
                'border': '1px solid #dbdbda'
            }
        )
    ],
    style={
        'width': '1000px',
        'margin': '0 auto',
        'paddingTop': '50px',
        'paddingBottom': '50px',
    }
)


if __name__ == '__main__':
    app.run(debug=True)
