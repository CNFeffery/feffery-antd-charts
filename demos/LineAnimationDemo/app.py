if True:
    import sys
    sys.path.append('../..')
    import dash
    import requests
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

demo_data = (
    requests
    .get(
        'https://gw.alipayobjects.com/os/bmw-prod/e00d52f4-2fa6-47ee-a0d7-105dd95bde20.json'
    )
    .json()
)

app.layout = html.Div(
    [
        fact.AntdLine(
            data=demo_data,
            xField='year',
            yField='gdp',
            seriesField='name',
            legend={
                'position': 'top',
            },
            smooth=True,
            animation={
                'appear': {
                    'animation': 'path-in',
                    'duration': 5000,
                },
            },
            style={
                'height': '500px'
            }
        )
    ],
    style={
        'padding': '100px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
