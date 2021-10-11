## Antd Charts参数文档



### 1 制图参数

#### 1.1 图表容器

- style

  object型，设置图表容器的样式

- className

  string型，设置图表容器的类

- width

  number型，默认400，设置图表像素宽度

- height

  number型，默认400，设置图表像素高度

- autoFit

  boolean型，默认true，设置图表是否自适应容器宽高，为true时会屏蔽width与height的效果

- padding

  number、number[]或'auto'，设置图表画布的padding值，代表图表在*上右下左*的像素间距，单个数字输入时同时定义四个方向，四个数字组成的数组输入时分别代表四个方向

- appendPadding

  number、number[]型，用于在padding的基础上额外增加四个方向上的留白间距

- renderer

  string型，默认为'canvas'，设置图表的渲染方式，可选的有'canvas'和'svg'

- limitInPlot

  boolean型，设置是否对超出坐标系范围的Geometry进行剪切

- locale

  string型，设置语言，可选的有'zh-CN'和'en-US'

#### 1.2 数据映射

- data

  array[object]型，设置图表数据源，数据源为对象数组，例如：

  ```javascript
  const data = [
    { time: '1991'，value: 20 },
    { time: '1992'，value: 20 },
  ];
  ```

- xField

  string型，基于data，设置图表x轴数据字段名

- yField

  string型，基于data，设置图表y轴数据字段名

- seriesField

  string型，基于data，设置图表分组依据的字段名，支持的图表类型有**折线图**

#### 1.3 图形样式

- smooth

  boolean型，默认为false，设置图表中曲线是否平滑，支持的图表类型有**折线图**

- stepType

  string型，设置阶梯折线图类型，配置后会屏蔽smooth的效果，可选的有'hv'、'vh'、'hvh'和'vhv'，'h'代表水平方向，'v'代表竖直方向，譬如'vh'就代表先竖直再水平，支持的图表类型有**折线图**

- isStack

  boolean型，默认为false，在seriesField配置时，设置isStack=true可以堆叠显示折线，支持的图表类型有**折线图**

- color

  string、string[]或function，用于统一设置图形的颜色方案，输入单个css色彩字符串代表单色方案，传入多个css色彩字符串数组代表调色盘方案，传入function代表自定义回调函数，来基于seriesField输入来自由映射颜色，例如：

  ```javascript
  color: (ref) => {
      if(ref.分组字段名称 === 'male'){
          return 'red';
      }
      return 'yellow';
  }
  ```
  支持的图表类型有**折线图**
  
- lineStyle

  object、function，用于设置折线图线型等样式，适用的二级属性有：

  - lineWidth

    number型，设置折线的像素宽度

  - lineDash

    [number, number]，用于设置折线的虚线样式，格式为[分段像素长度, 分段像素间距]

  - lineOpacity

    number型，0~1之间，设置折线的透明度

  - shadowColor

    string型，设置折线阴影颜色

  - shadowBlur

    number型，设置折线阴影的高斯模糊系数，越大越模糊

  - shadowOffsetX

    number型，设置阴影相对折线的水平偏移像素距离

  - shadowOffsetY

    number型，设置阴影相对折线的竖直偏移像素距离

  - cursor

    string型，默认为'default'，同css中的cursor属性，用于设置鼠标悬浮于折线上时的鼠标样式
  
  当输入function时，可以基于seriesField，自定义回调映射折线样式，例如：
  
  ```javascript
  (ref) => {
      if (ref.分组字段名称 === 'a'){
          return {
              lineDash: [4, 4],
              opacity: 1,
          };
      }
      return { opacity: 0.5 };
  }
  ```
  
  支持的图表类型有**折线图**
  
- point

  object型，用于设置折线图点样式，适用的二级属性有：

  - color

    string、string[]、function型，设置数据点颜色，使用方式同一级属性color

  - shape

    string、function型，设置数据点形状，使用方式同一级属性color，可选的形状有'circle'、'square'、'line'、'diamond'、'triangle'、'triangle-down'、'hexagon'、'bowtie'、'cross'、'tick'、'plus'、'hyphen'

  - style

    object、function型，设置数据点详细样式，使用方式同一级属性color，适用的三级属性有：

    - r

      number型，设置点半径像素大小

    - fill

      string型，设置点填充颜色

    - fillOpacity

      number型，设置点填充色透明度

    - stroke

      string型，设置点轮廓色

    - lineWidth

      string型，设置点轮廓像素宽度

    - lineDash

      [number, number]，设置点轮廓线型

    - strokeOpacity

      number，设置点轮廓透明度
    
    - cursor
  
      string型，默认为'default'，同css中的cursor属性，用于设置鼠标悬浮于点上时的鼠标样式
  
  支持的图表类型有**折线图**
  
- 

  

  

  


​    

​    

  





  


