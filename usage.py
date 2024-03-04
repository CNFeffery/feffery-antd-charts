import dash
import requests
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.H2('基础小提琴图'),
        fact.AntdViolin(
            data=(
                requests
                .get('https://gw.alipayobjects.com/os/bmw-prod/6b0a5f1d-5931-42ae-b3ba-3c3cb77d0861.json')
                .json()
            ),
            xField='x',
            yField='y',
            height=500
        ),
        html.H2('分组小提琴图'),
        fact.AntdViolin(
            data=(
                requests
                .get('https://gw.alipayobjects.com/os/bmw-prod/6b0a5f1d-5931-42ae-b3ba-3c3cb77d0861.json')
                .json()
            ),
            xField='x',
            yField='y',
            seriesField='species',
            height=500
        ),
        html.H2('平滑空心小提琴图'),
        fact.AntdViolin(
            data=(
                requests
                .get('https://gw.alipayobjects.com/os/bmw-prod/6b0a5f1d-5931-42ae-b3ba-3c3cb77d0861.json')
                .json()
            ),
            xField='x',
            yField='y',
            seriesField='species',
            shape='hollow-smooth',
            height=500
        ),
        html.H2('自定义Tooltip文案'),
        fact.AntdViolin(
            data=(
                requests
                .get('https://gw.alipayobjects.com/os/bmw-prod/6b0a5f1d-5931-42ae-b3ba-3c3cb77d0861.json')
                .json()
            ),
            width=400,
            height=500,
            xField='x',
            yField='y',
            seriesField='species',
            meta={
                'high': {
                    'alias': '最大值',
                    'formatter': {
                        'func': '(v) => `${v.toFixed(2)} %`'
                    },
                },
                'low': {
                    'alias': '最小值',
                    'formatter': {
                        'func': '(v) => `${v.toFixed(2)} %`'
                    },
                },
                'q1': {
                    'alias': '上四分位数',
                    'formatter': {
                        'func': '(v) => `${v.toFixed(2)} %`'
                    },
                },
                'q3': {
                    'alias': '下四分位数',
                    'formatter': {
                        'func': '(v) => `${v.toFixed(2)} %`'
                    },
                },
                'species': {
                    'alias': '品类',
                },
            },
            tooltip={
                'fields': ['species', 'high', 'q1', 'q3', 'low'],
            }
        )
    ],
    style={
        'padding': '50px 100px',
        'display': 'flex',
        'flexDirection': 'column'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
