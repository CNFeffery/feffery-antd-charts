import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdLiquid(
            percent=0.8,
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
