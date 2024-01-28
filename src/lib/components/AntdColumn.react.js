/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    scrollbarBasePropTypes,
    sliderBasePropTypes,
    baseStyle,
    areaBaseStyle,
    textBaseStyle,
    themeBasePropTypes,
    patternBasePropTypes,
    animationBasePropTypes
} from './BasePropTypes.react';

const LazyAntdColumn = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdColumn.react'));

const AntdColumn = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdColumn {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdColumn.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 定义绘图所需数据，必须参数
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 定义作为x轴的字段名
    xField: PropTypes.string.isRequired,

    // 定义作为y轴的字段名，格式为[左轴对应y轴字段, 右轴对应y轴字段]
    yField: PropTypes.string.isRequired,

    // 定义作为分组依据的字段名
    seriesField: PropTypes.string,

    // 用于在堆叠分组柱状图中指定分组字段，此时seriesField指定的字段会作为每个组内堆叠的分层依据
    groupField: PropTypes.string,

    // 在存在seriesField分组字段时，用于设置是否堆叠条形图
    isStack: PropTypes.bool,

    // 在存在seriesField分组字段时，用于设置是否分组条形图
    isGroup: PropTypes.bool,

    // 在xField的值格式为[number, number]时，用于设置是否区间条形图
    isRange: PropTypes.bool,

    // 在isStack=true时生效，用于设置是否百分比条形图
    isPercent: PropTypes.bool,

    // 用于手动设置调色方案，接受css中合法的所有颜色值，当传入单个字符串时，所有折线沿用此颜色值
    // 当传入数组时，会视作调色盘方案对seriesField区分的不同系列进行着色
    // 当传入对象时，会解析出其'func'属性对应的字符串，解析为函数，以支持更为自由的seriesField->色彩映射
    color: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            // 传入字符串形式的js函数体源码，例如
            // (ref) => {
            //     if (ref.series === '系列一'){
            //         return 'red'
            //     }
            //     return 'blue'
            // }
            func: PropTypes.string
        })
    ]),

    // 配置缩略轴相关参数
    slider: sliderBasePropTypes,

    // 设置分组条形图组间像素间隔宽度
    intervalPadding: PropTypes.number,

    // 设置分组条形图组内像素间隔宽度
    dodgePadding: PropTypes.number,

    // 设置柱状图的最小像素宽度
    minColumnWidth: PropTypes.number,

    // 设置柱状图的最大像素宽度
    maxColumnWidth: PropTypes.number,

    // 设置柱体的样式
    columnStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 设置柱状图背景样式
    columnBackground: PropTypes.exact({
        // 具体样式
        style: areaBaseStyle
    }),

    // 设置柱状图宽度占比，0~1之间
    columnWidthRatio: PropTypes.number,

    // 设置分组柱状图中条形之间的间距，0~1之间
    marginRatio: PropTypes.number,

    // 设置条形图滚动条样式
    scrollbar: scrollbarBasePropTypes,

    // 设置转化标签相关属性
    conversionTag: PropTypes.exact({
        // 设置转化率标签像素尺寸大小
        size: PropTypes.number,

        // 设置转化率标签与柱体之间的像素间距
        spacing: PropTypes.number,

        // 设置组件与坐标轴之间的距离
        offset: PropTypes.number,

        // 配置转化率组件箭头样式，false时不显示箭头
        arrow: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.exact({
                // 设置箭头尺寸
                headSize: PropTypes.number
            })
        ]),

        // 配置转化率组件文本信息，false时不显示文本
        text: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.exact({
                // 自定义转化率计算函数
                formatter: PropTypes.exact({
                    // 回调模式
                    func: PropTypes.string
                }),

                // 自定义转化率文字样式
                style: textBaseStyle
            })
        ])
    }),

    // 设置联通对比区域相关参数
    connectedArea: PropTypes.oneOfType([
        PropTypes.exact({
            // 设置触发方式，false表示不触发，可选的有'hover'、'click'
            trigger: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.string
            ])
        }),
        PropTypes.bool
    ]),

    // 设置x坐标轴相关属性
    xAxis: axisBasePropTypes,

    // 设置y坐标轴相关属性
    yAxis: axisBasePropTypes,

    // 定义图表容器像素宽度，默认为400
    width: PropTypes.number,

    // 定义图表容器像素高度，默认为400
    height: PropTypes.number,

    // 设置图表是否自适应容器宽高，当设置为true时，width与height参数将失效，默认为true
    autoFit: PropTypes.bool,

    // 定义图表四个方向的空白间距值，可以为单个数字譬如16，也可以为四个数字构成的数组，按顺序代表上-右-下-左分别的像素间距
    padding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.string
    ]),

    // 定义在padding基础上额外的像素填充间距
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.string
    ]),

    // 设置图表渲染方式为'canvas'或'svg'模式，默认为'canvas'
    renderer: PropTypes.oneOf(['canvas', 'svg']),

    // 设置语言，可选的有'zh-CN'与'en-US'
    locale: PropTypes.oneOf(['zh-CN', 'en-US']),

    // 设置是否对超出绘图区域的几何元素进行裁剪
    limitInPlot: PropTypes.bool,

    // 配置图例相关参数
    legend: legendBasePropTypes,

    // 配置文字标签相关参数
    label: labelBasePropTypes,

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

    // 配置标注相关参数
    annotations: annotationsBasePropTypes,

    // 配置动画相关参数
    animation: animationBasePropTypes,

    // 常用事件监听参数
    // tooltip显示事件
    recentlyTooltipChangeRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.arrayOf(PropTypes.object)
    }),

    // 单独column点击事件
    recentlyColumnClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.object
    }),

    // 监听图例事件
    recentlyLegendInfo: PropTypes.exact({
        // 记录当前点击的图例项内容
        triggerItemName: PropTypes.any,
        // 记录当前各图例项信息
        items: PropTypes.arrayOf(
            PropTypes.object
        )
    }),

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

    /**
     * 配置图形填充贴图样式
     */
    pattern: patternBasePropTypes,

    // 交互事件配置
    interactions: PropTypes.array,

    // 柱体点击事件
    recentlyBarClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.object
    }),

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

// 设置默认参数
AntdColumn.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdColumn;

export const propTypes = AntdColumn.propTypes;
export const defaultProps = AntdColumn.defaultProps;