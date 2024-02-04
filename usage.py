import dash
import requests
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdTinyArea(
            data=[
                264, 417, 438, 887, 309, 397, 550, 575, 563, 430, 525, 592, 492, 467, 513, 546, 983, 340, 539, 243, 226, 192,
            ],
            height=60,
            smooth=True
        ),
        fact.AntdTinyArea(
            data=[
                264, 417, 438, 887, 309, 397, 550, 575, 563, 430, 525, 592, 492, 467, 513, 546, 983, 340, 539, 243, 226, 192,
            ],
            height=60,
            smooth=True,
            color='#E5EDFE',
            pattern={
                'type': 'line',
                'cfg': {
                    'stroke': '#5B8FF9',
                },
            }
        ),
        fact.AntdTinyArea(
            data=[
                264, 417, 438, 887, 309, 397, 550, 575, 563, 430, 525, 592, 492, 467, 513, 546, 983, 340, 539, 243, 226, 192,
            ],
            height=60,
            smooth=True,
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
                },
                {
                    'type': 'line',
                    'start': ['min', 800],
                    'end': ['max', 800],
                    'text': {
                        'content': '目标值',
                        'offsetY': -2,
                        'style': {
                            'textAlign': 'left',
                            'fontSize': 10,
                            'fill': 'rgba(44, 53, 66, 0.45)',
                            'textBaseline': 'bottom',
                        },
                    },
                    'style': {
                        'stroke': 'rgba(0, 0, 0, 0.55)',
                    },
                },
            ]
        ),
        fact.AntdTinyArea(
            data=[
                264, 417, 438, 887, 309, 397, 550, 575, 563, 430, 525, 592, 492, 467, 513, 546, 983, 340, 539, 243, 226, 192,
            ],
            height=60,
            smooth=True,
            areaStyle={
                'fill': '#d6e3fd',
            }
        )
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
