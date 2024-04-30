import dash
import json
from dash import html
import feffery_antd_charts as fact
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

demo_data = {
    'id': 'Modeling Methods',
    'children': [
        {
            'id': 'Classification',
            'children': [
                {
                    'id': 'Logistic regression',
                    'value': 'Logistic regression',
                },
                {
                    'id': 'Linear discriminant analysis',
                    'value': 'Linear discriminant analysis',
                },
                {'id': 'Rules', 'value': 'Rules'},
                {
                    'id': 'Decision trees',
                    'value': 'Decision trees',
                },
                {
                    'id': 'Naive Bayes',
                    'value': 'Naive Bayes',
                },
                {
                    'id': 'K nearest neighbor',
                    'value': 'K nearest neighbor',
                },
                {
                    'id': 'Probabilistic neural network',
                    'value': 'Probabilistic neural network',
                },
                {
                    'id': 'Support vector machine',
                    'value': 'Support vector machine',
                },
            ],
            'value': 'Classification',
        },
        {
            'id': 'Consensus',
            'children': [
                {
                    'id': 'Models diversity',
                    'children': [
                        {
                            'id': 'Different initializations',
                            'value': 'Different initializations',
                        },
                        {
                            'id': 'Different parameter choices',
                            'value': 'Different parameter choices',
                        },
                        {
                            'id': 'Different architectures',
                            'value': 'Different architectures',
                        },
                        {
                            'id': 'Different modeling methods',
                            'value': 'Different modeling methods',
                        },
                        {
                            'id': 'Different training sets',
                            'value': 'Different training sets',
                        },
                        {
                            'id': 'Different feature sets',
                            'value': 'Different feature sets',
                        },
                    ],
                    'value': 'Models diversity',
                },
                {
                    'id': 'Methods',
                    'children': [
                        {
                            'id': 'Classifier selection',
                            'value': 'Classifier selection',
                        },
                        {
                            'id': 'Classifier fusion',
                            'value': 'Classifier fusion',
                        },
                    ],
                    'value': 'Methods',
                },
                {
                    'id': 'Common',
                    'children': [
                        {
                            'id': 'Bagging',
                            'value': 'Bagging',
                        },
                        {
                            'id': 'Boosting',
                            'value': 'Boosting',
                        },
                        {
                            'id': 'AdaBoost',
                            'value': 'AdaBoost',
                        },
                    ],
                    'value': 'Common',
                },
            ],
            'value': 'Consensus',
        },
        {
            'id': 'Regression',
            'children': [
                {
                    'id': 'Multiple linear regression',
                    'value': 'Multiple linear regression',
                },
                {
                    'id': 'Partial least squares',
                    'value': 'Partial least squares',
                },
                {
                    'id': 'Multi-layer feedforward neural network',
                    'value': 'Multi-layer feedforward neural network',
                },
                {
                    'id': 'General regression neural network',
                    'value': 'General regression neural network',
                },
                {
                    'id': 'Support vector regression',
                    'value': 'Support vector regression',
                },
            ],
            'value': 'Regression',
        },
    ],
    'value': 'Modeling Methods',
}

app.layout = html.Div(
    [
        html.Div(
            fact.AntdRadialTree(
                data=demo_data,
                nodeCfg={
                    'type': 'diamond',
                },
                behaviors=[
                    'drag-canvas',
                    'zoom-canvas',
                    'drag-node',
                ],
                style={'height': '100%'},
            ),
            style={'height': 700},
        ),
        html.Div(
            fact.AntdRadialTree(
                data=demo_data,
                nodeCfg={
                    'size': [30, 30],
                    'type': 'circle',
                    'label': {
                        'style': {
                            'fill': '#fff',
                        },
                    },
                    'style': {
                        'fill': '#73B3D1',
                        'stroke': '#0E1155',
                        'lineWidth': 2,
                        'strokeOpacity': 0.45,
                        'shadowColor': '#73B3D1',
                        'shadowBlur': 25,
                    },
                    'nodeStateStyles': {
                        'hover': {
                            'stroke': '#73B3D1',
                            'lineWidth': 2,
                            'strokeOpacity': 1,
                        },
                    },
                },
                edgeCfg={
                    'style': {
                        'stroke': '#73B3D1',
                        'shadowColor': '#73B3D1',
                        'shadowBlur': 20,
                    },
                    'endArrow': {
                        'type': 'triangle',
                        'fill': '#73B3D1',
                        'd': 15,
                        'size': 8,
                    },
                    'edgeStateStyles': {
                        'hover': {
                            'stroke': '#73B3D1',
                            'lineWidth': 2,
                        },
                    },
                },
                behaviors=[
                    'drag-canvas',
                    'zoom-canvas',
                    'drag-node',
                ],
                style={'height': '100%'},
            ),
            style={'height': 700},
        ),
    ],
    style={'padding': 50},
)

if __name__ == '__main__':
    app.run(debug=True)
