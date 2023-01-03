import PropTypes from 'prop-types';


// 定义基于g2及g2plot的ShapeAttrs的相关参数模板，参考：
// https://g2.antv.vision/zh/docs/api/shape/shape-attrs
// https://antv-g2plot.gitee.io/zh/docs/api/graphic-style

// 定义全局通用style参数模板
const baseStyle = PropTypes.exact({

    // 定义矩形圆角像素程度，number或[number, number, number, number]
    radius: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number)
    ]),

    // 设置点半径像素大小
    r: PropTypes.number,

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

    // 设置填充色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    // 图形纹理填充方式配置格式：
    //     格式如：'p(a)https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*58XjQY1tO7gAAAAAAAAAAABkARQnAQ'
    //     其中a表示“该模式在水平和垂直方向重复”，其他可选的模式有：
    //         x：“该模式只在水平方向重复”
    //         y：“该模式只在垂直方向重复”
    //         n：“该模式只显示一次（不重复）”
    fill: PropTypes.string,

    // 设置填充色透明度
    fillOpacity: PropTypes.number,

    // 设置描边色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    stroke: PropTypes.string,

    lineWidth: PropTypes.number,

    lineDash: PropTypes.arrayOf(PropTypes.number),

    lineOpacity: PropTypes.number,

    opacity: PropTypes.number,

    // 设置阴影填充色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    // 图形纹理填充方式配置格式：
    //     格式如：'p(a)https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*58XjQY1tO7gAAAAAAAAAAABkARQnAQ'
    //     其中a表示“该模式在水平和垂直方向重复”，其他可选的模式有：
    //         x：“该模式只在水平方向重复”
    //         y：“该模式只在垂直方向重复”
    //         n：“该模式只显示一次（不重复）”
    shadowColor: PropTypes.string,

    shadowBlur: PropTypes.number,

    shadowOffsetX: PropTypes.number,

    shadowOffsetY: PropTypes.number,

    cursor: PropTypes.string
})


// 定义点通用style参数模板
const pointBaseStyle = PropTypes.exact({
    // 设置点半径像素大小
    r: PropTypes.number,

    // 设置填充色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    // 图形纹理填充方式配置格式：
    //     格式如：'p(a)https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*58XjQY1tO7gAAAAAAAAAAABkARQnAQ'
    //     其中a表示“该模式在水平和垂直方向重复”，其他可选的模式有：
    //         x：“该模式只在水平方向重复”
    //         y：“该模式只在垂直方向重复”
    //         n：“该模式只显示一次（不重复）”
    fill: PropTypes.string,

    // 设置全局透明度
    opacity: PropTypes.number,

    // 设置点填充色透明度
    fillOpacity: PropTypes.number,

    // 设置轮廓色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
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

// 定义线通用style参数模版
const lineBaseStyle = PropTypes.exact({

    // 设置线条色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    stroke: PropTypes.string,

    // 设置全局透明度
    opacity: PropTypes.number,

    // 设置线像素宽度
    lineWidth: PropTypes.number,

    // 设置线的虚线样式，可以指定一个数组。一组描述交替绘制线段和间距（坐标空间单位）长度的数字。 
    // 如果数组元素的数量是奇数， 数组的元素会被复制并重复。例如， [5, 15, 25] 会变成 [5, 15, 25, 5, 15, 25]
    lineDash: PropTypes.arrayOf(PropTypes.number),

    // 设置线末端样式，可选的有'butt'、'round'、'square'
    lineCap: PropTypes.string,

    // 设置线的透明度
    lineOpacity: PropTypes.number,

    // 设置阴影色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    // 图形纹理填充方式配置格式：
    //     格式如：'p(a)https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*58XjQY1tO7gAAAAAAAAAAABkARQnAQ'
    //     其中a表示“该模式在水平和垂直方向重复”，其他可选的模式有：
    //         x：“该模式只在水平方向重复”
    //         y：“该模式只在垂直方向重复”
    //         n：“该模式只显示一次（不重复）”
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

// 定义面style参数模板
const areaBaseStyle = PropTypes.exact({

    // 设置填充色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    // 图形纹理填充方式配置格式：
    //     格式如：'p(a)https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*58XjQY1tO7gAAAAAAAAAAABkARQnAQ'
    //     其中a表示“该模式在水平和垂直方向重复”，其他可选的模式有：
    //         x：“该模式只在水平方向重复”
    //         y：“该模式只在垂直方向重复”
    //         n：“该模式只显示一次（不重复）”
    fill: PropTypes.string,

    fillOpacity: PropTypes.number,

    opacity: PropTypes.number,

    // 设置阴影色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    // 图形纹理填充方式配置格式：
    //     格式如：'p(a)https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*58XjQY1tO7gAAAAAAAAAAABkARQnAQ'
    //     其中a表示“该模式在水平和垂直方向重复”，其他可选的模式有：
    //         x：“该模式只在水平方向重复”
    //         y：“该模式只在垂直方向重复”
    //         n：“该模式只显示一次（不重复）”
    shadowColor: PropTypes.string,

    shadowBlur: PropTypes.number,

    shadowOffsetX: PropTypes.number,

    shadowOffsetY: PropTypes.number,

    cursor: PropTypes.string
})

// 定义文字通用style参数模版
const textBaseStyle = PropTypes.exact({

    // 设置全局透明度
    opacity: PropTypes.number,

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

    // 设置文字填充色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    // 图形纹理填充方式配置格式：
    //     格式如：'p(a)https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*58XjQY1tO7gAAAAAAAAAAABkARQnAQ'
    //     其中a表示“该模式在水平和垂直方向重复”，其他可选的模式有：
    //         x：“该模式只在水平方向重复”
    //         y：“该模式只在垂直方向重复”
    //         n：“该模式只显示一次（不重复）”
    fill: PropTypes.string,

    // 设置文字颜色透明度
    fillOpacity: PropTypes.number,

    // 设置文字轮廓色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    stroke: PropTypes.string,

    // 设置文字轮廓像素宽度
    lineWidth: PropTypes.number,

    // 设置文字轮廓线型，格式为[分段长度, 分段间距]
    lineDash: PropTypes.arrayOf(PropTypes.number),

    // 设置阴影色彩，常规单一色彩格式同css色彩
    // 渐变色配置格式：
    //     线性渐变：设置角度及不同断点处的色彩值，如'l(0) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'
    //     环形渐变：设置渐变圆对应的圆心x、y坐标及半径值，并设置不同断点处的色彩值，如'r(0.5, 0.5, 0.1) 0:#ffffff 1:#1890ff'
    // 图形纹理填充方式配置格式：
    //     格式如：'p(a)https://gw.alipayobjects.com/mdn/rms_d314dd/afts/img/A*58XjQY1tO7gAAAAAAAAAAABkARQnAQ'
    //     其中a表示“该模式在水平和垂直方向重复”，其他可选的模式有：
    //         x：“该模式只在水平方向重复”
    //         y：“该模式只在垂直方向重复”
    //         n：“该模式只显示一次（不重复）”
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


// 定义全局化配置图表数据元信息PropTypes模板，其中原始字段名为属性名
const metaBasePropTypes = PropTypes.objectOf(
    PropTypes.exact({
        // 设置字段别名
        alias: PropTypes.string,

        // 设置特殊的字段信息格式化处理回调
        formatter: PropTypes.oneOfType([
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            }),
            PropTypes.any
        ]),

        // 枚举该字段下所有值
        values: PropTypes.arrayOf(PropTypes.string),

        // 设置该字段的数据映射区间，默认为[0, 1]
        range: PropTypes.arrayOf(PropTypes.number),

        // 指定字段度量类型，可选的有：
        // cat: 分类度量
        // timeCat: 时间分类度量
        // linear: 线性度量
        // time: 连续的时间度量
        // log: 对数度量
        // pow: 幂数度量
        // quantize: 分段度量，用户可以指定不均匀的分段
        // quantile: 等分度量，根据数据的分布自动计算分段
        // identity: 常量度量
        type: PropTypes.oneOf([
            'cat', 'timeCat', 'linear', 'linear', 'time', 'log',
            'pow', 'quantize', 'quantile', 'identity'
        ]),

        // 定义域下限
        min: PropTypes.number,

        // 定义域上限
        max: PropTypes.number
    })
)

// 定义坐标轴通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/axis
const axisBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.exact({
        // 默认false，设置是否将对应坐标轴渲染于画布顶层，从而避免部分图表坐标轴被图形遮挡
        top: PropTypes.bool,

        // 设置坐标轴绘图范围，譬如[0, 1]代表撑满
        range: PropTypes.arrayOf(PropTypes.number),

        // 适用于*直角坐标系*，设置坐标轴方位，可选的有'top'、'bottom'、'left'、'right'
        position: PropTypes.string,

        // 设置坐标轴标题
        title: PropTypes.exact({
            // 设置标题文字内容
            text: PropTypes.string,

            // 设置标题文字样式属性
            style: textBaseStyle,

            // 设置坐标轴标题的对其位置，可选的有'center'、'start'、'end'
            position: PropTypes.string,

            // 设置坐标轴标题距离坐标轴的像素距离
            offset: PropTypes.number,

            // 设置坐标轴标题距离坐标轴文字标签的像素距离
            spacing: PropTypes.number,

            // 设置是否自动旋转
            autoRotate: PropTypes.bool
        }),

        // 设置坐标轴文本标签
        label: PropTypes.oneOfType([
            PropTypes.oneOf([false]),
            PropTypes.exact({

                // 设置label的偏移量
                offset: PropTypes.number,

                // 设置label相对于数据点在水平方向的偏移像素距离
                offsetX: PropTypes.number,

                // 设置label相对于数据点在竖直方向的偏移像素距离
                offsetY: PropTypes.number,

                // 设置label标题文字样式属性
                style: textBaseStyle,

                // 设置是否自动旋转
                autoRotate: PropTypes.bool,

                // 设置文本旋转角度
                rotate: PropTypes.number,

                // 只对极坐标下的文本生效，表示文本是否按照角度进行放射状显示，true表示开启，false表示关闭
                labelEmit: PropTypes.bool,

                // 设置当前文字标签相对于数据点的位置，可选的有'top'、'bottom'、'middle'、'left'、'right'
                position: PropTypes.string,

                // 设置文字标签的格式化显示回调函数
                formatter: PropTypes.oneOfType([
                    PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string
                    }),
                    PropTypes.any
                ]),

                // 设置是否自动隐藏，默认为false
                autoHide: PropTypes.bool
            })
        ]),

        // 设置坐标轴线样式
        line: PropTypes.exact({
            style: lineBaseStyle
        }),

        // 设置坐标轴网格线
        grid: PropTypes.exact({
            // 设置线要素样式
            line: PropTypes.exact({
                // 线要素样式
                style: lineBaseStyle,
                // 类型，可选的有'line'、'circle'
                type: PropTypes.oneOf(['line', 'circle'])
            }),

            // 设置两个栅格线之间的填充色
            alternateColor: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.arrayOf(PropTypes.string)
            ]),

            // 设置网格线是否与刻度线对齐，若设置为false，则会显示在两个刻度线之间
            alignTick: PropTypes.bool,

            // 设置对于circle是否关闭grid
            closed: PropTypes.bool
        }),

        // 设置坐标轴刻度线
        tickLine: PropTypes.exact({
            // 设置坐标轴刻度线样式
            style: lineBaseStyle,

            // 设置坐标轴刻度线是否与tick对齐
            alignTick: PropTypes.bool,

            // 设置坐标轴刻度线长度
            length: PropTypes.number
        }),

        // 设置坐标轴子刻度线
        subTickLine: PropTypes.exact({
            // 设置坐标轴刻度线样式
            style: lineBaseStyle,

            // 设置子刻度线数量
            count: PropTypes.number,

            // 设置坐标轴刻度线长度
            length: PropTypes.number
        }),

        // 设置是否进行美化，默认为true
        nice: PropTypes.bool,

        // 设置坐标轴最小值，默认为0
        min: PropTypes.number,

        // 设置坐标轴最大值
        max: PropTypes.number,

        // 设置最小值限定
        minLimit: PropTypes.number,

        // 设置最大值限定
        maxLimit: PropTypes.number,

        // 设置期望的坐标轴刻度数量
        tickCountL: PropTypes.number,

        // 设置坐标轴刻度间隔
        tickInterval: PropTypes.number
    })
])


// 定义legend通用PropTypes模板，设置为false表示关闭legend
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/legend
const legendBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.exact({
        // 设置图例位置，可选的有'top'、'top-left'、'top-right'、'left'、'left-top'、
        // 'left-bottom'、'right'、'right-top'、'right-bottom'、'bottom'、'bottom-left'及'bottom-right'
        position: PropTypes.string,

        // 设置图例布局方式，可选的有'horizontal'及'vertical'
        layout: PropTypes.string,

        // 设置是否启用图例交互指示器，默认为true
        radio: PropTypes.bool,

        // 设置图例标题
        title: PropTypes.exact({
            // 设置图例标题内容
            text: PropTypes.string,

            // 设置图例与图例项之间的像素距离
            spacing: PropTypes.number,

            // 设置图例标题文字的样式
            style: textBaseStyle
        }),

        // 设置图例整体在x方向上的偏移
        offsetX: PropTypes.number,

        // 设置图例整体在y方向上的偏移
        offsetY: PropTypes.number,

        // 配置背景框
        background: PropTypes.exact({
            // 设置背景框内部留白宽度
            padding: PropTypes.oneOfType([
                PropTypes.number,
                PropTypes.arrayOf(PropTypes.number)
            ])
        }),

        // 适用于分类图例的相关参数

        // 在图例元素较多时设置是否分页
        flipPage: PropTypes.bool,

        // 设置图例项最大宽度值，当layout设置为'horizontal'且图例项宽度总和超出maxWidth时
        // 会强制激活flipPage: true进行分页展示
        maxWidth: PropTypes.number,

        // 设置图例项最大高度值，当layout设置为'vertical'且图例项高度总和超出maxHeight时
        // 会强制激活flipPage: true进行分页展示
        maxHeight: PropTypes.number,

        // 设置是否以逆序方式展示图例项
        reversed: PropTypes.bool,

        // 设置图例的高度，默认为null
        itemHeight: PropTypes.number,

        // 设置图例的宽度，默认为null
        itemWidth: PropTypes.number,

        // 设置图例文本的相关格式
        itemName: PropTypes.exact({
            // 设置图例项marker同后面name的间距
            spacing: PropTypes.number,

            // 设置文本样式
            style: textBaseStyle,

            // 回调设置文字内容
            formatter: PropTypes.oneOfType([
                PropTypes.exact({
                    // 回调模式
                    func: PropTypes.string,
                }),
                PropTypes.any
            ])
        }),

        // 设置图例数值的相关格式
        itemValue: PropTypes.exact({
            // 设置是否右对齐，默认为false，仅当设置图例项宽度时生效
            alignRight: PropTypes.bool,

            // 设置文本样式
            style: textBaseStyle,

            // 回调设置文字内容
            formatter: PropTypes.oneOfType([
                PropTypes.exact({
                    // 回调模式
                    func: PropTypes.string,
                }),
                PropTypes.any
            ])
        }),

        // 设置图例项水平方向的间距
        itemSpacing: PropTypes.number,

        // 用于自定义图例的高亮状态，譬如：
        // selected: {
        //     '分类一': true,
        //     '分类二': false,
        //     '分类三': false,
        // }
        selected: PropTypes.object,

        // 适用于连续图例的相关参数

        // 设置图例选择范围的最小值
        min: PropTypes.number,

        // 设置图例选择范围的最大值
        max: PropTypes.number,

        // 设置图例当前停留位置对应的值
        value: PropTypes.number,

        // 设置图例滑块是否可滑动
        slidable: PropTypes.bool,

        // 配置图例滑轨的样式
        rail: PropTypes.exact({
            // 设置图例滑轨的类型，可选的有'color'、'size'
            type: PropTypes.string,

            // 设置图例滑轨的像素宽度
            size: PropTypes.number,

            // 设置图例滑轨的默认长度，默认为100，当设置了maxWidth、maxHeight时，此参数失效
            defaultLength: PropTypes.number,

            // 设置图例滑轨的样式
            style: baseStyle
        }),

        // 配置图例滑轨选择范围的样式
        track: PropTypes.exact({
            style: baseStyle
        }),

        // 配置图例滑轨滑块的样式
        handler: PropTypes.exact({
            // 设置图例滑轨滑块的尺寸大小，默认为10
            size: PropTypes.number,

            // 设置图例滑轨滑块的样式
            style: baseStyle
        }),

        // 设置是否启用自定义图例模式，默认为false
        // 设置为true时需配合items属性使用
        custom: PropTypes.bool,

        // 适用于分类图例，用于自定义图例项内容
        items: PropTypes.arrayOf(
            PropTypes.exact({
                // 图例名称，必填
                name: PropTypes.string.isRequired,
                // 图例值
                value: PropTypes.string.isRequired,
                // 配置图形标记
                marker: PropTypes.exact({
                    // 设置图例图形类型
                    // 可选的有"circle" | "square" | "line" | "diamond" | "triangle" | "triangle-down" | "hexagon" | "bowtie" | "cross" | "tick" | "plus" | "hyphen"
                    symbol: PropTypes.oneOf([
                        "circle", "square", "line", "diamond", "triangle", "triangle-down", "hexagon", "bowtie", "cross", "tick", "plus", "hyphen"
                    ]),
                    // 设置图例图形样式
                    style: baseStyle,
                    // 设置当前图例name与其后图形的间距
                    spacing: PropTypes.number
                })
            })
        )
    })
])

// 定义label通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/label
const labelBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.exact({

        // 声明特殊的label类型，典型如饼图label支持'inner'、'outer'、'spider'
        type: PropTypes.string,

        // 设置label的偏移量，像素或百分比字符串
        offset: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),

        // 设置label相对于数据点在水平方向上的偏移距离
        offsetX: PropTypes.number,

        // 设置label相对于数据点在竖直方向上的偏移距离
        offsetY: PropTypes.number,

        // 设置label文本样式
        style: textBaseStyle,

        // 设置是否自动旋转，默认为true
        autoRotate: PropTypes.bool,

        // 设置文本旋转角度
        rotate: PropTypes.number,

        // 只对极坐标下的文本生效，表示文本是否按照角度进行放射状显示，true表示开启，false表示关闭
        labelEmit: PropTypes.bool,

        // 设置当前文字标签相对于数据点的位置，可选的有'top'、'bottom'、'middle'、'left'、'right'
        position: PropTypes.string,

        // 设置文本布局类型
        layout: PropTypes.arrayOf(
            PropTypes.exact({
                // 指定具体类型
                type: PropTypes.string
            })
        ),

        // 简易格式化文本标签的方式
        content: PropTypes.string,

        // 设置文字标签的格式化显示回调函数
        formatter: PropTypes.oneOfType([
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            }),
            PropTypes.any
        ]),

        // 设置是否自动隐藏，默认为false
        autoHide: PropTypes.bool
    })
])

// 定义tooltip通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/tooltip
const tooltipBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.exact({
        // 设置需要在tooltip中显示的字段，不同的图表有不同的默认字段列表
        // 可配合formatter做进一步配置
        fields: PropTypes.arrayOf(PropTypes.string),

        // 设置tooltip显示的回调函数
        formatter: PropTypes.oneOfType([
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            }),
            PropTypes.any
        ]),

        // 设置tooltip内容是否跟随鼠标移动，默认为true
        follow: PropTypes.bool,

        // 设置tooltip是否允许鼠标划入，默认为false
        enterable: PropTypes.bool,

        // 设置是否展示tooltip的标题，默认为false
        showTitle: PropTypes.bool,

        // 设置tooltip的标题内容，可传入字段名从而显示对应数据点的对应字段信息，若传入的字段名不存在
        // 则会直接显示原始的title内容
        title: PropTypes.string,

        // 设置tooltip相对于数据点的展示方位，可选的有'top'、'bottom'、'left'及'right'
        position: PropTypes.string,

        // 设置是否渲染marker，默认为true
        showMarkers: PropTypes.bool,

        // 设置tooltip marker的样式
        marker: pointBaseStyle,

        // 精细化设置各个dom部分的css样式
        // 格式为：
        /** Tooltip 内容框的 css 样式定义 */
        // {
        //     domStyles: {
        //     'g2-tooltip'?: CSSProperties;
        //     'g2-tooltip-title'?: CSSProperties;
        //     'g2-tooltip-list'?: CSSProperties;
        //     'g2-tooltip-list-item'?: CSSProperties;
        //     'g2-tooltip-marker'?: CSSProperties;
        //     'g2-tooltip-value'?: CSSProperties;
        //     'g2-tooltip-name'?: CSSProperties;
        //     }
        // }
        domStyles: PropTypes.object,

        // 设置tooltip偏移量
        offset: PropTypes.number,

        // 设置是否将tooltip中的项目逆序展示
        reversed: PropTypes.bool,

        // 设置是否显示为空值的tooltip项
        showNil: PropTypes.bool,

        // 设置是否在tooltip渲染之前对最终的items进行预处理
        customItems: PropTypes.oneOfType([
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            }),
            PropTypes.any
        ]),

        // true 表示合并当前点对应的所有数据并展示，false 表示只展示离当前点最逼近的数据内容
        shared: PropTypes.bool
    })
])


// 定义手动标注通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/annotations
const annotationsBasePropTypes = PropTypes.oneOfType([
    PropTypes.oneOf([false]),
    PropTypes.arrayOf(
        PropTypes.exact({
            // 设置标注类型，可选的有text | line | image | region | dataMarker | dataRegion | regionFilter | shape | html
            // 详细文档参考https://antv-g2plot.gitee.io/zh/docs/api/components/annotations
            type: PropTypes.string.isRequired,

            // 设置标注位置，具体说明如下：
            // 第一种，object 使用图表 x, y 对应的原始数据例如：{ time: '2010-01-01', value: 200 };
            // 第二种，数组来配置位置 [ x, y ]，根据数组中的值的存在以下几种形式： 
            //      1、对应数据源中的原始数据； 
            //      2、关键字：'min'、'max'、'median'、'start'、'end' 分别代表数据的最大值、最小值、中间值以及坐标系区间的起始和结束； 
            //      3、x, y 都是百分比的形式，如 30%，在绘图区域定位(即坐标系内)。 1 和 2 两种类型的数据可以混用，但是使用百分比形式时 x 和 y 必须都是百分比形式。
            // 第三种，回调函数，可以动态得确定辅助元素的位置，应用于数据动态更新，辅助元素的位置根据数据变化的场景。
            position: PropTypes.oneOfType([
                PropTypes.object,
                PropTypes.array
            ]),

            // 设置是否将标注绘制到canvas顶层，默认为false，即最底层
            top: PropTypes.bool,

            // 设置标注在水平方向上的偏移量
            offsetX: PropTypes.number,

            // 设置标注在竖直方向上的偏移量
            offsetY: PropTypes.number,

            // 设置起始位置，适用于类型line、region
            start: PropTypes.array,

            // 设置结束位置，适用于类型line、region
            end: PropTypes.array,

            // 设置图形样式
            style: baseStyle,

            // 设置图片路径，适用于类型image
            src: PropTypes.string,

            // 设置文本内容，适用于类型text
            content: PropTypes.string,

            // 设置文本旋转角度
            rotate: PropTypes.number,

            // 设置文本内容的最大长度
            maxLength: PropTypes.number,

            // 设置文本内容超出maxLength限制时，是否自动省略
            autoEllipsis: PropTypes.bool,

            // 设置文本内容截断的位置，可选的有head | middle | tail
            ellipsisPosition: PropTypes.string,

            // 设置文本在笛卡尔坐标系中，是否竖直显示，默认false为水平显示
            isVertical: PropTypes.bool,

            // 设置文本背景框的样式
            background: PropTypes.exact({
                // 设置背景样式
                style: baseStyle,

                // 设置背景文字周围留白大小
                padding: PropTypes.oneOfType([
                    PropTypes.number,
                    PropTypes.arrayOf(PropTypes.number)
                ])
            }),

            // 设置染色色值，适用于类型regionFilter
            color: PropTypes.string,

            // 设置regionFilter只针对特定的geometry起作用，适用于类型regionFilter
            apply: PropTypes.arrayOf(PropTypes.string),

            // 设置文本超出绘图区域范围时，是否自动调整文本角度以适应绘图范围区域
            autoAdjust: PropTypes.bool,

            // 设置朝向，可选的有'upward'、'downward'
            direction: PropTypes.string,

            // 设置线长度，适用于dataRegion
            lineLength: PropTypes.number,

            // 设置自定义html图形标记容器的元素，格式为html源码
            container: PropTypes.string,

            // 设置自定义html图形标记的元素，格式为html源码
            html: PropTypes.string,

            // 设置dom在水平方向上的对齐方式，适用于类型html，可选的有'left'、'middle'、'right'
            alignX: PropTypes.string,

            // 设置dom在竖直方向上的对齐方式，适用于类型html，可选的有'left'、'middle'、'right'
            alignY: PropTypes.string
        })
    )
])


// 定义滚动条通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/scrollbar
const scrollbarBasePropTypes = PropTypes.oneOfType([
    PropTypes.oneOf([false]),
    PropTypes.exact({
        // 设置滚动条类型，可选的有'horizontal'、'vertical'，默认'horizontal'
        type: PropTypes.string,

        // 设置滚动条像素宽度，仅在type='vertical'时生效
        width: PropTypes.number,

        // 设置滚动条高度，仅在type='horizontal'时生效
        height: PropTypes.number,

        // 设置滚动条布局padding
        padding: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number)
        ]),

        // 对应水平滚动条，为X轴每个分类字段的宽度；对于垂直滚动条，为X轴每个分类字段的高度
        categorySize: PropTypes.number,

        // 设置滚动条样式
        style: PropTypes.exact({
            // 设置滚动条滑道颜色
            trackColor: PropTypes.string,

            // 设置滚动条滑块颜色
            thumbColor: PropTypes.string,

            // 设置滚动条滑块高亮颜色
            thumbHighlightColor: PropTypes.string,

            // 设置滚动条圆角样式，可选的有'butt'、'round'、'square'
            lineCap: PropTypes.string
        })
    })
])

// 定义缩略轴通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/slider
const sliderBasePropTypes = PropTypes.oneOfType([
    PropTypes.oneOf([false]),
    PropTypes.exact({
        // 设置默认起始位置，0到1之间，表示百分比范围
        start: PropTypes.number,

        // 设置默认结束位置，0到1之间，表示百分比范围
        end: PropTypes.number,

        // 设置缩略轴高度
        height: PropTypes.number,

        // 设置背景趋势
        trendCfg: PropTypes.exact({
            // 设置统计文本的样式
            data: PropTypes.arrayOf(PropTypes.number),

            // 设置是否光滑
            smooth: PropTypes.bool,

            // 设置是否为面积图
            isArea: PropTypes.bool,

            // 设置背景样式
            backgroundStyle: baseStyle,

            // 设置line样式
            lineStyle: lineBaseStyle,

            // 设置area样式
            areaStyle: baseStyle
        }),

        // 设置背景样式
        backgroundStyle: baseStyle,

        // 设置前景样式
        foregroundStyle: baseStyle,

        // 配置handler
        handlerStyle: PropTypes.exact({
            // 设置缩略轴手柄宽度
            width: PropTypes.number,

            // 设置缩略轴手柄高度
            height: PropTypes.number,

            // 设置缩略轴手柄填充色
            fill: PropTypes.string,

            // 设置缩略轴手柄填充高亮色（hover 状态）
            highLightFill: PropTypes.string,

            // 设置缩略轴手柄描边色
            stroke: PropTypes.string,

            // 设置缩略轴手柄填充透明度
            opacity: PropTypes.number,

            // 设置缩略轴手柄背景圆角像素值
            radius: PropTypes.number,

            // 设置缩略轴手柄鼠标样式 （hover 状态）
            cursor: PropTypes.string
        }),

        // 设置文本样式
        textStyle: textBaseStyle,

        // 设置允许滑动范围下限
        minLimit: PropTypes.number,

        // 设置允许滑动范围上限
        maxLimit: PropTypes.number,

        // 设置滑块文本格式化函数
        formatter: PropTypes.oneOfType([
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            }),
            PropTypes.any
        ])
    })
])

// 定义主题通用PropTypes模板
const themeBasePropTypes = PropTypes.exact({
    // 设置自定义主题样式表
    styleSheet: PropTypes.exact({
        // 设置背景色
        backgroundColor: PropTypes.string,
        // 设置主题色
        brandColor: PropTypes.string,
        // 设置分类颜色色板，分类个数小于10时使用
        paletteQualitative10: PropTypes.arrayOf(PropTypes.string),
        // 设置分类颜色色板，分类个数大于10时使用
        paletteQualitative20: PropTypes.arrayOf(PropTypes.string),
        // 设置字体
        fontFamily: PropTypes.string
    }),

    // 主题色
    defaultColor: PropTypes.string,

    // 设置四周留白
    padding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(
            PropTypes.number
        )
    ]),
    // 图表字体
    fontFamily: PropTypes.string,
    // 分类颜色色板，分类个数小于10时使用
    colors10: PropTypes.arrayOf(PropTypes.string),
    // 分类颜色色板，分类个数大于10时使用
    colors20: PropTypes.arrayOf(PropTypes.string)
})

export {
    baseStyle,
    pointBaseStyle,
    lineBaseStyle,
    areaBaseStyle,
    textBaseStyle,
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    scrollbarBasePropTypes,
    sliderBasePropTypes,
    themeBasePropTypes
};