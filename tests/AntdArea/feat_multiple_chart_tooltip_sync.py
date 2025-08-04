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

app.layout = lambda: html.Div(
    [
        fact.AntdArea(
            id={'type': 'demo-area', 'index': i},
            data=[
                {
                    'date': f'2020-0{i}',
                    'y': random.randint(50, 100),
                }
                for i in range(1, 10)
            ],
            xField='date',
            yField='y',
            height=200,
            style=style(marginBottom=24),
        )
        for i in range(4)
    ],
    style=style(padding=100),
)


app.clientside_callback(
    # 同步多个面积图之间的tooltip显示
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
                        triggered_tooltip_info.data ?
                        {
                            type: 'tooltip:show',
                            tooltipPositionData: {
                                date: triggered_tooltip_info.data[0].date,
                                y: triggered_tooltip_info.data[0].y
                            }
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
            'type': 'demo-area',
            'index': ALL,
        },
        'recentlyTooltipChangeRecord',
    ),
)

if __name__ == '__main__':
    app.run(debug=True)
