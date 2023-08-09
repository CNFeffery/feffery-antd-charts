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

app.layout = html.Div(
    [
        html.Div(
            fact.AntdScatter(
                data=[
                    {
                        "city": "上海",
                        "搜索UV": 1.5,
                        "端DAU": 6,
                        "搜索DAU渗透率": 3,
                    },
                    {
                        "city": "台北",
                        "搜索UV": 2,
                        "端DAU": 5,
                        "搜索DAU渗透率": 13,
                    },
                    {
                        "city": "北京",
                        "搜索UV": 7,
                        "端DAU": 3.6,
                        "搜索DAU渗透率": 16,
                    },
                    {
                        "city": "济南",
                        "搜索UV": 5,
                        "端DAU": 5,
                        "搜索DAU渗透率": 16,
                    },
                    {
                        "city": "青岛",
                        "搜索UV": 2,
                        "端DAU": 1,
                        "搜索DAU渗透率": 19,
                    },
                    {
                        "city": "杭州",
                        "搜索UV": 7,
                        "端DAU": 2,
                        "搜索DAU渗透率": 90,
                    },
                    {
                        "city": "广东",
                        "搜索UV": 7.4,
                        "端DAU": 1.5,
                        "搜索DAU渗透率": 30,
                    },
                    {
                        "city": "无锡",
                        "搜索UV": 1,
                        "端DAU": 1,
                        "搜索DAU渗透率": 34,
                    },
                    {
                        "city": "重庆",
                        "搜索UV": 7,
                        "端DAU": 5,
                        "搜索DAU渗透率": 46,
                    },
                    {
                        "city": "成都",
                        "搜索UV": 3.4,
                        "端DAU": 2.3,
                        "搜索DAU渗透率": 49,
                    },
                    {
                        "city": "哈尔滨",
                        "搜索UV": 0.5,
                        "端DAU": 6.5,
                        "搜索DAU渗透率": 51,
                    },
                    {
                        "city": "内蒙古",
                        "搜索UV": 2.5,
                        "端DAU": 5,
                        "搜索DAU渗透率": 51,
                    },
                    {
                        "city": "云南",
                        "搜索UV": 1,
                        "端DAU": 5,
                        "搜索DAU渗透率": 53,
                    },
                    {
                        "city": "河北",
                        "搜索UV": 6,
                        "端DAU": 5,
                        "搜索DAU渗透率": 57,
                    },
                    {
                        "city": "陕西",
                        "搜索UV": 2,
                        "端DAU": 3,
                        "搜索DAU渗透率": 57,
                    },
                    {
                        "city": "苏州",
                        "搜索UV": 3,
                        "端DAU": 4.6,
                        "搜索DAU渗透率": 65,
                    },
                    {
                        "city": "四川",
                        "搜索UV": 6,
                        "端DAU": 7,
                        "搜索DAU渗透率": 68,
                    },
                    {
                        "city": "贵阳",
                        "搜索UV": 5,
                        "端DAU": 3.4,
                        "搜索DAU渗透率": 68,
                    },
                    {
                        "city": "台湾",
                        "搜索UV": 5,
                        "端DAU": 2,
                        "搜索DAU渗透率": 69,
                    },
                    {
                        "city": "哈尔滨",
                        "搜索UV": 2,
                        "端DAU": 7,
                        "搜索DAU渗透率": 78,
                    },
                    {
                        "city": "天津",
                        "搜索UV": 4.4,
                        "端DAU": 5,
                        "搜索DAU渗透率": 45,
                    },
                    {
                        "city": "长沙",
                        "搜索UV": 3.4,
                        "端DAU": 7,
                        "搜索DAU渗透率": 29,
                    },
                    {
                        "city": "沧州",
                        "搜索UV": 3,
                        "端DAU": 1,
                        "搜索DAU渗透率": 94,
                    },
                    {
                        "city": "宁波",
                        "搜索UV": 6,
                        "端DAU": 3,
                        "搜索DAU渗透率": 99,
                    },
                ],
                meta={
                    'city': {
                        'alias': '城市'
                    }
                },
                appendPadding=16,
                xField='搜索UV',
                yField='端DAU',
                sizeField='搜索DAU渗透率',
                size=[12, 30],
                shape='circle',
                pointStyle={
                    'fill': '#D6E3FD',
                    'fillOpacity': 0.6,
                    'stroke': '#6d9bf9',
                },
                tooltip={
                    'fields': ['city', '搜索UV', '端DAU', '搜索DAU渗透率'],
                    'customItems': {
                        'func': '''(items) => {
                            items.forEach((item, index) => {
                                if ( item.name === '搜索UV' || item.name === '端DAU' ) {
                                    items[index] = {
                                        ...item,
                                        value: item.value + '万'
                                    }
                                } else if ( item.name === '搜索DAU渗透率' ) {
                                    items[index] = {
                                        ...item,
                                        value: item.value + '%'
                                    }
                                }
                            })
                            console.log(items)
                            return items;
                        }
                    '''
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

if __name__ == '__main__':
    app.run(debug=True)
