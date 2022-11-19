if True:
    import sys
    sys.path.append('../..')
    import dash
    import demjson3
    from dash import html
    import feffery_antd_charts as fact
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

demo_data1 = demjson3.decode('''
[
    {
      year: '1991',
      value: 3,
      count: 10,
    },
    {
      year: '1992',
      value: 4,
      count: 4,
    },
    {
      year: '1993',
      value: 3.5,
      count: 5,
    },
    {
      year: '1994',
      value: 5,
      count: 5,
    },
    {
      year: '1995',
      value: 4.9,
      count: 4.9,
    },
    {
      year: '1996',
      value: 6,
      count: 35,
    },
    {
      year: '1997',
      value: 7,
      count: 7,
    },
    {
      year: '1998',
      value: 9,
      count: 1,
    },
    {
      year: '1999',
      value: 13,
      count: 20,
    },
]
''')

demo_data2 = demjson3.decode('''
[
    {
      time: '2019-03',
      value: 350,
      count: 800,
    },
    {
      time: '2019-04',
      value: 900,
      count: 600,
    },
    {
      time: '2019-05',
      value: 300,
      count: 400,
    },
    {
      time: '2019-06',
      value: 450,
      count: 380,
    },
    {
      time: '2019-07',
      value: 470,
      count: 220,
    },
  ]
''')

app.layout = html.Div(
    [
        html.Div(
            fact.AntdDualAxes(
                data=[demo_data1, demo_data1],
                xField='year',
                yField=['value', 'count'],
                geometryOptions=[
                    {
                        'geometry': 'line',
                        'color': '#5B8FF9'
                    },
                    {
                        'geometry': 'line',
                        'color': '#5AD8A6'
                    }
                ]
            ),
            style={
                'height': '400px'
            }
        ),
        html.Div(
            fact.AntdDualAxes(
                data=[demo_data2, demo_data2],
                xField='time',
                yField=['value', 'count'],
                geometryOptions=[
                    {
                        'geometry': 'column'
                    },
                    {
                        'geometry': 'line',
                        'lineStyle': {
                            'lineWidth': 2
                        }
                    }
                ]
            ),
            style={
                'height': '400px'
            }
        ),
    ],
    style={
        'padding': '25px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
