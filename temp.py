import dash
from dash import html, dcc
import feffery_antd_charts as fact
import pandas as pd
from io import StringIO

app = dash.Dash(__name__)

raw_data = '''类别,区域,销售额,备注
服装,四川,100,
日化,四川,110,
电子,四川,120,
食品,四川,130,
服装,广东,140,
日化,广东,150,
电子,广东,160,
食品,广东,170,
服装,江苏,180,
日化,江苏,190,
电子,湖北,200,
食品,湖北,210,
服装,安徽,220,
,河南,,
'''

data = pd.read_csv(StringIO(raw_data))

# 自定义区域 -> 颜色字典
region2color = {
    '四川': '#d29200',
    '广东': '#ffb900',
    '江苏': '#fff100',
    '湖北': '#d83b01',
    '安徽': '#5c005c',
    '河南': '#0078d4'
}

data.sort_values('区域', ascending=False, inplace=True)

app.layout = html.Div(
    [
        html.Div(
            fact.AntdBar(
                data=data.to_dict('records'),
                xField='销售额',
                yField='类别',
                seriesField='区域',
                isStack=True,
                color={
                    'func': '''(e) => {
                        let region2color = %s
                        
                        return region2color[e.区域]
                    }''' % str(region2color)
                }
            ),
            style={
                'height': '600px'
            }
        )
    ],
    style={
        'padding': '50px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
