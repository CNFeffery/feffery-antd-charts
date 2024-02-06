/* eslint-disable no-inline-comments */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    axisBasePropTypes,
    annotationsBasePropTypes,
    themeBasePropTypes,
    animationBasePropTypes,
    baseStyle
} from './BasePropTypes.react';

const LazyAntdProgress = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdProgress.react'));

const AntdProgress = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdProgress {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdProgress.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    /**
     * 必填，设置百分比数值，取值应在0到1
     */
    percent: PropTypes.number.isRequired,

    /**
     * 设置进度条宽度占比，取值应在0到1之间
     * 默认：0.5
     */
    barWidthRatio: PropTypes.number,

    /**
     * 配置进度条颜色
     */
    color: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 设置进度条样式
     */
    progressStyle: PropTypes.oneOfType([
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

    // 配置标注相关参数
    annotations: annotationsBasePropTypes,

    // 配置动画相关参数
    animation: animationBasePropTypes,

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

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
AntdProgress.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdProgress;

export const propTypes = AntdProgress.propTypes;
export const defaultProps = AntdProgress.defaultProps;