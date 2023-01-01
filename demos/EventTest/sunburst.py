if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    import numpy as np
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

mock_data = {
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
}

app.layout = html.Div(
    [
        html.Div(
            fact.AntdSunburst(
                id='sunburst-demo',
                data=mock_data,
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
            style={
                'height': '400px'
            }
        ),
        html.Pre(
            id='output'
        )
    ],
    style={
        'padding': '50px 150px'
    }
)


@app.callback(
    Output('output', 'children'),
    [Input('sunburst-demo', 'recentlyTooltipChangeRecord'),
     Input('sunburst-demo', 'recentlyAreaClickRecord')]
)
def demo(recentlyTooltipChangeRecord,
         recentlyAreaClickRecord):

    return json.dumps(
        dict(
            recentlyTooltipChangeRecord=recentlyTooltipChangeRecord,
            recentlyAreaClickRecord=recentlyAreaClickRecord
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
