import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdRose(
            id='rose-demo',
            data=[
                {
                    'type': '分类一',
                    'value': 27,
                },
                {
                    'type': '分类二',
                    'value': 25,
                },
                {
                    'type': '分类三',
                    'value': 18,
                },
                {
                    'type': '分类四',
                    'value': 15,
                },
                {
                    'type': '分类五',
                    'value': 10,
                },
                {
                    'type': '其他',
                    'value': 5,
                },
            ],
            xField='type',
            yField='value',
            seriesField='type',
            radius=0.9,
            legend={
                'position': 'bottom',
            },
            pattern={
                'type': 'square'
            }
        ),
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
