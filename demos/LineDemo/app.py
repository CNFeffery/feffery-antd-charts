if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

demo_data = [{'日期': 1, '排名': 5},
             {'日期': 2, '排名': 3},
             {'日期': 3, '排名': 2},
             {'日期': 4, '排名': 1},
             {'日期': 5, '排名': 5},
             {'日期': 6, '排名': 7},
             {'日期': 8, '排名': 3}]

app.layout = html.Div(
    [
        # fact.AntdLine(
        #     data=demo_data,
        #     xField='日期',
        #     yField='排名',
        #     meta={
        #         '排名': {
        #             'alias': '指数'
        #         }
        #     },
        #     label={},
        #     smooth=True,
        #     style={
        #         'height': '250px'
        #     }
        # ),

        fact.AntdLine(
            data=[{'CHIP-ID': 'FH019040784', 'TM': '23:59:04', 'T': 45.3, 'H': 21}, {'CHIP-ID': 'FH019040784', 'TM': '23:59:14', 'T': 45.3, 'H': 21}, {'CHIP-ID': 'FH019040784', 'TM': '23:59:24', 'T': 45.3, 'H': 21},
                  {'CHIP-ID': 'FH019040784', 'TM': '23:59:34', 'T': 45.6, 'H': 21}, {'CHIP-ID': 'FH019040784', 'TM': '23:59:44', 'T': 45.3, 'H': 21}, {'CHIP-ID': 'FH019040784', 'TM': '23:59:55', 'T': 45.3, 'H': 21}],
            xField='TM',
            yField='T',
            meta={
                'TM': {
                    'type': 'cat'
                }
            },
            label={},
            smooth=True,
            style={
                'height': '250px'
            },
            slider={}
        )
    ],
    style={
        'padding': '100px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
