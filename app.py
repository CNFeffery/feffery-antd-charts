import dash
import numpy as np
from dash import html
import feffery_antd_charts as fact
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State


def generate_mock_data():

    random_data = np.random.randint(10, 20, 8)
    random_statistic = int(np.random.uniform(10, 99))

    return [
        [
            {
                'type': f'类别{i}',
                'value': value
            }
            for i, value in enumerate(random_data)
        ],
        {
            'content': {
                'content': f'{int(random_statistic)}万'
            }
        }
    ]


app = dash.Dash(__name__)

initial_data, initial_statistic = generate_mock_data()

app.layout = html.Div(
    html.Div(
        [
            fac.AntdSpace(
                [
                    fac.AntdButton(
                        '只更新data',
                        id='update-data',
                    ),
                    fac.AntdButton(
                        '只更新statistic',
                        id='update-statistic',
                    ),
                    fac.AntdButton(
                        '更新data和statistic',
                        id='update-data-and-statistic',
                    )
                ]
            ),

            fact.AntdPie(
                id='pie-chart',
                data=initial_data,
                statistic=initial_statistic,
                angleField='value',
                colorField='type',
                radius=0.8,
                innerRadius=0.4
            )
        ]
    ),
    style={
        'padding': '50px'
    }
)


@app.callback(
    [Output('pie-chart', 'data'),
     Output('pie-chart', 'statistic')],
    [Input('update-data', 'nClicks'),
     Input('update-statistic', 'nClicks'),
     Input('update-data-and-statistic', 'nClicks')],
    [State('pie-chart', 'data'),
     State('pie-chart', 'statistic')],
    prevent_initial_call=True
)
def update_demo(nClicks1, nClicks2, nClicks3, data, statistic):

    if dash.ctx.triggered_id == 'update-data':
        return generate_mock_data()[0], dash.no_update

    elif dash.ctx.triggered_id == 'update-statistic':
        return dash.no_update, generate_mock_data()[1]

    elif dash.ctx.triggered_id == 'update-data-and-statistic':
        return generate_mock_data()


if __name__ == '__main__':
    app.run(debug=True)
