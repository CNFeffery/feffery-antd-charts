if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

demo_data = dict(
    demo1={'id': 'A0',
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
                                   'items': [{'text': '595万'}, {'text': '占比', 'value': '30%'}]}}]},
    demo2={'id': 'A0',
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
                                   'items': [{'text': '595万'}, {'text': '占比-非常非常非常非常非常长', 'value': '30%'}]}}]}
)


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H3('指标拆解图'),
        html.Div(
            fact.AntdDecompositionTree(
                data=demo_data.get('demo1'),
                # 回调控制每个节点是否渲染展开/折叠子节点按钮
                markerCfg={
                    'func': '''
(cfg) => {
    const { children } = cfg;
    return {
    show: children?.length,
    };
}
'''
                },
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node']
            ),
            style={
                'height': '500px',
                'border': '1px solid #dbdbda'
            }
        ),
        html.H3('指标拆解图-调整布局'),
        html.Div(
            fact.AntdDecompositionTree(
                data=demo_data.get('demo1'),
                layout={
                    'direction': 'LR',
                    'type': 'indented',
                    'dropCap': False,
                    'indent': 400
                },
                # 回调控制每个节点是否渲染展开/折叠子节点按钮
                markerCfg={
                    'func': '''
(cfg) => {
    const { children } = cfg;
    return {
    show: children?.length,
    };
}
'''
                },
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node']
            ),
            style={
                'height': '500px',
                'border': '1px solid #dbdbda'
            }
        ),
        html.H3('指标拆解图-节点样式'),
        html.Div(
            fact.AntdDecompositionTree(
                data=demo_data.get('demo1'),
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node'],
                nodeCfg={
                    'items': {
                        'containerStyle': {
                            'fill': '#fff'
                        },
                        'style': {
                            'func': '''
(cfg, group, type) => {
    const styles = {
    value: {
        fill: '#52c41a',
    },
    text: {
        fill: '#aaa',
    },
    icon: {
        width: 10,
        height: 10,
    },
    };
    return styles[type];
}
'''
                        }
                    },
                    'nodeStateStyles': {
                        'hover': {
                            'stroke': '#1890ff',
                            'lineWidth': 2
                        }
                    },
                    'style': {
                        'radius': [2, 2, 2, 2]
                    }
                },
                markerCfg={
                    'func': '''
(cfg) => {
    const { children } = cfg;
    return {
    show: children?.length,
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
        html.H3('指标拆解图-边样式'),
        html.Div(
            fact.AntdDecompositionTree(
                data=demo_data.get('demo1'),
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node'],
                edgeCfg={
                    'endArrow': {
                        'fill': '#40a9ff'
                    },
                    'style': {
                        'func': '''
(item, graph) => {

return {
    stroke: 'red',
    lineWidth: 1,
    strokeOpacity: 0.5,
};
}
'''
                    }
                },
                markerCfg={
                    'func': '''
(cfg) => {
    const { children } = cfg;
    return {
    show: children?.length,
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
        html.H3('指标拆解图-无边框'),
        html.Div(
            fact.AntdDecompositionTree(
                data=demo_data.get('demo1'),
                behaviors=['drag-canvas', 'zoom-canvas', 'drag-node'],
                nodeCfg={
                    'title': {
                        'containerStyle': {
                            'fill': 'transparent'
                        },
                        'style': {
                            'fill': '#000'
                        }
                    },
                    'items': {
                        'containerStyle': {
                            'fill': '#fff',
                        },
                        'style': {
                            'func': '''
(cfg, group, type) => {
    const styles = {
    icon: {
        width: 10,
        height: 10,
    },
    value: {
        fill: '#52c41a',
    },
    text: {
        fill: '#aaa',
    },
    };
    return styles[type];
}
'''
                        }
                    },
                    'style': {
                        'stroke': 'transparent'
                    },
                    'nodeStateStyles': False
                },
                edgeCfg={
                    'endArrow': {
                        'show': False,
                    },
                    'edgeStateStyles': False,
                    'style': {
                        'func': '''
(item, graph) => {
    return {
        stroke: '#40a9ff',
        lineWidth: Math.random() * 10 + 1,
        strokeOpacity: 0.5,
    };
}
'''
                    }
                }
            ),
            style={
                'height': '500px',
                'border': '1px solid #dbdbda'
            }
        ),
        html.H3('指标拆解图-自适应'),
        html.Div(
            fact.AntdDecompositionTree(
                data=demo_data.get('demo2'),
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
