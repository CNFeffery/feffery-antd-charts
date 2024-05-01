import dash
import json
from dash import html
import feffery_antd_charts as fact
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

demo_data = {
    'id': 'A0',
    'value': {
        'title': '订单金额',
        'items': [{'text': '3031万'}],
    },
    'children': [
        {
            'id': 'A1',
            'value': {
                'title': '华南',
                'items': [
                    {'text': '1152万'},
                    {'text': '占比', 'value': '30%'},
                ],
            },
            'children': [
                {
                    'id': 'A11',
                    'value': {
                        'title': '广东',
                        'items': [
                            {'text': '1152万'},
                            {
                                'text': '占比',
                                'value': '30%',
                            },
                        ],
                    },
                },
                {
                    'id': 'A12',
                    'value': {
                        'title': '广西',
                        'items': [
                            {'text': '1152万'},
                            {
                                'text': '占比',
                                'value': '30%',
                            },
                        ],
                    },
                },
                {
                    'id': 'A13',
                    'value': {
                        'title': '海南',
                        'items': [
                            {'text': '1152万'},
                            {
                                'text': '占比',
                                'value': '30%',
                            },
                        ],
                    },
                },
            ],
        },
        {
            'id': 'A2',
            'value': {
                'title': '华北',
                'items': [
                    {'text': '595万'},
                    {
                        'text': '占比',
                        'value': '30%',
                        'icon': 'https://gw.alipayobjects.com/zos/antfincdn/iFh9X011qd/7797962c-04b6-4d67-9143-e9d05f9778bf.png',
                    },
                ],
            },
        },
    ],
}

app.layout = html.Div(
    [
        html.Div(
            fact.AntdDecompositionTree(
                id='chart-demo',
                data=demo_data,
                behaviors=[
                    'drag-canvas',
                    'zoom-canvas',
                    'drag-node',
                ],
                animate=False,
                style={'height': '100%'},
            ),
            style={'height': 700},
        ),
        html.Pre(id='output'),
    ],
    style={'padding': 50},
)


@app.callback(
    Output('output', 'children'),
    Input('chart-demo', 'recentlyNodeClickRecord'),
    prevent_initial_call=True,
)
def demo(recentlyNodeClickRecord):
    return json.dumps(
        recentlyNodeClickRecord,
        indent=4,
        ensure_ascii=False,
    )


if __name__ == '__main__':
    app.run(debug=True)
