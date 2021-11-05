import dash
import math
import demjson
import requests
from dash import html
import feffery_antd_components as fac
import feffery_antd_charts as fact
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

# 构建示例数据
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


radar_data = [
    {'name': 'G2', 'star': 10178},
    {'name': 'G6', 'star': 7077},
    {'name': 'F2', 'star': 7345},
    {'name': 'L7', 'star': 2029},
    {'name': 'X6', 'star': 298},
    {'name': 'AVA', 'star': 806},
]

radar_data = [
    {
        **item,
        **{
            'star': round(math.log(item['star']), 2)
        }
    }
    for item in radar_data
]

# 构建前端内容
app.layout = html.Div(
    [
        fac.AntdTitle('折线图参数测试', level=2),

        fac.AntdRow(
            [
                fac.AntdCol(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdSwitch(
                                    id='fact-line-legend-switch',
                                    checkedChildren='开启图例',
                                    unCheckedChildren='关闭图例',
                                    checked=True
                                ),
                                fac.AntdSwitch(
                                    id='fact-line-xAxis-switch',
                                    checkedChildren='开启xAxis',
                                    unCheckedChildren='关闭xAxis',
                                    checked=True
                                ),
                                fac.AntdSwitch(
                                    id='fact-line-yAxis-switch',
                                    checkedChildren='开启yAxis',
                                    unCheckedChildren='关闭yAxis',
                                    checked=True
                                ),
                                fac.AntdSwitch(
                                    id='fact-line-label-switch',
                                    checkedChildren='开启label',
                                    unCheckedChildren='关闭label',
                                    checked=True
                                ),
                                fac.AntdSwitch(
                                    id='fact-line-tooltip-switch',
                                    checkedChildren='开启tooltip',
                                    unCheckedChildren='关闭tooltip',
                                    checked=True
                                ),
                                fac.AntdSwitch(
                                    id='fact-line-slider-switch',
                                    checkedChildren='开启slider',
                                    unCheckedChildren='关闭slider',
                                    checked=True
                                )
                            ],
                            direction='vertical'
                        )
                    ],
                    span=8,
                    style={
                        'borderRight': '1px solid rgba(213, 213, 213, 0.8)'
                    }
                ),
                fac.AntdCol(
                    fact.AntdLine(
                        id='fact-line',
                        data=data,
                        xField='x',
                        yField='y',
                        seriesField='series',
                        slider={},
                        padding='auto',
                        appendPadding=40,
                        renderer='svg'
                    ),
                    span=16
                )
            ],
            style={
                'height': '800px'
            }
        ),

        fac.AntdDivider(),


        fact.AntdRadar(
            data=radar_data,
            xField='name',
            yField='star',
            # xAxis={
            #     'line': None,
            #     'tickLine': None,
            # },
            # yAxis={
            #     'label': False,
            #     'grid': {
            #         'alternateColor': 'rgba(0, 0, 0, 0.04)',
            #     },
            # },
            # meta={
            #     'star': {
            #         'alias': '分数'
            #     },
            # },
            point={},
            area={}
        )
    ],
    style={
        'padding': '100px 100px 100px 100px'
    }
)


@app.callback(
    [Output('fact-line', 'legend'),
     Output('fact-line', 'xAxis'),
     Output('fact-line', 'yAxis'),
     Output('fact-line', 'label'),
     Output('fact-line', 'tooltip'),
     Output('fact-line', 'slider')],
    [Input('fact-line-legend-switch', 'checked'),
     Input('fact-line-xAxis-switch', 'checked'),
     Input('fact-line-yAxis-switch', 'checked'),
     Input('fact-line-label-switch', 'checked'),
     Input('fact-line-tooltip-switch', 'checked'),
     Input('fact-line-slider-switch', 'checked')]
)
def fact_line_callback(legend_checked,
                       xAxis_checked,
                       yAxis_checked,
                       label_checked,
                       tooltip_checked,
                       slider_checked):

    return [
        {} if legend_checked else False,
        {} if xAxis_checked else False,
        {} if yAxis_checked else False,
        {} if label_checked else False,
        {} if tooltip_checked else False,
        {} if slider_checked else False
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
