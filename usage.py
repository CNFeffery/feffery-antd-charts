import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdProgress(
            height=50,
            width=300,
            autoFit=False,
            percent=0.7,
            color=['#5B8FF9', '#E8EDF3']
        ),
        fact.AntdProgress(
            height=50,
            width=300,
            autoFit=False,
            percent=0.536,
            barWidthRatio=0.3,
            color=['#F4664A', '#E8EDF3']
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
