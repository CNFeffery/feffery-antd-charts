import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.H2('基础韦恩图'),
        fact.AntdVenn(
            data=[
                {
                    'sets': ['A'],
                    'size': 12,
                    'label': 'A',
                },
                {
                    'sets': ['B'],
                    'size': 12,
                    'label': 'B',
                },
                {
                    'sets': ['C'],
                    'size': 12,
                    'label': 'C',
                },
                {
                    'sets': ['A', 'B'],
                    'size': 2,
                    'label': 'A&B',
                },
                {
                    'sets': ['A', 'C'],
                    'size': 2,
                    'label': 'A&C',
                },
                {
                    'sets': ['B', 'C'],
                    'size': 2,
                    'label': 'B&C',
                },
                {
                    'sets': ['A', 'B', 'C'],
                    'size': 1,
                },
            ],
            setsField='sets',
            sizeField='size',
            pointStyle={
                'fillOpacity': 0.85,
            },
            legend={
                'position': 'top'
            }
        ),
        html.H2('设置颜色叠加模式'),
        fact.AntdVenn(
            data=[
                {
                    'sets': ['A'],
                    'size': 12,
                    'label': 'A',
                },
                {
                    'sets': ['B'],
                    'size': 12,
                    'label': 'B',
                },
                {
                    'sets': ['C'],
                    'size': 12,
                    'label': 'C',
                },
                {
                    'sets': ['A', 'B'],
                    'size': 2,
                    'label': 'A&B',
                },
                {
                    'sets': ['A', 'C'],
                    'size': 2,
                    'label': 'A&C',
                },
                {
                    'sets': ['B', 'C'],
                    'size': 2,
                    'label': 'B&C',
                },
                {
                    'sets': ['A', 'B', 'C'],
                    'size': 1,
                },
            ],
            setsField='sets',
            sizeField='size',
            blendMode='overlay',
            pointStyle={
                'fillOpacity': 0.85,
            }
        ),
        html.H2('格式化tooltip'),
        fact.AntdVenn(
            data=[
                {
                    'sets': ['A'],
                    'size': 12,
                    'label': 'A',
                },
                {
                    'sets': ['B'],
                    'size': 12,
                    'label': 'B',
                },
                {
                    'sets': ['C'],
                    'size': 12,
                    'label': 'C',
                },
                {
                    'sets': ['A', 'B'],
                    'size': 2,
                    'label': 'A&B',
                },
                {
                    'sets': ['A', 'C'],
                    'size': 2,
                    'label': 'A&C',
                },
                {
                    'sets': ['B', 'C'],
                    'size': 2,
                    'label': 'B&C',
                },
                {
                    'sets': ['A', 'B', 'C'],
                    'size': 1,
                    'label': 'A&B&C',
                },
            ],
            setsField='sets',
            sizeField='size',
            pointStyle={
                'fillOpacity': 0.85,
            },
            tooltip={
                'fields': ['label', 'size'],
                'formatter': {
                    'func': '''(datum) => {
        return {
          name: datum.label,
          value: datum.size,
        };
      }'''
                }
            }
        ),
        html.H2('设置label'),
        fact.AntdVenn(
            data=[
                {
                    'sets': ['A'],
                    'size': 12,
                    'label': 'A',
                },
                {
                    'sets': ['B'],
                    'size': 12,
                    'label': 'B',
                },
                {
                    'sets': ['C'],
                    'size': 12,
                    'label': 'C',
                },
                {
                    'sets': ['A', 'B'],
                    'size': 2,
                    'label': 'A&B',
                },
                {
                    'sets': ['A', 'C'],
                    'size': 2,
                    'label': 'A&C',
                },
                {
                    'sets': ['B', 'C'],
                    'size': 2,
                    'label': 'B&C',
                },
                {
                    'sets': ['A', 'B', 'C'],
                    'size': 1,
                    'label': 'A&B&C',
                },
            ],
            setsField='sets',
            sizeField='size',
            pointStyle={
                'fillOpacity': 0.85,
            },
            label={
                'offsetY': 7,
                'style': {
                    'fontSize': 14,
                },
                'formatter': {
                    'func': '''(datum) => `${datum.sets.join('&')}: ${datum.size}`'''
                },
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
