if True:
    import sys

    sys.path.append('../../')
    import dash
    import random
    from dash import html
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


app.clientside_callback(
    # 同步多个折线图之间的tooltip显示
    """
() => {

    // 获取本次回调触发来源
    let triggered_tooltip_info = dash_clientside.callback_context.triggered[0].value

    // 基于set_props()同步其余折线图tooltip显示/隐藏
    for ( let item of dash_clientside.callback_context.inputs_list[0] ) {
        if ( item.id.index !== dash_clientside.callback_context.triggered_id.index ) {
            dash_clientside.set_props(
                item.id,
                {
                    action: (
                        triggered_tooltip_info.position ?
                        {
                            type: 'tooltip:show',
                            tooltipPosition: triggered_tooltip_info.position
                        } :
                        {
                            type: 'tooltip:hide'
                        }
                    )
                }
            )
        }
    }
}
""",
    Input(
        {
            'type': 'demo-line',
            'index': ALL,
        },
        'recentlyTooltipChangeRecord',
    ),
)

if __name__ == '__main__':
    app.run(debug=True)
