import dash
import requests
from dash import html
import feffery_antd_charts as fact

# 示例数据
demo_data = (
    requests
    .get('https://gw.alipayobjects.com/os/bmw-prod/be63e0a2-d2be-4c45-97fd-c00f752a66d4.json')
    .json()
)

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdColumn(
            data=demo_data,
            xField='城市',
            yField='销售额',
            xAxis={
                'label': {
                    'autoRotate': False,
                },
            },
            appendPadding=10,
            scrollbar={
                'type': 'horizontal',
            },
            theme={
                'components': {
                    'scrollbar': {
                        'default': {
                            'style': {
                                'trackColor': 'rgba(255,255,255,0.05)',
                                'thumbColor': 'red',
                            },
                        },
                        'hover': {
                            'style': {
                                'thumbColor': 'rgba(255,255,255,0.6)',
                            },
                        },
                    }
                }
            }
        )
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
