import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdPie(
            data=[
                {
                    'type': 'A',
                    'value': 1
                },
                {
                    'type': 'B',
                    'value': 1
                },
                {
                    'type': 'C',
                    'value': 1
                }
            ],
            angleField='value',
            colorField='type',
            pattern={
                'func': '''(e) => {
                    if ( e.type === 'A' ) {
                        return {
                            type: 'dot'
                        }
                    } else if ( e.type === 'B' ) {
                        return {
                            type: 'line'
                        }
                    }
                    return {
                        'type': 'square'
                    };
                }'''
            }
        )
    ],
    style={
        'padding': 50
    }
)

if __name__ == '__main__':
    app.run(debug=True)
