if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_antd_charts as fact
    from feffery_dash_utils.style_utils import style
    from feffery_antd_charts.demo_data import stock_data

app = dash.Dash(__name__)

app.layout = html.Div(
    fact.AntdStock(
        data=stock_data,
        xField='trade_date',
        yField=['open', 'close', 'high', 'low'],
        slider={},
    ),
    style=style(padding=100),
)

if __name__ == '__main__':
    app.run(debug=True)
