if True:
    import sys

    sys.path.append('../../')
    import dash
    import random
    from dash import html, set_props
    import feffery_antd_charts as fact
    from dash.dependencies import Input, ALL
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fact.AntdLine(
            id={'type': 'demo-line', 'index': i},
            data=[
                {
                    'date': f'2020-0{i}',
                    'y': random.randint(50, 100),
                }
                for i in range(1, 10)
            ],
            xField='date',
            yField='y',
            height=100,
            xAxis=False if i < 5 else {},
            smooth=True,
            style=style(marginBottom=24),
        )
        for i in range(6)
    ],
    style=style(padding=100),
)


@app.callback(
    Input(
        {
            'type': 'demo-line',
            'index': ALL,
        },
        'recentlyTooltipChangeRecord',
    )
)
def sync_tooltip(*args):
    """同步多个折线图之间的tooltip显示，仅用作功能测试，实际应用建议更换为浏览器端回调实现"""

    triggered_tooltip_info = dash.ctx.triggered[0]['value']

    for item in dash.ctx.inputs_list[0]:
        if (
            item['id']['index']
            != dash.ctx.triggered_id['index']
        ):
            set_props(
                item['id'],
                {
                    'action': {
                        'type': 'tooltip:show',
                        'tooltipPositionData': triggered_tooltip_info[
                            'data'
                        ][0],
                    }
                    if triggered_tooltip_info['data']
                    else {
                        'type': 'tooltip:hide',
                    },
                },
            )


if __name__ == '__main__':
    app.run(debug=True)
