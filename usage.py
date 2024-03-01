import dash
import math
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fact.AntdRadialBar(
            data=[
                {
                    'name': 'X6',
                    'star': 297,
                },
                {
                    'name': 'G',
                    'star': 506,
                },
                {
                    'name': 'AVA',
                    'star': 805,
                },
                {
                    'name': 'G2Plot',
                    'star': 1478,
                },
                {
                    'name': 'L7',
                    'star': 2029,
                },
                {
                    'name': 'G6',
                    'star': 7100,
                },
                {
                    'name': 'F2',
                    'star': 7346,
                },
                {
                    'name': 'G2',
                    'star': 10178,
                },
            ],
            xField='name',
            yField='star',
            radius=0.8,
            innerRadius=0.2,
            tooltip={
                'formatter': {
                    'func': '''(datum) => {
                    return {
                        name: 'star数',
                        value: datum.star,
                    }
                }'''
                }
            }
        ),
        fact.AntdRadialBar(
            data=[
                {
                    'name': 'X6',
                    'star': 297,
                },
                {
                    'name': 'G',
                    'star': 506,
                },
                {
                    'name': 'AVA',
                    'star': 805,
                },
                {
                    'name': 'G2Plot',
                    'star': 1478,
                },
                {
                    'name': 'L7',
                    'star': 2029,
                },
                {
                    'name': 'G6',
                    'star': 7100,
                },
                {
                    'name': 'F2',
                    'star': 7346,
                },
                {
                    'name': 'G2',
                    'star': 10178,
                },
            ],
            xField='name',
            yField='star',
            radius=0.8,
            innerRadius=0.2,
            barStyle={
                'lineCap': 'round',
            }
        ),
        fact.AntdRadialBar(
            data=[
                {
                    'name': 'X6',
                    'star': 297,
                },
                {
                    'name': 'G',
                    'star': 506,
                },
                {
                    'name': 'AVA',
                    'star': 805,
                },
                {
                    'name': 'G2Plot',
                    'star': 1478,
                },
                {
                    'name': 'L7',
                    'star': 2029,
                },
                {
                    'name': 'G6',
                    'star': 7100,
                },
                {
                    'name': 'F2',
                    'star': 7346,
                },
                {
                    'name': 'G2',
                    'star': 10178,
                },
            ],
            xField='name',
            yField='star',
            radius=0.8,
            innerRadius=0.2,
            maxAngle=270,
            tooltip={
                'formatter': {
                    'func': '''(datum) => {
                    return {
                        name: 'star数',
                        value: datum.star,
                    }
                }'''
                }
            },
            colorField='star',
            color={
                'func': '''({ star }) => {
      if (star > 10000) {
        return '#36c361';
      } else if (star > 1000) {
        return '#2194ff';
      }

      return '#ff4d4f';
    }'''
            }
        ),
        fact.AntdRadialBar(
            data=[
                {
                    "year": "1991",
                    "value": 3,
                    "type": "Lon"
                },
                {
                    "year": "1992",
                    "value": 4,
                    "type": "Lon"
                },
                {
                    "year": "1993",
                    "value": 3.5,
                    "type": "Lon"
                },
                {
                    "year": "1994",
                    "value": 5,
                    "type": "Lon"
                },
                {
                    "year": "1995",
                    "value": 4.9,
                    "type": "Lon"
                },
                {
                    "year": "1996",
                    "value": 6,
                    "type": "Lon"
                },
                {
                    "year": "1997",
                    "value": 7,
                    "type": "Lon"
                },
                {
                    "year": "1998",
                    "value": 9,
                    "type": "Lon"
                },
                {
                    "year": "1999",
                    "value": 13,
                    "type": "Lon"
                },
                {
                    "year": "1991",
                    "value": 3,
                    "type": "Bor"
                },
                {
                    "year": "1992",
                    "value": 4,
                    "type": "Bor"
                },
                {
                    "year": "1993",
                    "value": 3.5,
                    "type": "Bor"
                },
                {
                    "year": "1994",
                    "value": 5,
                    "type": "Bor"
                },
                {
                    "year": "1995",
                    "value": 4.9,
                    "type": "Bor"
                },
                {
                    "year": "1996",
                    "value": 6,
                    "type": "Bor"
                },
                {
                    "year": "1997",
                    "value": 7,
                    "type": "Bor"
                },
                {
                    "year": "1998",
                    "value": 9,
                    "type": "Bor"
                },
                {
                    "year": "1999",
                    "value": 13,
                    "type": "Bor"
                }
            ],
            xField='year',
            yField='value',
            colorField='type',
            isStack=True,
            maxAngle=270
        ),
        fact.AntdRadialBar(
            data=[
                {
                    "year": "1991",
                    "value": 3,
                    "type": "Lon"
                },
                {
                    "year": "1992",
                    "value": 4,
                    "type": "Lon"
                },
                {
                    "year": "1993",
                    "value": 3.5,
                    "type": "Lon"
                },
                {
                    "year": "1994",
                    "value": 5,
                    "type": "Lon"
                },
                {
                    "year": "1995",
                    "value": 4.9,
                    "type": "Lon"
                },
                {
                    "year": "1996",
                    "value": 6,
                    "type": "Lon"
                },
                {
                    "year": "1997",
                    "value": 7,
                    "type": "Lon"
                },
                {
                    "year": "1998",
                    "value": 9,
                    "type": "Lon"
                },
                {
                    "year": "1999",
                    "value": 13,
                    "type": "Lon"
                },
                {
                    "year": "1991",
                    "value": 3,
                    "type": "Bor"
                },
                {
                    "year": "1992",
                    "value": 4,
                    "type": "Bor"
                },
                {
                    "year": "1993",
                    "value": 3.5,
                    "type": "Bor"
                },
                {
                    "year": "1994",
                    "value": 5,
                    "type": "Bor"
                },
                {
                    "year": "1995",
                    "value": 4.9,
                    "type": "Bor"
                },
                {
                    "year": "1996",
                    "value": 6,
                    "type": "Bor"
                },
                {
                    "year": "1997",
                    "value": 7,
                    "type": "Bor"
                },
                {
                    "year": "1998",
                    "value": 9,
                    "type": "Bor"
                },
                {
                    "year": "1999",
                    "value": 13,
                    "type": "Bor"
                }
            ],
            xField='year',
            yField='value',
            colorField='type',
            isGroup=True,
            maxAngle=270
        ),
        fact.AntdRadialBar(
            data=[
                {
                    'name': 'X6',
                    'star': 297,
                },
                {
                    'name': 'G',
                    'star': 506,
                },
                {
                    'name': 'AVA',
                    'star': 805,
                },
                {
                    'name': 'G2Plot',
                    'star': 1478,
                },
                {
                    'name': 'L7',
                    'star': 2029,
                },
                {
                    'name': 'G6',
                    'star': 7100,
                },
                {
                    'name': 'F2',
                    'star': 7346,
                },
                {
                    'name': 'G2',
                    'star': 10178,
                },
            ],
            xField='name',
            yField='star',
            maxAngle=350,
            radius=0.8,
            innerRadius=0.2,
            tooltip={
                'formatter': {
                    'func': '''(datum) => {
        return {
          name: 'star数',
          value: datum.star,
        };
      }'''
                },
            },
            colorField='star',
            color={
                'func': '''({star}) => {
                if (star > 10000) {
                    return '#6349ec'
                } else if (star > 1000) {
                    return '#ff9300'
                }

                return '#ff93a7'
            }'''
            },
            barBackground={},
            barStyle={
                'lineCap': 'round',
            }
        ),
        fact.AntdRadialBar(
            data=[
                {
                    'term': 'Zombieland',
                    'count': 9,
                },
                {
                    'term': 'Wieners',
                    'count': 8,
                },
                {
                    'term': 'Toy Story',
                    'count': 8,
                },
                {
                    'term': 'trashkannon',
                    'count': 7,
                },
                {
                    'term': 'the GROWLERS',
                    'count': 6,
                },
                {
                    'term': 'mudweiser',
                    'count': 6,
                },
                {
                    'term': 'ThunderCats',
                    'count': 4,
                },
                {
                    'term': 'The Taqwacores - Motion Picture',
                    'count': 4,
                },
                {
                    'term': 'The Shawshank Redemption',
                    'count': 2,
                },
                {
                    'term': 'The Olivia Experiment',
                    'count': 1,
                },
            ],
            xField='term',
            yField='count',
            radius=1,
            innerRadius=0.4,
            startAngle=0.5 * math.pi,
            endAngle=2.5 * math.pi,
            tooltip={
                'showMarkers': True,
            },
            type='line',
            annotations=[
                {
                    'type': 'text',
                    'position': ['50%', '50%'],
                    'content': 'Music',
                    'style': {
                        'textAlign': 'center',
                        'fontSize': 24,
                    },
                },
            ]
        )
    ][::-1],
    style={
        'padding': '50px 100px',
        'display': 'flex',
        'flexDirection': 'column',
        'gap': 100
    }
)

if __name__ == '__main__':
    app.run(debug=True)
