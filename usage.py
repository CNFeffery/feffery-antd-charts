import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdRingProgress(
            height=100,
            width=100,
            autoFit=False,
            percent=0.7,
            color=['#5B8FF9', '#E8EDF3']
        ),
        fact.AntdRingProgress(
            height=100,
            width=100,
            autoFit=False,
            percent=0.6,
            color=['#F4664A', '#E8EDF3'],
            innerRadius=0.85,
            radius=0.98,
            statistic={
                'title': {
                    'style': {
                        'color': '#363636',
                        'fontSize': '12px',
                        'lineHeight': '14px',
                    },
                    'formatter': {
                        'func': "()=> '进度'"
                    },
                },
            }
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
