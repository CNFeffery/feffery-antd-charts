if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

demo_data = [{'类型': '分类1', '排名': 59999},
             {'类型': '分类2', '排名': 39999},
             {'类型': '分类3', '排名': 29999},
             {'类型': '分类4', '排名': 19999},
             {'类型': '分类5', '排名': 59999},
             {'类型': '分类6', '排名': 79999},
             {'类型': '分类8', '排名': 39999}]

app.layout = html.Div(
    [
        fact.AntdColumn(
            data=demo_data,
            xField='类型',
            yField='排名',
            meta={
                '日期': {
                    'type': 'cat'
                }
            },
            label={
                'position': 'top'
            },
            style={
                'height': '250px'
            },
            yAxis={
                'max': 100000
            }
        )
    ],
    style={
        'padding': '100px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)