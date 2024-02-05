import dash
import requests
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdTinyColumn(
            data=[274, 337, 81, 497, 666, 219, 269],
            height=64,
            columnWidthRatio=0.9
        ),
        fact.AntdTinyColumn(
            data=[274, 337, 81, 497, 666, 219, 269],
            height=64,
            pattern={
                'type': 'line'
            }
        ),
        fact.AntdTinyColumn(
            data=[274, 337, 81, 497, 666, 219, 269],
            height=64,
            tooltip=False,
            annotations=[
                {
                    'type': 'line',
                    'start': ['min', 'mean'],
                    'end': ['max', 'mean'],
                    'text': {
                        'content': '平均值',
                        'offsetY': -2,
                        'style': {
                            'textAlign': 'left',
                            'fontSize': 10,
                            'fill': 'rgba(44, 53, 66, 0.45)',
                            'textBaseline': 'bottom',
                        },
                    },
                    'style': {
                        'stroke': 'rgba(0, 0, 0, 0.25)',
                    },
                }
            ]
        ),
    ],
    style={
        'padding': '50px 100px',
        'display': 'flex',
        'flexDirection': 'column',
        'gap': 100
    }
)

if __name__ == '__main__':
    app.run(debug=True)
