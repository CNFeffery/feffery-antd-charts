import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdWaterfall(
            data=[
                {
                    'type': '日用品',
                    'money': 120,
                },
                {
                    'type': '伙食费',
                    'money': 900,
                },
                {
                    'type': '交通费',
                    'money': 200,
                },
                {
                    'type': '水电费',
                    'money': 300,
                },
                {
                    'type': '房租',
                    'money': 1200,
                },
                {
                    'type': '商场消费',
                    'money': 1000,
                },
                {
                    'type': '红包收入',
                    'money': -2000,
                },
            ],
            xField='type',
            yField='money',
            appendPadding=[15, 0, 0, 0],
            meta={
                'type': {
                    'alias': '类别',
                },
                'money': {
                    'alias': '收支',
                    'formatter': {
                        'func': '(v) => `${v} 元`'
                    },
                },
            },
            label={
                'style': {
                    'fontSize': 10,
                    'fill': 'rgba(0,0,0,0.65)',
                },
                'layout': [
                    {
                        'type': 'interval-adjust-position',
                    },
                ],
            },
            total={
                'label': '总支出',
                'style': {
                    'fill': '#96a6a6',
                },
            }
        ),
        fact.AntdWaterfall(
            data=[
                {
                    'month': '2019',
                    'value': 23000000,
                },
                {
                    'month': 'Jan',
                    'value': 2200000,
                },
                {
                    'month': 'Feb',
                    'value': -4600000,
                },
                {
                    'month': 'Mar',
                    'value': -9100000,
                },
                {
                    'month': 'Apr',
                    'value': 3700000,
                },
                {
                    'month': 'May',
                    'value': -2100000,
                },
                {
                    'month': 'Jun',
                    'value': 5300000,
                },
                {
                    'month': 'Jul',
                    'value': 3100000,
                },
                {
                    'month': 'Aug',
                    'value': -1500000,
                },
                {
                    'month': 'Sep',
                    'value': 4200000,
                },
                {
                    'month': 'Oct',
                    'value': 5300000,
                },
                {
                    'month': 'Nov',
                    'value': -1500000,
                },
                {
                    'month': 'Dec',
                    'value': 5100000,
                },
            ],
            padding='auto',
            appendPadding=[20, 0, 0, 0],
            xField='month',
            yField='value',
            meta={
                'month': {
                    'alias': '月份',
                },
                'value': {
                    'alias': '销售量',
                    'formatter': {
                        'func': '(v) => `${v / 10000000} 亿`'
                    },
                },
            },
            total={
                'label': '2020',
            },
            color={
                'func': '''({month, value})=> {
                if (month === '2019' || month === '2020') {
                    return '#96a6a6'
                }

                return value > 0 ? '#f4664a': '#30bf78'
            }'''
            },
            label={
                'style': {
                    'fontSize': 14,
                },
                'background': {
                    'style': {
                        'fill': '#f6f6f6',
                        'stroke': '#e6e6e6',
                        'strokeOpacity': 0.65,
                        'radius': 2,
                    },
                    'padding': 1.5
                }
            },
            waterfallStyle={
                'func': '''()=> {
                return {
                    fillOpacity: 0.85
                }
            }'''
            }
        ),
        fact.AntdWaterfall(
            data=[
                {
                    'month': '一月',
                    'value': 6200000,
                },
                {
                    'month': '二月',
                    'value': -600000,
                },
                {
                    'month': '三月',
                    'value': -4100000,
                },
                {
                    'month': '四月',
                    'value': 3700000,
                },
                {
                    'month': '五月',
                    'value': -2100000,
                },
                {
                    'month': '六月',
                    'value': 5300000,
                },
                {
                    'month': '七月',
                    'value': 3100000,
                },
                {
                    'month': '八月',
                    'value': -500000,
                },
                {
                    'month': '九月',
                    'value': 4200000,
                },
                {
                    'month': '十月',
                    'value': 5300000,
                },
                {
                    'month': '十一月',
                    'value': -500000,
                },
                {
                    'month': '十二月',
                    'value': 5100000,
                },
            ],
            padding='auto',
            appendPadding=[20, 0, 0, 0],
            xField='month',
            yField='value',
            meta={
                'month': {
                    'alias': '月份',
                },
                'value': {
                    'alias': '销售量',
                    'formatter': {
                        'func': '''(v) => `${v / 10000000} 亿`'''
                    },
                },
            },
            total={
                'label': '总计',
                'style': {
                    'fill': '#96a6a6',
                },
            },
            labelMode='absolute',
            label={
                'style': {
                    'fontSize': 10,
                },
                'background': {
                    'style': {
                        'fill': '#f6f6f6',
                        'radius': 1,
                    },
                    'padding': 1.5,
                }
            }
        )
    ][::-1],
    style={
        'padding': '50px 100px',
        'display': 'flex',
        'flexDirection': 'column',
        'gap': 100
    }
)

if __name__ == '__main__':
    app.run(debug=True)
