/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    pointBaseStyle,
    lineBaseStyle,
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    baseStyle,
    textBaseStyle,
    themeBasePropTypes
} from './BasePropTypes.react';

const LazyAntdScatter = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdScatter.react'));

const AntdScatter = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdScatter {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdScatter.propTypes = {
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

    // 定义作为y轴的字段名
    yField: PropTypes.string.isRequired,

    // 定义作为色彩映射依据的字段
    colorField: PropTypes.string,

    // 定义作为尺寸映射依据的字段
    sizeField: PropTypes.string,

    // 定义作为形状映射依据的字段
    shapeField: PropTypes.string,

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

    // 用于设置散点像素尺寸大小
    size: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 用于设置形状相关参数
    shape: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 设置散点样式
    pointStyle: PropTypes.oneOfType([
        pointBaseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 当shapeField已设置时，且legend、shapeLegend均不为false时，则会渲染针对shape的图例
    shapeLegend: legendBasePropTypes,

    // 设置后会渲染散点尺寸相关的图例
    sizeLegend: legendBasePropTypes,

    // 设置四象限图组件相关参数
    quadrant: PropTypes.exact({
        // 设置x轴上的基准分割线位置，默认为0
        xBaseline: PropTypes.number,

        // 设置y轴上的基准分割线位置，默认为0
        yBaseline: PropTypes.number,

        // 配置分割线样式
        lineStyle: lineBaseStyle,

        // 配置四个象限的样式，单对象输入时全局设置，
        // 亦可按照上右下左的顺序分别传入四个对象构成的数组来分别设置四个象限的样式
        regionStyle: PropTypes.oneOfType([
            baseStyle,
            PropTypes.arrayOf(baseStyle)
        ]),

        // 分别设置四个象限的文字标注信息及其样式
        labels: PropTypes.arrayOf(
            PropTypes.exact({
                // 设置标注内容
                content: PropTypes.string,

                // 设置标注坐标位置，格式：[x坐标, y坐标]
                position: PropTypes.arrayOf(PropTypes.number),

                // 设置标注文字样式
                style: textBaseStyle
            })
        )
    }),

    // 设置回归线相关参数
    regressionLine: PropTypes.exact({
        // 设置回归线类型，可选的有'exp'、'linear'、'loess'、'log'、'poly'、'pow'、'quad'
        type: PropTypes.oneOf(['exp', 'linear', 'loess', 'log', 'poly', 'pow', 'quad']),

        // 设置回归线样式
        style: lineBaseStyle,

        // 自定义映射算法，优先级高于type
        algorithm: PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        }),

        // 设置是否置于图层顶层显示
        top: PropTypes.bool
    }),

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
    animation: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.bool
    ]),

    // 常用事件监听参数
    // tooltip显示事件
    recentlyTooltipChangeRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.arrayOf(PropTypes.object)
    }),

    // 单独折线点击事件
    recentlyPointClickRecord: PropTypes.exact({
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

    // 交互事件配置
    interactions: PropTypes.array,

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
AntdScatter.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdScatter;

export const propTypes = AntdScatter.propTypes;
export const defaultProps = AntdScatter.defaultProps;