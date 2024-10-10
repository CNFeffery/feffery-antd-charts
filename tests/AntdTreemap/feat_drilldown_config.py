if True:
    import sys

    sys.path.append('../../')
    import dash
    import requests
    from dash import html
    import feffery_antd_charts as fact
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    fact.AntdTreemap(
        data=requests.get(
            'https://gw.alipayobjects.com/os/antfincdn/k5SYI%24mOo1/treemap.json'
        ).json(),
        colorField='name',
        legend={
            'position': 'top-left',
        },
        animation={},
        drilldown={
            'enabled': True,
            'breadCrumb': {
                'position': 'top-left',
                'rootText': '根节点',
                'dividerText': '->',
                'textStyle': {'fontSize': 15},
                'activeTextStyle': {'fill': 'red'},
            },
        },
        height=600,
    ),
    style=style(padding=100),
)

if __name__ == '__main__':
    app.run(debug=True)
