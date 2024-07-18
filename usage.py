import dash
from dash import html
import feffery_antd_charts as fact
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fact.AntdPie(
            data=[
                {'type': '分类一', 'value': 27},
                {'type': '分类二', 'value': 25},
                {'type': '分类三', 'value': 18},
                {'type': '分类四', 'value': 15},
                {'type': '分类五', 'value': 10},
                {'type': '其他', 'value': 5},
            ],
            angleField='value',
            colorField='type',
            innerRadius=0.6,
            label={'type': 'inner'},
            meta={
                'value': {
                    'formatter': {
                        'func': '(v) => `${v} ¥`'
                    },
                },
            },
            statistic={'title': {'content': '总金额'}},
            interactions=[{'type': 'pie-statistic-active'}],
        )
    ],
    style=style(padding=50),
)

if __name__ == '__main__':
    app.run(debug=True)
