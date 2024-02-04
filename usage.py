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
        )
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
