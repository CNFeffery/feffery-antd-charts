import PropTypes from 'prop-types';


// 定义基于g2及g2plot的ShapeAttrs的相关参数模板，参考：
// https://g2.antv.vision/zh/docs/api/shape/shape-attrs
// https://antv-g2plot.gitee.io/zh/docs/api/graphic-style
// 定义通用图形样式参数模板
const baseStyle = PropTypes.shape({
    /**
     * 填充色
     */
    fill: PropTypes.string,
    /**
     * 填充透明度
     */
    fillOpacity: PropTypes.number,
    /**
     * 线要素颜色
     */
    stroke: PropTypes.string,
    /**
     * 轮廓透明度
     */
    strokeOpacity: PropTypes.number,
    /**
     * 图形描边像素宽度/线要素像素宽度
     */
    lineWidth: PropTypes.number,
    /**
     * 图形描边虚线配置
     */
    lineDash: PropTypes.arrayOf(PropTypes.number),
    /**
     * 描边透明度
     */
    lineOpacity: PropTypes.number,
    /**
     * 描边末端样式
     */
    lineCap: PropTypes.string,
    /**
     * 整体透明度
     */
    opacity: PropTypes.number,
    /**
     * 阴影颜色
     */
    shadowColor: PropTypes.string,
    /**
     * 阴影模糊系数
     */
    shadowBlur: PropTypes.number,
    /**
     * 阴影水平像素偏移
     */
    shadowOffsetX: PropTypes.number,
    /**
     * 阴影竖直像素偏移
     */
    shadowOffsetY: PropTypes.number,
    /**
     * 鼠标移入图形呈现的指针样式
     */
    cursor: PropTypes.string,
    /**
     * 像素圆角
     */
    radius: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number)
    ]),
    /**
     * 点像素半径
     */
    r: PropTypes.number,
    /**
     * 文字字体大小
     */
    fontSize: PropTypes.number,
    /**
     * 文字字体
     */
    fontFamily: PropTypes.string,
    /**
     * 文字字重
     */
    fontWeight: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.number
    ]),
    /**
     * 文字行高
     */
    lineHeight: PropTypes.number,
    /**
     * 文字对齐方式，可选的有'center'、'end'、'left'、'right'、'start'
     * 默认：'start'
     */
    textAlign: PropTypes.oneOf([
        'center',
        'end',
        'left',
        'right',
        'start'
    ]),
    /**
     * 文字基线，可选的有'top'、'middle'、'bottom'、'alphabetic'、'hanging'
     * 默认：'bottom'
     */
    textBaseline: PropTypes.oneOf([
        'top',
        'middle',
        'bottom',
        'alphabetic',
        'hanging'
    ])
})

// 定义全局化配置图表数据元信息PropTypes模板，其中原始字段名为属性名
const metaBasePropTypes = PropTypes.objectOf(
    PropTypes.exact({
        /**
         * 声明当前字段数据类型，可选的有：
         * cat: 分类度量
         * timeCat: 时间分类度量
         * linear: 线性度量
         * time: 连续的时间度量
         * log: 对数度量
         * pow: 幂数度量
         * quantize: 分段度量，用户可以指定不均匀的分段
         * quantile: 等分度量，根据数据的分布自动计算分段
         * identity: 常量度量
         */
        type: PropTypes.oneOf([
            'cat', 'timeCat', 'linear', 'time', 'log',
            'pow', 'quantize', 'quantile', 'identity'
        ]),

        /**
         * 设置当前字段的显示别名
         */
        alias: PropTypes.string,

        /**
         * 枚举当前字段下所有值
         */
        values: PropTypes.arrayOf(PropTypes.any),

        /**
         * 统一设置当前字段在坐标轴、图例、tooltip中的显示格式化规则
         */
        formatter: PropTypes.oneOfType([
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            }),
            PropTypes.any
        ]),

        /**
         * 设置当前字段用于绘图的值范围
         * 默认：[0, 1]
         */
        range: PropTypes.arrayOf(PropTypes.number),

        /**
         * 定义当前字段值域的最小值，分类度量下无效
         */
        min: PropTypes.number,

        /**
         * 定义当前字段值域的最大值，分类度量下无效
         */
        max: PropTypes.number,

        /**
         * 强制设置当前字段的值域最小值，会影响坐标轴刻度开始位置，分类度量下无效
         */
        minLimit: PropTypes.number,

        /**
         * 强制设置当前字段的值域最大值，会影响坐标轴刻度结束位置，分类度量下无效
         */
        maxLimit: PropTypes.number,

        /**
         * 对数度量下有效，用于定义底数
         */
        base: PropTypes.number,

        /**
         * 幂数度量下有效，用于定义指数
         */
        exponent: PropTypes.number,

        /**
         * 是否自动调整坐标轴范围
         */
        nice: PropTypes.bool,

        /**
         * 为当前字段手动设置坐标轴刻度值，优先级最高
         */
        ticks: PropTypes.arrayOf(PropTypes.any),

        /**
         * 线性度量下有效，为当前字段设置坐标轴刻度最小间隔
         */
        minTickInterval: PropTypes.number,

        /**
         * 为当前字段设置坐标轴刻度数量
         * 默认：5
         */
        tickCount: PropTypes.number,

        /**
         * 为当前字段设置坐标轴刻度最大数量
         * 默认：10
         */
        maxTickCount: PropTypes.number,

        /**
         * 连续的时间度量下有效，设置是否强制显示坐标轴刻度最后的时间刻度值
         */
        showLast: PropTypes.bool
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
            style: baseStyle,

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
                style: baseStyle,

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
            style: baseStyle
        }),

        // 设置坐标轴网格线
        grid: PropTypes.exact({
            // 设置线要素样式
            line: PropTypes.exact({
                // 线要素样式
                style: baseStyle,
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
            style: baseStyle,

            // 设置坐标轴刻度线是否与tick对齐
            alignTick: PropTypes.bool,

            // 设置坐标轴刻度线长度
            length: PropTypes.number
        }),

        // 设置坐标轴子刻度线
        subTickLine: PropTypes.exact({
            // 设置坐标轴刻度线样式
            style: baseStyle,

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
        tickCount: PropTypes.number,

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
            style: baseStyle
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
            style: baseStyle,

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
            style: baseStyle,

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
        style: baseStyle,

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
        autoHide: PropTypes.bool,

        /**
         * 配置文本标签背景
         */
        background: PropTypes.exact({
            /**
             * 设置文本标签背景样式
             */
            style: baseStyle,
            /**
             * 设置文本标签像素内边距
             */
            padding: PropTypes.number
        })
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
        marker: baseStyle,

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
        PropTypes.shape({
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
            html: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.exact({
                    /**
                     * 回调模式
                     */
                    func: PropTypes.string
                })
            ]),

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
            lineStyle: baseStyle,

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
        textStyle: baseStyle,

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
const themeBasePropTypes = PropTypes.oneOfType([
    PropTypes.shape({
        /**
         * 画布背景色
         */
        background: PropTypes.string,

        /**
         * 设置分类颜色色板，分类个数小于10时使用
         */
        colors10: PropTypes.arrayOf(PropTypes.string),

        /**
         * 设置分类颜色色板，分类个数大于10时使用
         */
        colors20: PropTypes.arrayOf(PropTypes.string),

        /**
         * 为坐标轴、图例等图表构件配置不同状态下的样式
         */
        components: PropTypes.object,

        // 设置自定义主题样式表
        styleSheet: PropTypes.exact({
            // 设置背景色
            backgroundColor: PropTypes.string,
            // 设置分类颜色色板，分类个数小于10时使用
            paletteQualitative10: PropTypes.arrayOf(PropTypes.string),
            // 设置分类颜色色板，分类个数大于10时使用
            paletteQualitative20: PropTypes.arrayOf(PropTypes.string),
            // 设置字体
            fontFamily: PropTypes.string
        }),

        /**
         * 设置需要融合的内置主题类型，可选的有：'default'、'dark'
         */
        withTheme: PropTypes.oneOf(['default', 'dark'])
    }),
    PropTypes.oneOf(['default', 'dark'])
])

// 定义贴图通用PropTypes模板
const patternBasePropTypes = PropTypes.oneOfType([
    PropTypes.exact({
        /**
         * 自定义js回调函数字符串
         */
        func: PropTypes.string
    }),
    PropTypes.exact({
        /**
         * 贴图类型
         * 可选的有'dot'、'square'、'line'
         */
        type: PropTypes.oneOf(['dot', 'square', 'line']),
        /**
         * 贴图配置参数
         */
        cfg: PropTypes.exact({
            // 通用配置参数
            /**
             * 贴图背景色
             */
            backgroundColor: PropTypes.string,
            /**
             * 贴图元素的填充色
             */
            fill: PropTypes.string,
            /**
             * 贴图元素填充透明度
             */
            fillOpacity: PropTypes.number,
            /**
             * 贴图元素描边色
             */
            stroke: PropTypes.string,
            /**
             * 贴图元素描边透明度
             */
            strokeOpacity: PropTypes.number,
            /**
             * 贴图元素描边像素宽度
             */
            lineWidth: PropTypes.number,
            /**
             * 贴图整体透明度
             */
            opacity: PropTypes.number,
            /**
             * 贴图整体旋转角度
             */
            rotation: PropTypes.number,
            // dot类型专用配置项
            /**
             * 圆点像素大小
             * 默认：6
             */
            size: PropTypes.number,
            /**
             * 圆点之间的像素间隔大小
             * 默认：2
             */
            padding: PropTypes.number,
            // line类型专用配置项
            /**
             * 线条之间的像素距离
             * 默认：5
             */
            spacing: PropTypes.number,
            // square类型专用配置项
            /**
             * 矩形像素大小
             * 默认：6
             */
            // eslint-disable-next-line no-dupe-keys
            size: PropTypes.number,
            /**
             * 矩形之间的像素间隔大小
             * 默认：1
             */
            // eslint-disable-next-line no-dupe-keys
            padding: PropTypes.number,
            // square、dot类型专用配置项
            /**
             * 矩形或圆点之间是否交错
             * 默认：true
             */
            isStagger: PropTypes.bool
        })
    })
])

// 定义动画通用PropTypes模板
const animationExactPropTypes = PropTypes.exact({
    /**
     * 设置动画效果类型，可选的有'fade-in'、'fade-out'、'grow-in-x'、
     * 'grow-in-y'、'grow-in-xy'、'scale-in-x'、'scale-in-y'、'wave-in'、
     * 'zoom-in'、'zoom-out'、'path-in'、'position-update'
     */
    animation: PropTypes.oneOf([
        'fade-in',
        'fade-out',
        'grow-in-x',
        'grow-in-y',
        'grow-in-xy',
        'scale-in-x',
        'scale-in-y',
        'wave-in',
        'zoom-in',
        'zoom-out',
        'path-in',
        'position-update'
    ]),
    /**
     * 设置动画持续时长，单位：毫秒
     */
    duration: PropTypes.number,
    /**
     * 设置动画延时播放时长，单位：毫秒
     */
    delay: PropTypes.number
})

const animationBasePropTypes = PropTypes.oneOfType([
    // 设置为false时关闭动画
    PropTypes.bool,
    PropTypes.exact({
        /**
         * 配置图表初次加载时的入场动画
         */
        appear: animationExactPropTypes,
        /**
         * 配置图表发生更新时的入场动画
         */
        enter: animationExactPropTypes,
        /**
         * 配置仅图表数据更新时的过渡动画
         */
        update: animationExactPropTypes,
        /**
         * 配置被新数据覆盖的旧数据对应图形被销毁时的退场动画
         */
        leave: animationExactPropTypes
    })
])

// 定义交互通用PropTypes模板
const interactionsBasePropTypes = PropTypes.arrayOf(
    PropTypes.exact({
        /**
         * 交互类型，可选的有'active-region'、'element-active'、'element-selected'、
         * 'element-single-selected'、'element-highlight'、'element-highlight-by-x'、
         * 'element-highlight-by-color'、'legend-filter'、'legend-visible-filter'、
         * 'legend-active'、'legend-highlight'、'legend-highlight'、'element-list-highlight'、'pie-statistic-active'等
         * 具体参考：https://g2-v4.antv.vision/zh/docs/api/general/interaction
         */
        type: PropTypes.string,
        // type: PropTypes.oneOf([
        //     'active-region',
        //     'element-active',
        //     'element-selected',
        //     'element-single-selected',
        //     'element-highlight',
        //     'element-highlight-by-x',
        //     'element-highlight-by-color',
        //     'legend-filter',
        //     'legend-active',
        //     'legend-highlight',
        //     'element-list-highlight'
        // ]),
        /**
         * 当前交互类型对应的配置参数
         */
        cfg: PropTypes.object,
        /**
         * 是否启用当前交互
         */
        enable: PropTypes.bool
    })
)

// 定义状态样式通用PropTypes模板
const stateBasePropTypes = PropTypes.exact({
    /**
     * 配置激活状态
     */
    active: PropTypes.exact({
        /**
         * 激活状态样式
         */
        style: baseStyle
    }),
    /**
     * 配置非激活状态
     */
    inactive: PropTypes.exact({
        /**
         * 非激活状态样式
         */
        style: baseStyle
    }),
    /**
     * 配置选中状态
     */
    selected: PropTypes.exact({
        /**
         * 选中状态样式
         */
        style: baseStyle
    }),
    /**
     * 默认状态
     */
    default: PropTypes.exact({
        /**
         * 默认状态样式
         */
        style: baseStyle
    })
})

// 刷选交互功能通用PropTypes模板
const brushBasePropTypes = PropTypes.exact({
    /**
     * 是否启用筛选功能
     * 默认值：`false`
     */
    enabled: PropTypes.bool,
    /**
     * 刷选类型，可选项有`'rect'`、`'x-rect'`、`'y-rect'`、`'circle'`、`'path'`
     * 默认值：`'rect'`
     */
    type: PropTypes.oneOf(['rect', 'x-rect', 'y-rect', 'circle', 'path']),
    /**
     * 刷选动作类型，可选项有`'filter'`、`'highlight'`
     * 默认值：`'filter'`
     */
    action: PropTypes.oneOf(['filter', 'highlight']),
    /**
     * 配置刷选范围样式
     */
    mask: baseStyle,
    /**
     * 配置筛选重置按钮
     */
    button: PropTypes.exact({
        /**
         * 按钮内边距
         */
        padding: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number)
        ]),
        /**
         * 按钮文本内容
         */
        text: PropTypes.string,
        /**
         * 文本样式
         */
        textStyle: baseStyle,
        /**
         * 按钮样式
         */
        buttonStyle: PropTypes.exact({
            /**
             * 默认状态样式
             */
            default: baseStyle,
            /**
             * 激活状态样式
             */
            active: baseStyle
        })
    })
})

export {
    baseStyle,
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    scrollbarBasePropTypes,
    sliderBasePropTypes,
    themeBasePropTypes,
    patternBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes,
    brushBasePropTypes
};