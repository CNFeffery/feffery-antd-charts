import dash
import json
from dash import html
import feffery_antd_charts as fact
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

demo_data = {
    'nodes': [
        {
            'id': '1',
            'value': {
                'text': 'Company1',
                'icon': 'https://gw.alipayobjects.com/zos/antfincdn/28B4PgocL4/bbd3e7ef-6b5e-4034-893d-1b5073ad9aa4.png',
            },
        },
        {'id': '2', 'value': {'text': 'Company2'}},
        {'id': '3', 'value': {'text': 'Company3'}},
        {'id': '4', 'value': {'text': 'Company4'}},
        {'id': '5', 'value': {'text': 'Company5'}},
        {'id': '6', 'value': {'text': 'Company6'}},
        {'id': '7', 'value': {'text': 'Company7'}},
        {'id': '8', 'value': {'text': 'Company8'}},
        {'id': '9', 'value': {'text': 'Company9'}},
    ],
    'edges': [
        {
            'source': '1',
            'target': '2',
            'value': {
                'text': '100,000 Yuan',
                'subText': '2019-08-03',
                'extraKey': 'A',
            },
        },
        {
            'source': '1',
            'target': '3',
            'value': {
                'text': '100,000 Yuan',
                'subText': '2019-08-03',
                'extraKey': 'B',
            },
        },
        {
            'source': '2',
            'target': '5',
            'value': {
                'text': '100,000 Yuan',
                'subText': '2019-08-03',
            },
        },
        {
            'source': '5',
            'target': '6',
            'value': {
                'text': '100,000 Yuan',
                'subText': '2019-08-03',
            },
        },
        {
            'source': '3',
            'target': '4',
            'value': {
                'text': '100,000 Yuan',
                'subText': '2019-08-03',
            },
        },
        {
            'source': '4',
            'target': '7',
            'value': {
                'text': '100,000 Yuan',
                'subText': '2019-08-03',
            },
        },
        {
            'source': '1',
            'target': '8',
            'value': {
                'text': '100,000 Yuan',
                'subText': '2019-08-03',
            },
        },
        {
            'source': '1',
            'target': '9',
            'value': {
                'text': '100,000 Yuan',
                'subText': '2019-08-03',
            },
        },
    ],
}

app.layout = html.Div(
    [
        html.Div(
            fact.AntdFundFlow(
                id='chart-demo',
                data=demo_data,
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
