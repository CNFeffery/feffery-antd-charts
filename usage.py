import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdColumn(
            data=[{'x': i, 'y': i} for i in range(10)],
            xField='x',
            yField='y',
            pattern={
                'func': '''(e) => {
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
