/* eslint-disable no-inline-comments */
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
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    themeBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes,
    patternBasePropTypes,
    areaBaseStyle
} from './BasePropTypes.react';

const LazyAntdTinyArea = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdTinyArea.react'));

const AntdTinyArea = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdTinyArea {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdTinyArea.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 定义绘图所需数据，必须参数
    data: PropTypes.arrayOf(PropTypes.number).isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 设置是否以平滑曲线方式渲染折线，默认为false
    smooth: PropTypes.bool,

    // 设置面积图颜色
    color: PropTypes.string,

    /**
     * 设置面积区域样式
     */
    areaStyle: areaBaseStyle,

    /**
     * 配置折线样式
     */
    line: PropTypes.exact({
        /**
         * 设置折线颜色
         */
        color: PropTypes.string,
        /**
         * 设置折线样式
         */
        style: lineBaseStyle
    }),

    /**
     * 配置折点样式
     */
    point: PropTypes.exact({
        /**
         * 设置折点颜色
         */
        color: PropTypes.string,
        /**
         * 设置折点样式
         */
        style: pointBaseStyle
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
        PropTypes.oneOf(['auto'])
    ]),

    // 定义在padding基础上额外的像素填充间距
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number)
    ]),

    // 设置图表渲染方式为'canvas'或'svg'模式，默认为'canvas'
    renderer: PropTypes.oneOf(['canvas', 'svg']),

    // 设置语言，可选的有'zh-CN'与'en-US'
    locale: PropTypes.oneOf(['zh-CN', 'en-US']),

    // 设置是否对超出绘图区域的几何元素进行裁剪
    limitInPlot: PropTypes.bool,

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
AntdTinyArea.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdTinyArea;

export const propTypes = AntdTinyArea.propTypes;
export const defaultProps = AntdTinyArea.defaultProps;