import dash
import random
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdColumn(
            data=[
                {
                    '类型': f'类型{type}',
                    '分组': f'分组{group}',
                    '数值': round(random.uniform(10, 50), 2)
                }
                for type in list('abcedf')
                for group in range(1, 4)
            ],
            xField='类型',
            yField='数值',
            seriesField='分组',
            isGroup=True,
            legend={
                'position': 'bottom'
            },
            columnStyle={
                'radius': [6, 6, 0, 0]
            },
            interactions=[
                {
                    'type': 'element-list-highlight'
                }
            ]
        )
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
