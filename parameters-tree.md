## Feffery-Antd-Charts参数设计文档



### 1 制图参数

#### 1.1 基础ShapeAttrs

在`Ant Design Charts`中，针对不同的数据映射视觉元素，可归纳为以下几种类型：

##### 1.1.1 点要素

```javascript
// 定义点通用style参数模板
const pointBaseStyle = PropTypes.exact({
    // 设置点半径像素大小
    r: PropTypes.number,

    // 设置点填充色
    fill: PropTypes.string,

    // 设置点填充色透明度
    fillOpacity: PropTypes.number,

    // 设置点描边色彩
    stroke: PropTypes.string,

    // 设置点描边像素宽度
    lineWidth: PropTypes.number,

    // 设置点描边线型
    lineDash: PropTypes.arrayOf(PropTypes.number),

    // 设置点描边透明度
    strokeOpacity: PropTypes.number,

    // 设置鼠标悬浮点上时的样式
    cursor: PropTypes.string
})
```

##### 1.1.2 线要素

```javascript
// 定义线通用style参数模版
const lineBaseStyle = PropTypes.exact({
    // 设置线像素宽度
    lineWidth: PropTypes.number,

    // 设置线的虚线样式，可以指定一个数组。一组描述交替绘制线段和间距（坐标空间单位）长度的数字。 
    // 如果数组元素的数量是奇数， 数组的元素会被复制并重复。例如， [5, 15, 25] 会变成 [5, 15, 25, 5, 15, 25]
    lineDash: PropTypes.arrayOf(PropTypes.number),

    // 设置线末端样式，可选的有'butt'、'round'、'square'
    lineCap: PropTypes.string,

    // 设置线的透明度
    lineOpacity: PropTypes.number,

    // 设置线的阴影颜色
    shadowColor: PropTypes.string,

    // 设置线的阴影的高斯模糊系数
    shadowBlur: PropTypes.number,

    // 设置线的阴影相对线的水平偏移距离
    shadowOffsetX: PropTypes.number,

    // 设置线的阴影相对线的竖直偏移距离
    shadowOffsetY: PropTypes.number,

    // 设置鼠标悬浮线上时的css样式
    cursor: PropTypes.string
})
```

##### 1.1.3 文字要素

```javascript
// 定义文字通用style参数模版
const textBaseStyle = PropTypes.exact({
    // 设置文字内容的当前对齐方式，可选的有'start'、'center'、'end'、'left'、'right'
    textAlign: PropTypes.string,

    // 设置在绘制文本时使用的当前文本基线, 可选的有'top', 'hanging', 'middle', 'alphabetic', 'ideographic', 'bottom'
    textBaseline: PropTypes.string,

    // 设置字体样式，可选的有'normal', 'italic', 'oblique'
    fontStyle: PropTypes.string,

    // 设置字体像素行高
    lineHeight: PropTypes.number,

    // 设置文字像素大小
    fontSize: PropTypes.number,

    // 设置文字字体
    fontFamily: PropTypes.string,

    // 设置文字粗细水平
    fontWeight: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.number
    ]),

    // 设置文字颜色
    fill: PropTypes.string,

    // 设置文字颜色透明度
    fillOpacity: PropTypes.number,

    // 设置文字轮廓色
    stroke: PropTypes.string,

    // 设置文字轮廓像素宽度
    lineWidth: PropTypes.number,

    // 设置文字轮廓线型，格式为[分段长度, 分段间距]
    lineDash: PropTypes.arrayOf(PropTypes.number),

    // 设置文字阴影颜色
    shadowColor: PropTypes.string,

    // 设置文字阴影x方向偏移距离
    shadowOffsetX: PropTypes.number,

    // 设置文字阴影y方向偏移距离
    shadowOffsetY: PropTypes.number,

    // 设置文字阴影高斯模糊系数，越大越模糊
    shadowBlur: PropTypes.number,

    // 设置文字鼠标悬浮css样式
    cursor: PropTypes.string
})
```

#### 1.2 整体样式

- theme

  string、object型，设置图表整体的主题风格，字符串输入时可选的有'default'、'dark'

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

#### 1.3 数据映射

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

#### 1.4 图形样式

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

<a id='lineStyle'></a>

- lineStyle

  object、{func: string}，用于设置折线图线型等样式，接受的参数对应[线要素](#####1.1.2 线要素)：

  亦可基于数据字段进行回调，例如：

  ```javascript
  (ref) => {
      if (ref.字段名称 === 'a'){
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

  object型，用于设置点样式，接受的参数有：

  - color

    string、string[]、{func: string}型，设置数据点颜色，回调使用方式同[lineStyle](#lineStyle)

  - shape

    string、{func: string}型，设置数据点形状，回调使用方式同[lineStyle](#lineStyle)，可选的形状有'circle'、'square'、'line'、'diamond'、'triangle'、'triangle-down'、'hexagon'、'bowtie'、'cross'、'tick'、'plus'、'hyphen'

  - style

    object、{func: string}型，设置点样式，接受的参数对应[点要素](#####1.1.1 点要素)：

    亦可基于数据字段进行回调，例如：

    ```javascript
  (ref) => {
        if (ref.字段名称 === 'a'){
          return {
                r: 10
          };
        }
      return { r: 2 };
    }
  ```
  
  支持的图表类型有**折线图**
  
- xAxis/yAxis

  object型，设置坐标轴相关属性，接受的参数有：

  - top

    boolean型，默认false，设置是否将对应坐标轴渲染于画布顶层，从而避免部分图表坐标轴被图形遮挡
  
  - position
  
    string型，适用于*直角坐标系*，设置坐标轴的位置，可选的有'top'、'bottom'、'left'、'right'，其中xAxis适用'bottom'、'top'；yAxis适用'left'、'right'
  
  - title
  
    object型，用配置标题内容，可用的三级属性有：
  
    - title
  
      string型，设置对应坐标轴的标题文字
  
    - position
  
      string型，设置标题对齐位置，可选的有'start'、'center'、'end'
  
    - offset
  
      number型，设置标题距离坐标轴的像素距离
  
    - spacing
  
      number型，设置标题距离坐标轴文本的距离
  
    - autoRotate
  
      boolean型，设置是否自动旋转标题
  
    - style
  
      object型，用于自定义文本的样式属性，适用的属性有：
  
      - fontSize
  
        number型，设置文字像素大小
  
      - fontFamily
  
        string型，设置文字字体
  
      - fontWeight
  
        number、string型，同css中的font-weight，设置字体粗细水平
  
      - fill
  
        string型，设置文字颜色
  
      - fillOpacity
  
        number型，设置文字颜色透明度
  
      - stroke
  
        string型，设置文字轮廓色
  
      - lineWidth
  
        number型，设置文字轮廓像素宽度
  
      - lineDash
  
        [number, number]，设置文字描边线型
  
      - shadowColor
  
        string型，设置文字阴影颜色
  
      - shadowOffsetX
  
        number型，设置文字阴影x方向偏移距离
  
      - shadowOffsetY
  
        number型，设置文字阴影y方向偏移距离
  
      - shadowBlur
  
        number型，设置文字阴影高斯模糊系数，越大越模糊
  
      - cursor
  
        string型，设置文字鼠标悬浮时的css样式
  
  
  
  
  
  


​    

​    

  





  

