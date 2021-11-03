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
                                )
                            ]
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

        fac.AntdDivider()
    ],
    style={
        'padding': '100px 100px 100px 100px'
    }
)


@app.callback(
    [Output('fact-line', 'legend')],
    [Input('fact-line-legend-switch', 'checked')],
    prevent_initial_call=True,
)
def fact_line_callback(legend_checked):

    return [
        {} if legend_checked else False
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
