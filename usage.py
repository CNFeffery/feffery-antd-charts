import dash
import requests
from dash import html
import feffery_antd_charts as fact

# 示例数据
demo_data = (
    requests
    .get('https://gw.alipayobjects.com/os/bmw-prod/be63e0a2-d2be-4c45-97fd-c00f752a66d4.json')
    .json()
    [:10]
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
                'withTheme': 'dark',
                'fontFamily': 'KaiTi'
            }
        )
    ],
    style={
        'padding': 50,
        'background': 'black'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
