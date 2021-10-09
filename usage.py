import feffery_antd_charts as fact
from dash import html
import dash


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            fact.AntdLine(
                data=[
                    {
                        'x': i,
                        'y': i ** 2,
                        'series': '系列一'
                    }
                    for i in range(10)
                ] + [
                    {
                        'x': i,
                        'y': i ** 3,
                        'series': '系列二'
                    }
                    for i in range(10)
                ],
                xField='x',
                yField='y',
                smooth=True,
                seriesField='series',
                # stepType='hv',
                color={
                    'func': '''
                (ref) => {
                    if (ref.series === '系列一'){
                        return 'red'
                    }
                    return 'blue'
                }
                '''
                },
                lineStyle={
                    'lineWidth': 3,
                    'lineDash': [20, 5],
                    'lineOpacity': 0.4,
                    'shadowColor': 'rgba(0, 0, 0, 0.4)',
                    'shadowBlur': 20,
                    'shadowOffsetX': 5,
                    'shadowOffsetY': 5
                },
                padding=[80, 80, 80, 120],
                point={
                    'color': {
                        'func': '''
                        (ref) => {
                            if (ref.series === '系列一'){
                                return 'yellow'
                            }
                            return 'green'
                        }
                        '''
                    }
                },
                legend={
                    'position': 'left',
                    'layout': 'vertical'
                },
                # renderer='svg'
            ),
            style={
                'width': '1000px',
                'height': '500px',
                'padding': '200px 0 0 0',
                'border': '1px solid black'
            }
        )
    ],
    style={
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
