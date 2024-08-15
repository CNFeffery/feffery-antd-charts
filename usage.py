import dash
from dash import html
import feffery_antd_charts as fact
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

mock_data = [
    {'type': '分类一', 'value': 27},
    {'type': '分类二', 'value': 25},
    {'type': '分类三', 'value': 18},
    {'type': '分类四', 'value': 15},
    {'type': '分类五', 'value': 10},
    {'type': '其他', 'value': 5},
]

app.layout = html.Div(
    [
        html.Div(
            [
                fac.AntdAvatar(
                    id=f'demo-avatar{i}',
                    mode='image',
                    src=f'https://api.dicebear.com/7.x/miniavs/svg?seed={i}',
                    size='large',
                    shape='circle',
                )
                for i, item in enumerate(mock_data)
            ],
            style=style(display='none'),
        ),
        fact.AntdBar(
            data=[
                {**item, 'index': i}
                for i, item in enumerate(mock_data)
            ],
            xField='value',
            yField='index',
            yAxis={
                'label': {
                    'formatter': {
                        'func': """(idx) => data[idx].type"""
                    }
                }
            },
            annotations=[
                {
                    'type': 'html',
                    'position': [i, item['value']],
                    'html': {
                        'func': "(e) => document.getElementById('demo-avatar%s').cloneNode(true)"
                        % i
                    },
                    'alignY': 'middle',
                    'offsetX': 5,
                }
                for i, item in enumerate(mock_data)
            ],
        ),
    ],
    style=style(padding=50),
)

if __name__ == '__main__':
    app.run(debug=True)
