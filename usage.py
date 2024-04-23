import dash
import json
from dash import html
import feffery_antd_charts as fact
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

demo_data = [
    {'type': '家具家电', 'sales': 38},
    {'type': '粮油副食', 'sales': 52},
    {'type': '生鲜水果', 'sales': 61},
    {'type': '美容洗护', 'sales': 145},
    {'type': '母婴用品', 'sales': 48},
    {'type': '进口食品', 'sales': 38},
    {'type': '食品饮料', 'sales': 38},
    {'type': '家庭清洁', 'sales': 38},
]

app.layout = html.Div(
    [
        fact.AntdColumn(
            id='demo-chart',
            data=demo_data,
            xField='type',
            yField='sales',
            label={
                'position': 'middle',
                'style': {
                    'fill': '#FFFFFF',
                    'opacity': 0.6,
                },
            },
            xAxis={
                'label': {
                    'autoHide': True,
                    'autoRotate': False,
                },
            },
            meta={
                'type': {
                    'alias': '类别',
                },
                'sales': {
                    'alias': '销售额',
                },
            },
        ),
        html.Pre(id='event-output'),
    ],
    style={'padding': '50px 100px'},
)


@app.callback(
    Output('event-output', 'children'),
    Input('demo-chart', 'recentlyColumnClickRecord'),
    prevent_initial_call=True,
)
def show_event(recentlyColumnClickRecord):
    return json.dumps(
        recentlyColumnClickRecord,
        indent=4,
        ensure_ascii=False,
    )


if __name__ == '__main__':
    app.run(debug=True)
