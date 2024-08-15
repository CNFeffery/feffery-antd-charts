import dash
from dash import html
import feffery_antd_charts as fact
import feffery_antd_components as fac
import feffery_utils_components as fuc

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
)

server = app.server

app.title = '自动化测试报告管理平台'

home_content = [
    {
        'name': '压测用例数(个)',
        'data': [
            {'type': 'App', 'count': 76},
            {'type': '固件', 'count': 98},
            {'type': '记录仪', 'count': 10},
        ],
    },
    {
        'name': '压测覆盖版本(个)',
        'data': [
            {'type': 'App', 'count': 76},
            {'type': '固件', 'count': 98},
            {'type': '记录仪', 'count': 10},
        ],
    },
    {
        'name': '压测次数(万次)',
        'data': [
            {'type': 'App', 'count': 10.8},
            {'type': '固件', 'count': 0.7},
            {'type': '记录仪', 'count': 1},
        ],
    },
    {
        'name': 'UI用例数(个)',
        'data': [
            {'type': 'App', 'count': 76},
            {'type': '固件', 'count': 98},
            {'type': '记录仪', 'count': 10},
        ],
    },
    {
        'name': 'UI回归覆盖版本(个)',
        'data': [
            {'type': 'App', 'count': 76},
            {'type': '固件', 'count': 98},
            {'type': '记录仪', 'count': 10},
        ],
    },
    {
        'name': 'UI回归次数(万次)',
        'data': [
            {'type': 'App', 'count': 3.5},
            {'type': '固件', 'count': 1.2},
            {'type': '记录仪', 'count': 1},
        ],
    },
]

app.layout = html.Div(
    [
        fac.AntdRow(
            [
                fac.AntdCol(
                    fuc.FefferyDiv(
                        [
                            fac.AntdTag(
                                content=item['name'],
                                style={'fontSize': '12px'},
                            ),
                            fact.AntdPie(
                                data=item['data'],
                                legend=False,
                                angleField='count',
                                colorField='type',
                                innerRadius=0.8,
                                label=False,
                                statistic={
                                    'title': {
                                        'style': {
                                            'fontSize': '11px'
                                        },
                                        'content': '总计',
                                        'offsetY': -5,
                                    },
                                    'content': {
                                        'style': {
                                            'fontSize': '11px'
                                        }
                                    },
                                },
                                interactions=[
                                    {
                                        'type': 'pie-statistic-active'
                                    }
                                ],
                                height=120,
                                radius=0.8,
                                style={'paddingTop': '5px'},
                            ),
                        ],
                        shadow='always-shadow',
                        style={
                            'borderRadius': 8,
                            'height': 140,
                            'border': '1px solid #e9ecef',
                            'padding': '20px 25px',
                            'position': 'relative',
                        },
                    ),
                    span=4,
                )
                for index, item in enumerate(home_content)
            ],
            gutter=15,
            style={'marginBottom': 25},
        ),
    ],
    style={'padding': '50px 150px'},
)


if __name__ == '__main__':
    """
    1、 想每个柱状图后，显示图像组件
    2、每个柱状图自定义颜色
       16进制颜色码  '5b9bd5', 'ed7d31', '70ad47', 'ffc000' , '4472c4', '91d024' , 'b235e6' , '02ae75'
    """
    app.run(debug=True)
