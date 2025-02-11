import dash
import time
import random
from dash import html, dcc
import feffery_antd_charts as fact
from dash.dependencies import Input, Output
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button('更新', id='update'),
        dcc.Loading(
            fact.AntdLine(
                id='chart-demo',
                data=[
                    {
                        'date': f'2020-0{i}',
                        'y': random.randint(50, 100),
                    }
                    for i in range(1, 10)
                ],
                xField='date',
                yField='y',
            )
        ),
    ],
    style=style(padding=50),
)


@app.callback(
    Output('chart-demo', 'key'),
    Input('update', 'n_clicks'),
    prevent_initial_call=True,
)
def update(n_clicks):
    time.sleep(2)

    return str(n_clicks)


if __name__ == '__main__':
    app.run(debug=True)
