import dash
import requests
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdHeatmap(
            data=(
                requests
                .get('https://gw.alipayobjects.com/os/basement_prod/a719cd4e-bd40-4878-a4b4-df8a6b531dfe.json')
                .json()
            ),
            xField='Month of Year',
            yField='District',
            colorField='AQHI',
            color=['#174c83', '#7eb6d4', '#efefeb', '#efa759', '#9b4d16'],
            meta={
                'Month of Year': {
                    'type': 'cat',
                },
            }
        ),
        fact.AntdHeatmap(
            data=(
                requests
                .get('https://gw.alipayobjects.com/os/bmw-prod/68d3f380-089e-4683-ab9e-4493200198f9.json')
                .json()
            ),
            xField='name',
            yField='country',
            colorField='value',
            shape='circle',
            sizeRatio=0.5,
            color=['#0d5fbb', '#7eadfc', '#fd8b6f', '#aa3523'],
            label={
                'style': {
                    'fill': '#fff',
                    'shadowBlur': 2,
                    'shadowColor': 'rgba(0, 0, 0, .45)',
                },
            }
        ),
        fact.AntdHeatmap(
            data=(
                requests
                .get('https://gw.alipayobjects.com/os/bmw-prod/68d3f380-089e-4683-ab9e-4493200198f9.json')
                .json()
            ),
            xField='name',
            yField='country',
            colorField='value',
            sizeField='value',
            shape='square',
            color=['#dddddd', '#9ec8e0', '#5fa4cd', '#2e7ab6', '#114d90'],
            label={
                'style': {
                    'fill': '#fff',
                    'shadowBlur': 2,
                    'shadowColor': 'rgba(0, 0, 0, .45)',
                },
            }
        ),
        fact.AntdHeatmap(
            height=800,
            data=(
                requests
                .get('https://gw.alipayobjects.com/os/antvdemo/assets/data/polar-heatmap.json')
                .json()
            ),
            xField='time',
            yField='week',
            colorField='value',
            legend=True,
            color='#BAE7FF-#1890FF-#1028ff',
            coordinate={
                'type': 'polar',
                'cfg': {
                    'innerRadius': 0.2,
                },
            },
            heatmapStyle={
                'stroke': '#f5f5f5',
                'opacity': 0.8,
            },
            meta={
                'time': {
                    'type': 'cat',
                },
                'value': {
                    'min': 0,
                    'max': 1,
                },
            },
            xAxis={
                'line': None,
                'grid': None,
                'tickLine': None,
                'label': {
                    'offset': 12,
                    'style': {
                        'fill': '#666',
                        'fontSize': 12,
                        'textBaseline': 'top',
                    },
                },
            },
            yAxis={
                'top': True,
                'line': None,
                'grid': None,
                'tickLine': None,
                'label': {
                    'offset': 0,
                    'style': {
                        'fill': '#fff',
                        'textAlign': 'center',
                        'shadowBlur': 2,
                        'shadowColor': 'rgba(0, 0, 0, .45)',
                    },
                },
            },
            tooltip={
                'showMarkers': False,
            },
            interactions=[
                {
                    'type': 'element-active',
                }
            ]
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
