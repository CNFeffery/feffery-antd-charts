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
    baseStyle,
    themeBasePropTypes,
    patternBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes
} from './BasePropTypes.react';

const LazyAntdHeatmap = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdHeatmap.react'));

const AntdHeatmap = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdHeatmap {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdHeatmap.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 辅助强制刷新
     */
    key: PropTypes.string,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * css样式
     */
    style: PropTypes.object,

    /**
     * 必填，用于定义绘图所需数据
     */
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    /**
     * 字段预处理元信息
     */
    meta: metaBasePropTypes,

    /**
     * 定义作为x轴的字段名
     */
    xField: PropTypes.string.isRequired,

    // 定义作为y轴的字段名
    yField: PropTypes.string.isRequired,

    /**
     * 定义作为色彩映射依据的字段
     */
    colorField: PropTypes.string,

    /**
     * 定义作为尺寸映射依据的字段
     */
    sizeField: PropTypes.string,

    /**
     * 配置坐标轴映射，可选的有'x'、'y'
     */
    reflect: PropTypes.oneOf(['x', 'y']),

    // 用于手动设置调色方案，接受css中合法的所有颜色值，当传入单个字符串时，当前图表所有图形沿用此颜色值
    // 当传入数组时，会视作调色盘方案对colorField区分的不同系列进行着色
    // 当传入对象时，会解析出其'func'属性对应的字符串，解析为函数，以支持更为自由的colorField->色彩映射
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

    /**
     * 设置热力网格形状，可选的有'rect'、'square'、'square'
     */
    shape: PropTypes.oneOf(['rect', 'square', 'circle']),

    /**
     * 配置坐标系相关参数
     */
    coordinate: PropTypes.exact({
        /**
         * 坐标系类型，可选的有'cartesian'（笛卡尔坐标系）、'polar'（极坐标系）、'helix'（螺旋坐标系）、'theta'（角度映射坐标系）
         */
        type: PropTypes.oneOf(['cartesian', 'polar', 'helix', 'theta']),
        /**
         * 坐标系配置项，作用于极坐标系
         */
        cfg: PropTypes.exact({
            /**
             * 配置起始弧度
             */
            startAngle: PropTypes.number,
            /**
             * 配置结束弧度
             */
            endAngle: PropTypes.number,
            /**
             * 配置极坐标系半径，取值在0到1之间
             */
            radius: PropTypes.number,
            /**
             * 配置极坐标系内半径，取值在0到1之间
             */
            innerRadius: PropTypes.number
        })
    }),

    /**
     * 热力网格中图形的尺寸比例，当shape或sizeField定义时有效
     */
    sizeRatio: PropTypes.number,

    // 配置热力图样式
    heatmapStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 设置x坐标轴相关属性
    xAxis: axisBasePropTypes,

    // 设置y坐标轴相关属性
    yAxis: axisBasePropTypes,

    /**
     * 定义图表容器像素宽度
     * 默认：400
     */
    width: PropTypes.number,

    /**
     * 定义图表容器像素高度
     * 默认：400
     */
    height: PropTypes.number,

    /**
     * 图表是否自适应容器宽高，当设置为true时，width与height参数将失效
     * 默认：true
     */
    autoFit: PropTypes.bool,

    /**
     * 定义图表四个方向的空白间距值，可以为单个数字譬如16，也可以为四个数字构成的数组，
     * 按顺序代表上-右-下-左分别的像素间距
     */
    padding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.string
    ]),

    /**
     * 定义在padding基础上额外的像素填充间距
     */
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.string
    ]),

    /**
     * 图表渲染模式，可选的有'canvas'、'svg'
     * 默认：'canvas'
     */
    renderer: PropTypes.oneOf(['canvas', 'svg']),

    /**
     * canvas模式下，控制渲染图表图片的像素比
     * 默认：1
     */
    pixelRatio: PropTypes.number,

    /**
     * 设置语言，可选的有'zh-CN'与'en-US'
     */
    locale: PropTypes.oneOf(['zh-CN', 'en-US']),

    /**
     * 是否对超出绘图区域的几何元素进行裁剪
     */
    limitInPlot: PropTypes.bool,

    // 配置图例相关参数
    legend: legendBasePropTypes,

    // 配置文字标签相关参数
    label: labelBasePropTypes,

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

    // 配置标注相关参数
    annotations: annotationsBasePropTypes,

    /**
     * 配置图形填充贴图样式
     */
    pattern: patternBasePropTypes,

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

    // 热力网格点击事件
    recentlyGridClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.object
    }),

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

    /**
     * 交互功能项配置
     */
    interactions: interactionsBasePropTypes,

    /**
     * 状态样式配置
     */
    state: stateBasePropTypes,

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
AntdHeatmap.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdHeatmap;

export const propTypes = AntdHeatmap.propTypes;
export const defaultProps = AntdHeatmap.defaultProps;