import PropTypes from 'prop-types';


// 定义基于g2及g2plot的ShapeAttrs的相关参数模板，参考：
// https://g2.antv.vision/zh/docs/api/shape/shape-attrs
// https://antv-g2plot.gitee.io/zh/docs/api/graphic-style
// 定义通用图形样式参数模板
const baseStyle = PropTypes.shape({
    /**
     * 填充颜色
     */
    fill: PropTypes.string,
    /**
     * 填充透明度，取值应在`0`到`1`之间
     */
    fillOpacity: PropTypes.number,
    /**
     * 轮廓颜色
     */
    stroke: PropTypes.string,
    /**
     * 轮廓透明度，取值应在`0`到`1`之间
     */
    strokeOpacity: PropTypes.number,
    /**
     * 轮廓像素宽度
     */
    lineWidth: PropTypes.number,
    /**
     * 轮廓虚线配置
     */
    lineDash: PropTypes.arrayOf(PropTypes.number),
    /**
     * 轮廓透明度，取值应在`0`到`1`之间
     */
    lineOpacity: PropTypes.number,
    /**
     * 轮廓末端类型配置
     */
    lineCap: PropTypes.string,
    /**
     * 整体透明度，取值应在`0`到`1`之间
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
     * 元素内鼠标指针类型
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
     * 散点像素半径
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
     * 文字对齐方式，可选项有`'center'`、`'end'`、`'left'`、`'right'`、`'start'`
     * 默认值：`'start'`
     */
    textAlign: PropTypes.oneOf([
        'center',
        'end',
        'left',
        'right',
        'start'
    ]),
    /**
     * 文字基线，可选项有`'top'`、`'middle'`、`'bottom'`、`'alphabetic'`、`'hanging'`
     * 默认值：`'bottom'`
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
    PropTypes.shape({
        /**
         * 声明当前字段度量类型，可选项有`'cat'`（分类度量）、`'timeCat'`（时间分类度量）、`'linear'`（线性度量）、`'time'`（连续的时间度量）、`'log'`（对数度量）、`'pow'`（幂数度量）、`'quantize'`（分段度量）、`'quantile'`（等分度量）、`'identity'`（常量度量）
         */
        type: PropTypes.oneOf([
            'cat', 'timeCat', 'linear', 'time', 'log',
            'pow', 'quantize', 'quantile', 'identity'
        ]),
        /**
         * 当前字段显示别名
         */
        alias: PropTypes.string,
        /**
         * 枚举当前字段下所有值
         */
        values: PropTypes.arrayOf(PropTypes.any),
        /**
         * 统一设置当前字段在坐标轴、图例、信息框中对应的文字内容`javascript`格式化函数
         */
        formatter: PropTypes.oneOfType([
            PropTypes.shape({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            }),
            PropTypes.any
        ]),
        /**
         * 当前字段绘图值域比例范围
         * 默认值：`[0, 1]`
         */
        range: PropTypes.arrayOf(PropTypes.number),
        /**
         * 当前字段值域下限，分类度量下无效
         */
        min: PropTypes.number,
        /**
         * 当前字段值域上限，分类度量下无效
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
         */
        tickCount: PropTypes.number,
        /**
         * 为当前字段设置坐标轴刻度最大数量
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
    PropTypes.shape({
        /**
         * 是否将坐标轴渲染于画布顶层，从而避免部分图表坐标轴被图形遮挡
         * 默认值：`false`
         */
        top: PropTypes.bool,
        /**
         * 坐标轴绘图范围，`[0, 1]`表示完整范围
         */
        range: PropTypes.arrayOf(PropTypes.number),
        /**
         * 适用于直角坐标系，设置坐标轴方位，可选项有`'top'`、`'bottom'`、`'left'`、`'right'`
         */
        position: PropTypes.string,
        /**
         * 配置坐标轴标题
         */
        title: PropTypes.shape({
            /**
             * 标题内容
             */
            text: PropTypes.string,
            /**
             * 标题文本样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle,
            /**
             * 标题对齐方式，可选项有`'center'`、`'start'`、`'end'`
             */
            position: PropTypes.string,
            /**
             * 标题与坐标轴之间的像素间距
             */
            offset: PropTypes.number,
            /**
             * 标题与坐标轴标签之间的像素间距
             */
            spacing: PropTypes.number,
            /**
             * 是否开启自动旋转
             */
            autoRotate: PropTypes.bool
        }),
        /**
         * 配置坐标轴标签，设置为`False`时隐藏
         */
        label: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.shape({
                /**
                 * 像素偏移量
                 */
                offset: PropTypes.number,
                /**
                 * 水平方向像素偏移量
                 */
                offsetX: PropTypes.number,
                /**
                 * 竖直方向像素偏移量
                 */
                offsetY: PropTypes.number,
                /**
                 * 标签文本样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
                 */
                style: baseStyle,
                /**
                 * 是否开启自动旋转
                 */
                autoRotate: PropTypes.bool,
                /**
                 * 文本旋转角度
                 */
                rotate: PropTypes.number,
                /**
                 * 适用于极坐标系，设置文本是否按照角度放射状显示
                 */
                labelEmit: PropTypes.bool,
                /**
                 * 标签位置，可选项有`'top'`、`'bottom'`、`'middle'`、`''left'`、`'right'`
                 */
                position: PropTypes.string,
                /**
                 * 文字内容`javascript`格式化函数
                 */
                formatter: PropTypes.oneOfType([
                    PropTypes.shape({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string
                    }),
                    PropTypes.any
                ]),
                /**
                 * 是否自动隐藏
                 */
                autoHide: PropTypes.bool
            })
        ]),
        /**
         * 配置坐标轴线
         */
        line: PropTypes.shape({
            /**
             * 坐标轴线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle
        }),
        /**
         * 配置坐标轴网格
         */
        grid: PropTypes.shape({
            /**
             * 配置网格线
             */
            line: PropTypes.shape({
                /**
                 * 网格线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
                 */
                style: baseStyle,
                /**
                 * 网格线类型，可选项有`'line'`、`'circle'`
                 */
                type: PropTypes.oneOf(['line', 'circle'])
            }),
            /**
             * 网格之间的填充色，可设置单个颜色或一组颜色
             */
            alternateColor: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.arrayOf(PropTypes.string)
            ]),
            /**
             * 网格线是否与刻度线对齐，设置为`False`时会处于刻度线之间
             */
            alignTick: PropTypes.bool,
            /**
             * 针对`'circle'`型网格线是否闭合
             */
            closed: PropTypes.bool
        }),
        /**
         * 配置坐标轴刻度线
         */
        tickLine: PropTypes.shape({
            /**
             * 刻度线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle,
            /**
             * 刻度线是否与刻度值对齐
             */
            alignTick: PropTypes.bool,
            /**
             * 刻度线像素长度
             */
            length: PropTypes.number
        }),
        /**
         * 配置坐标轴子刻度线
         */
        subTickLine: PropTypes.shape({
            /**
             * 子刻度线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle,
            /**
             * 子刻度线数量
             */
            count: PropTypes.number,
            /**
             * 子刻度线像素长度
             */
            length: PropTypes.number
        }),
        /**
         * 是否自动优化坐标轴
         */
        nice: PropTypes.bool,
        /**
         * 坐标轴最小值
         */
        min: PropTypes.number,
        /**
         * 坐标轴最大值
         */
        max: PropTypes.number,
        /**
         * 坐标轴范围下限
         */
        minLimit: PropTypes.number,
        /**
         * 坐标轴范围上限
         */
        maxLimit: PropTypes.number,
        /**
         * 期望的坐标轴刻度数量
         */
        tickCount: PropTypes.number,
        /**
         * 坐标轴刻度间隔值
         */
        tickInterval: PropTypes.number
    })
])


// 定义legend通用PropTypes模板，设置为false表示关闭legend
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/legend
const legendBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.shape({
        /**
         * 图例位置，可选项有`'top'`、`'top-left'`、`'top-right'`、`'left'`、`'left-top'`、`'left-bottom'`、`'right'`、`'right-top'`、`'right-bottom'`、`'bottom'`、`'bottom-left'`、`'bottom-right'`
         */
        position: PropTypes.string,
        /**
         * 图例布局方式，可选项有`'horizontal'`、`'vertical'`
         */
        layout: PropTypes.string,
        /**
         * 是否启用图例交互指示器
         * 默认值：`True`
         */
        radio: PropTypes.bool,
        /**
         * 配置图例标题
         */
        title: PropTypes.shape({
            /**
             * 图例标题内容
             */
            text: PropTypes.string,
            /**
             * 图例与图例项之间的像素间距
             */
            spacing: PropTypes.number,
            /**
             * 图例文字样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle
        }),
        /**
         * 图例整体在水平方向上的像素偏移
         */
        offsetX: PropTypes.number,
        /**
         * 图例整体在竖直方向上的像素偏移
         */
        offsetY: PropTypes.number,
        /**
         * 配置图例背景
         */
        background: PropTypes.shape({
            /**
             * 图例背景框像素内边距
             */
            padding: PropTypes.oneOfType([
                PropTypes.number,
                PropTypes.arrayOf(PropTypes.number)
            ])
        }),
        /**
         * 针对分类型图例，是否在图例项较多时分页
         */
        flipPage: PropTypes.bool,
        /**
         * 针对分类型图例，设置图例整体最大像素宽度
         */
        maxWidth: PropTypes.number,
        /**
         * 针对分类型图例，设置图例整体最大像素高度
         */
        maxHeight: PropTypes.number,
        /**
         * 针对分类型图例，是否反转图例项顺序
         */
        reversed: PropTypes.bool,
        /**
         * 针对分类型图例，设置图例项像素高度
         */
        itemHeight: PropTypes.number,
        /**
         * 针对分类型图例，设置图例项像素宽度
         */
        itemWidth: PropTypes.number,
        /**
         * 配置图例项名称
         */
        itemName: PropTypes.shape({
            /**
             * 图例项名称与标记之间的像素间距
             */
            spacing: PropTypes.number,
            /**
             * 图例项名称样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle,
            /**
             * 图例项名称内容`javascript`格式化函数
             */
            formatter: PropTypes.oneOfType([
                PropTypes.shape({
                    /**
                     * js函数体字符串
                     */
                    func: PropTypes.string,
                }),
                PropTypes.any
            ])
        }),
        /**
         * 配置图例项数值
         */
        itemValue: PropTypes.shape({
            /**
             * 设置图例项宽度后，控制数值是否右对齐
             */
            alignRight: PropTypes.bool,
            /**
             * 图例项数值样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle,
            /**
             * 图例项数值内容`javascript`格式化函数
             */
            formatter: PropTypes.oneOfType([
                PropTypes.shape({
                    /**
                     * js函数体字符串
                     */
                    func: PropTypes.string,
                }),
                PropTypes.any
            ])
        }),
        /**
         * 图例项水平像素间距
         */
        itemSpacing: PropTypes.number,
        /**
         * 自定义图例项高亮状态，格式如`{ 'item1': true, 'item2': false, 'item3': false }`
         */
        selected: PropTypes.object,
        /**
         * 针对连续型图例，设置图例选择范围的最小值
         */
        min: PropTypes.number,
        /**
         * 针对连续型图例，设置图例选择范围的最大值
         */
        max: PropTypes.number,
        /**
         * 针对连续型图例，设置图例当前停留位置对应的值
         */
        value: PropTypes.number,
        /**
         * 针对连续型图例，设置图例滑块是否可滑动
         */
        slidable: PropTypes.bool,
        /**
         * 配置连续型图例滑轨
         */
        rail: PropTypes.shape({
            /**
             * 滑轨类型，可选项有`'color'`、`'size'`
             */
            type: PropTypes.string,
            /**
             * 滑轨像素宽度
             */
            size: PropTypes.number,
            /**
             * 滑轨默认像素长度
             */
            defaultLength: PropTypes.number,
            /**
             * 滑轨样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle
        }),
        /**
         * 针对连续型图例，配置滑轨选择范围
         */
        track: PropTypes.shape({
            /**
             * 滑轨选择范围样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle
        }),
        /**
         * 针对连续型图例，配置滑轨滑块
         */
        handler: PropTypes.shape({
            /**
             * 滑块像素尺寸
             */
            size: PropTypes.number,
            /**
             * 滑块样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle
        }),
        /**
         * 是否启用自定义图例模式，开启后需配合`items`参数进行自定义图例的定义
         * 默认值：`False`
         */
        custom: PropTypes.bool,
        /**
         * 配置自定义分类型图例
         */
        items: PropTypes.arrayOf(
            PropTypes.shape({
                /**
                 * 当前图例项名称
                 */
                name: PropTypes.string.isRequired,
                /**
                 * 当前图例项数值
                 */
                value: PropTypes.string.isRequired,
                /**
                 * 配置当前图例项标记
                 */
                marker: PropTypes.shape({
                    /**
                     * 图例项标记类型，可选项有`'circle'`、`'square'`、`'line'`、`'diamond'`、`'triangle'`、`'triangle-down'`、`'hexagon'`、`'bowtie'`、`'cross'`、`'tick'`、`'plus'`、`'hyphen'`
                     */
                    symbol: PropTypes.oneOf([
                        "circle", "square", "line", "diamond", "triangle", "triangle-down", "hexagon", "bowtie", "cross", "tick", "plus", "hyphen"
                    ]),
                    /**
                     * 图例项标记样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
                     */
                    style: baseStyle,
                    /**
                     * 图例项名称与标记之间的像素间距
                     */
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
    PropTypes.shape({
        /**
         * 特殊标签类型，如针对饼图可用的`'inner'`、`'outer'`、`'spider'`
         */
        type: PropTypes.string,
        /**
         * 标签偏移量，支持数值型像素和百分比字符串
         */
        offset: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.string
        ]),
        /**
         * 标签水平方向像素偏移
         */
        offsetX: PropTypes.number,
        /**
         * 标签垂直方向像素偏移
         */
        offsetY: PropTypes.number,
        /**
         * 标签文字样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        style: baseStyle,
        /**
         * 是否自动旋转标签
         */
        autoRotate: PropTypes.bool,
        /**
         * 标签旋转角度
         */
        rotate: PropTypes.number,
        /**
         * 极坐标系下有效，设置文本是否按照角度放射状显示
         */
        labelEmit: PropTypes.bool,
        /**
         * 文字标签相对于数据点的位置，可选项有`'top'`、`'bottom'`、`'middle'`、`'left'`、`'right'`
         */
        position: PropTypes.string,
        /**
         * 配置文本布局
         */
        layout: PropTypes.arrayOf(
            PropTypes.shape({
                /**
                 * 文本布局类型，可选项有`'overlap'`、`'fixed-overlap'`、`'limit-in-shape'`
                 */
                type: PropTypes.string
            })
        ),
        /**
         * 配置文本标签内容
         */
        content: PropTypes.string,
        /**
         * 标签内容`javascript`格式化函数
         */
        formatter: PropTypes.oneOfType([
            PropTypes.shape({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            }),
            PropTypes.any
        ]),
        /**
         * 是否自动隐藏标签
         * 默认值：`False`
         */
        autoHide: PropTypes.bool,
        /**
         * 配置标签背景
         */
        background: PropTypes.shape({
            /**
             * 标签背景样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle,
            /**
             * 标签背景内边距
             */
            padding: PropTypes.number
        })
    })
])

// 定义tooltip通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/tooltip
const tooltipBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.shape({
        /**
         * 需要在信息框中显示的字段
         */
        fields: PropTypes.arrayOf(PropTypes.string),
        /**
         * 信息框内容`javascript`格式化函数
         */
        formatter: PropTypes.oneOfType([
            PropTypes.shape({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            }),
            PropTypes.any
        ]),
        /**
         * 信息框是否跟随鼠标移动
         * 默认值：`True`
         */
        follow: PropTypes.bool,
        /**
         * 信息框是否允许鼠标移入
         * 默认值：`False`
         */
        enterable: PropTypes.bool,
        /**
         * 是否显示信息框标题
         * 默认值：`False`
         */
        showTitle: PropTypes.bool,
        /**
         * 控制信息框标题，传入有效字段名时会显示对应字段值，否则则直接显示传入的标题文本
         */
        title: PropTypes.string,
        /**
         * 信息框相对于数据点的位置，可选项有`'top'`、`'bottom'`、`'left'`、`'right'`
         */
        position: PropTypes.string,
        /**
         * 信息框内是否显示各项图形标记
         * 默认值：`True`
         */
        showMarkers: PropTypes.bool,
        /**
         * 信息框各项图形标记样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        marker: baseStyle,
        /**
         * 分别控制信息框中不同构成部分的css样式，具体的构成部分对应键有`'g2-tooltip'`、`'g2-tooltip-title'`、`'g2-tooltip-list'`、`'g2-tooltip-list-item'`、`'g2-tooltip-marker'`、`'g2-tooltip-value'`、`'g2-tooltip-name'`
         */
        domStyles: PropTypes.object,
        /**
         * 信息框像素偏移量
         */
        offset: PropTypes.number,
        /**
         * 是否翻转显示信息框中的各子项
         */
        reversed: PropTypes.bool,
        /**
         * 是否显示信息框中数值为空的子项
         */
        showNil: PropTypes.bool,
        /**
         * 信息框子项`javascript`预处理函数
         */
        customItems: PropTypes.oneOfType([
            PropTypes.shape({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            }),
            PropTypes.any
        ]),
        /**
         * 是否合并展示当前数据点对应的所有数据
         */
        shared: PropTypes.bool
    })
])


// 定义手动标注通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/annotations
const annotationsBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.arrayOf(
        PropTypes.shape({
            /**
             * 当前标注类型，可选项有`'text'`、`'line'`、`'image'`、`'region'`、`'dataMarker'`、`'dataRegion'`、`''regionFilter'`、`'shape'`、`'html'`
             * 参考资料：https://g2-v4.antv.vision/zh/docs/api/general/annotation
             */
            type: PropTypes.string.isRequired,
            /**
             * 当前标注位置
             * - 当传入字典时，用于定义对应图表相关字段键值对数据的位置，如`{ 'time': '2010-01-01', 'value': 200 }`
             * - 当传入数组时，格式如`[x, y]`，其中`x`、`y`可以是图表坐标系中对应的数据值，百分比字符串如`'30%'`，或特殊位置关键词如`'min'`、`'max'`、`'median'`、`'start'`、`'end'`
             */
            position: PropTypes.oneOfType([
                PropTypes.object,
                PropTypes.array
            ]),
            /**
             * 是否将当前标注绘制到画布顶层
             * 默认值：`False`
             */
            top: PropTypes.bool,
            /**
             * 当前标注水平像素偏移量
             */
            offsetX: PropTypes.number,
            /**
             * 当前标注竖直像素偏移量
             */
            offsetY: PropTypes.number,
            /**
             * 适用于`'line'`、`'region'`类型标注，设置作用范围起始位置
             */
            start: PropTypes.array,
            /**
             * 适用于`'line'`、`'region'`类型标注，设置作用范围结束位置
             */
            end: PropTypes.array,
            /**
             * 当前标注样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            style: baseStyle,
            /**
             * 适用于`'image'`类型标注，设置图片地址
             */
            src: PropTypes.string,
            /**
             * 适用于`'text'`类型标注，设置文本内容
             */
            content: PropTypes.string,
            /**
             * 适用于`'text'`类型标注，设置文本旋转角度
             */
            rotate: PropTypes.number,
            /**
             * 适用于`'text'`类型标注，设置文本内容的最大像素长度
             */
            maxLength: PropTypes.number,
            /**
             * 适用于`'text'`类型标注，设置文本内容超出`maxLength`限制时，是否自动省略
             */
            autoEllipsis: PropTypes.bool,
            /**
             * 适用于`'text'`类型标注，设置文本内容超长省略截断的位置，可选项有`'head'`、`'middle'`、`'tail'`
             */
            ellipsisPosition: PropTypes.string,
            /**
             * 适用于`'text'`类型标注，针对直角坐标系，设置文本是否垂直显示
             */
            isVertical: PropTypes.bool,
            /**
             * 适用于`'text'`类型标注，配置文本背景框
             */
            background: PropTypes.shape({
                /**
                 * 文本背景框样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
                 */
                style: baseStyle,
                /**
                 * 文本背景框像素内边距
                 */
                padding: PropTypes.oneOfType([
                    PropTypes.number,
                    PropTypes.arrayOf(PropTypes.number)
                ])
            }),
            /**
             * 适用于`'regionFilter'`类型标注，设置着色颜色
             */
            color: PropTypes.string,
            /**
             * 适用于`'regionFilter'`类型标注，设置区域着色只针对特定的矢量类型起作用
             */
            apply: PropTypes.arrayOf(PropTypes.string),
            /**
             * 适用于`'text'`类型标注，当文本超出绘图区域范围时，是否自动调整文本角度来适应绘图范围
             */
            autoAdjust: PropTypes.bool,
            /**
             * 当前标注朝向，可选项有`'upward'`、`'downward'`
             */
            direction: PropTypes.string,
            /**
             * 适用于`'dataRegion'`类型标注，设置线像素长度
             */
            lineLength: PropTypes.number,
            /**
             * 自定义标记容器html源码字符串
             */
            container: PropTypes.string,
            /**
             * 适用于`'html'`类型标注，设置标注元素的html源码
             */
            html: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.shape({
                    /**
                     * js函数体字符串
                     */
                    func: PropTypes.string
                })
            ]),
            /**
             * 适用于`'html'`类型标注，设置标注元素水平方向对齐方式，可选项有`'left'`、`'middle'`、`'right'`
             */
            alignX: PropTypes.string,
            /**
             * 适用于`'html'`类型标注，设置标注元素竖直方向对齐方式，可选项有`'top'`、`'middle'`、`'bottom'`
             */
            alignY: PropTypes.string
        })
    )
])


// 定义滚动条通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/scrollbar
const scrollbarBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.shape({
        /**
         * 滚动条类型，可选项有`'horizontal'`、`'vertical'`
         * 默认值：`'horizontal'`
         */
        type: PropTypes.string,
        /**
         * 适用于`'vertical'`类型滚动条，设置滚动条像素宽度
         */
        width: PropTypes.number,
        /**
         * 适用于`'horizontal'`类型滚动条，设置滚动条像素高度
         */
        height: PropTypes.number,
        /**
         * 滚动条像素内边距
         */
        padding: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number)
        ]),
        /**
         * 对于`'horizontal'`类型滚动条，设置X轴每个分类字段的像素宽度；对于`'vertical'`类型滚动条，设置X轴每个分类字段的像素高度
         */
        categorySize: PropTypes.number,
        /**
         * 配置滚动条样式
         */
        style: PropTypes.shape({
            /**
             * 滚动条滑道颜色
             */
            trackColor: PropTypes.string,
            /**
             * 滚动条滑块颜色
             */
            thumbColor: PropTypes.string,
            /**
             * 滚动条滑块高亮颜色
             */
            thumbHighlightColor: PropTypes.string,
            /**
             * 滚动条滑道圆角类型，可选项有`'butt'`、`'round'`、`'square'`
             */
            lineCap: PropTypes.string
        })
    })
])

// 定义缩略轴通用PropTypes模板
// 参考文档：https://antv-g2plot.gitee.io/zh/docs/api/components/slider
const sliderBasePropTypes = PropTypes.oneOfType([
    PropTypes.bool,
    PropTypes.shape({
        /**
         * 初始化范围起始比例位置，取值应在`0`到`1`之间
         */
        start: PropTypes.number,
        /**
         * 初始化范围结束比例位置，取值应在`0`到`1`之间
         */
        end: PropTypes.number,
        /**
         * 缩略轴像素高度
         */
        height: PropTypes.number,
        /**
         * 缩略轴背景样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        backgroundStyle: baseStyle,
        /**
         * 缩略轴前景样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        foregroundStyle: baseStyle,
        /**
         * 配置缩略轴手柄
         */
        handlerStyle: PropTypes.shape({
            /**
             * 手柄像素宽度
             */
            width: PropTypes.number,
            /**
             * 手柄像素高度
             */
            height: PropTypes.number,
            /**
             * 手柄填充色
             */
            fill: PropTypes.string,
            /**
             * 手柄鼠标移入高亮状态下的填充色
             */
            highLightFill: PropTypes.string,
            /**
             * 手柄轮廓色
             */
            stroke: PropTypes.string,
            /**
             * 手柄透明度
             */
            opacity: PropTypes.number,
            /**
             * 手柄圆角程度
             */
            radius: PropTypes.number,
            /**
             * 手柄鼠标移入高亮状态下的鼠标指针类型
             */
            cursor: PropTypes.string
        }),
        /**
         * 缩略轴文本样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        textStyle: baseStyle,
        /**
         * 滑动范围下限
         */
        minLimit: PropTypes.number,
        /**
         * 滑动范围上限
         */
        maxLimit: PropTypes.number,
        /**
         * 缩略轴文本`javascript`格式化函数
         */
        formatter: PropTypes.oneOfType([
            PropTypes.shape({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            }),
            PropTypes.any
        ]),
        /**
         * 配置趋势线背景
         */
        trendCfg: PropTypes.shape({
            /**
             * 趋势线数据，默认会自动生成
             */
            data: PropTypes.arrayOf(PropTypes.number),
            /**
             * 是否渲染光滑折线
             */
            smooth: PropTypes.bool,
            /**
             * 是否渲染为填充面积图
             */
            isArea: PropTypes.bool,
            /**
             * 背景样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            backgroundStyle: baseStyle,
            /**
             * 折线样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            lineStyle: baseStyle,
            /**
             * 面积填充样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
             */
            areaStyle: baseStyle
        }),
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
         * 分类颜色数组，分类个数小于`10`时使用
         */
        colors10: PropTypes.arrayOf(PropTypes.string),
        /**
         * 分类颜色数组，分类个数大于`10`时使用
         */
        colors20: PropTypes.arrayOf(PropTypes.string),
        /**
         * 自定义主题样式
         */
        styleSheet: PropTypes.shape({
            /**
             * 画布背景色
             */
            backgroundColor: PropTypes.string,
            /**
             * 分类颜色数组，分类个数小于`10`时使用
             */
            paletteQualitative10: PropTypes.arrayOf(PropTypes.string),
            /**
             * 分类颜色数组，分类个数大于`10`时使用
             */
            paletteQualitative20: PropTypes.arrayOf(PropTypes.string),
            /**
             * 文字字体
             */
            fontFamily: PropTypes.string
        }),
        /**
         * 设置需要融合的内置主题类型，可选项有`'default'`、`'dark'`
         */
        withTheme: PropTypes.oneOf(['default', 'dark']),
        /**
         * 为坐标轴、图例等图表构件配置主题样式
         */
        components: PropTypes.object,
    }),
    PropTypes.oneOf(['default', 'dark'])
])

// 定义贴图通用PropTypes模板
const patternBasePropTypes = PropTypes.oneOfType([
    PropTypes.shape({
        /**
         * js函数体字符串
         */
        func: PropTypes.string
    }),
    PropTypes.shape({
        /**
         * 贴图类型，可选项有`'dot'`、`'square'`、`'line'`
         */
        type: PropTypes.oneOf(['dot', 'square', 'line']),
        /**
         * 配置贴图样式
         */
        cfg: PropTypes.shape({
            /**
             * 贴图背景色
             */
            backgroundColor: PropTypes.string,
            /**
             * 贴图元素填充色
             */
            fill: PropTypes.string,
            /**
             * 贴图元素填充透明度，取值应在`0`到`1`之间
             */
            fillOpacity: PropTypes.number,
            /**
             * 贴图元素描边色
             */
            stroke: PropTypes.string,
            /**
             * 贴图元素描边透明度，取值应在`0`到`1`之间
             */
            strokeOpacity: PropTypes.number,
            /**
             * 贴图元素描边像素宽度
             */
            lineWidth: PropTypes.number,
            /**
             * 贴图整体透明度，取值应在`0`到`1`之间
             */
            opacity: PropTypes.number,
            /**
             * 贴图整体旋转角度
             */
            rotation: PropTypes.number,
            /**
             * 适用于`'dot'`、`'square'`类型贴图，设置圆点或矩形像素大小
             * 默认值：`6`
             */
            size: PropTypes.number,
            /**
             * 适用于`'dot'`、`'square'`类型贴图，设置圆点或矩形之间的像素间隔大小
             */
            padding: PropTypes.number,
            /**
             * 适用于`'line'`类型贴图，设置线条之间的像素距离
             * 默认值：`5`
             */
            spacing: PropTypes.number,
            /**
             * 适用于`'dot'`、`'square'`类型贴图，控制圆点或矩形之间是否交错
             * 默认值：`True`
             */
            isStagger: PropTypes.bool
        })
    })
])

// 定义动画通用PropTypes模板
const animationExactPropTypes = PropTypes.shape({
    /**
     * 动画效果类型，可选项有`'fade-in'`、`'fade-out'`、`'grow-in-x'`、`'grow-in-y'`、`'grow-in-xy'`、`'scale-in-x'`、`'scale-in-y'`、`'wave-in'`、`'zoom-in'`、`'zoom-out'`、`'path-in'`、`'position-update'`
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
     * 动画持续时长，单位：毫秒
     */
    duration: PropTypes.number,
    /**
     * 动画渲染开始延时时长，单位：毫秒
     */
    delay: PropTypes.number
})

const animationBasePropTypes = PropTypes.oneOfType([
    // 设置为false时关闭动画
    PropTypes.bool,
    PropTypes.shape({
        /**
         * 初次加载阶段
         */
        appear: animationExactPropTypes,
        /**
         * 图表更新阶段
         */
        enter: animationExactPropTypes,
        /**
         * 仅数据更新阶段
         */
        update: animationExactPropTypes,
        /**
         * 旧数据覆盖销毁退场阶段
         */
        leave: animationExactPropTypes
    })
])

// 定义交互通用PropTypes模板
const interactionsBasePropTypes = PropTypes.arrayOf(
    PropTypes.shape({
        /**
         * 当前交互类型，常用项有`'active-region'`、`'element-active'`、`'element-selected'`、`'element-single-selected'`、`'element-highlight'`、`'element-highlight-by-x'`、·'element-highlight-by-color'·、`'legend-filter'`、`'legend-visible-filter'`、`'legend-active'`、`'legend-highlight'`、`'legend-highlight'`、`'element-list-highlight'`、`'pie-statistic-active'`等，[拓展阅读](https://g2-v4.antv.vision/zh/docs/api/general/interaction)
         */
        type: PropTypes.string,
        /**
         * 当前交互类型对应的配置参数，[拓展阅读](https://g2-v4.antv.vision/zh/docs/api/general/interaction)
         */
        cfg: PropTypes.object,
        /**
         * 是否启用当前交互
         */
        enable: PropTypes.bool
    })
)

// 定义状态样式通用PropTypes模板
const stateBasePropTypes = PropTypes.shape({
    /**
     * 配置激活状态
     */
    active: PropTypes.shape({
        /**
         * 激活状态样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        style: baseStyle
    }),
    /**
     * 配置非激活状态
     */
    inactive: PropTypes.shape({
        /**
         * 非激活状态样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        style: baseStyle
    }),
    /**
     * 配置选中状态
     */
    selected: PropTypes.shape({
        /**
         * 选中状态样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        style: baseStyle
    }),
    /**
     * 配置默认状态
     */
    default: PropTypes.shape({
        /**
         * 默认状态样式，具体参数请参考[样式配置项](https://fact.feffery.tech/style)
         */
        style: baseStyle
    })
})

// 刷选交互功能通用PropTypes模板
const brushBasePropTypes = PropTypes.shape({
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
    button: PropTypes.shape({
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
        buttonStyle: PropTypes.shape({
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