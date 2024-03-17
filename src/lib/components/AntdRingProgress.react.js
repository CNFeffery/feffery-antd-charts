/* eslint-disable no-inline-comments */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    annotationsBasePropTypes,
    themeBasePropTypes,
    animationBasePropTypes,
    baseStyle
} from './BasePropTypes.react';

const LazyAntdRingProgress = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdRingProgress.react'));

const AntdRingProgress = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdRingProgress {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdRingProgress.propTypes = {
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
     * 设置外环半径，取值应在0到1之间
     */
    radius: PropTypes.number,

    /**
     * 设置内环半径，取值应在0到1之间
     */
    innerRadius: PropTypes.number,

    /**
     * 配置进度环颜色
     */
    color: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    /**
     * 设置进度环样式
     */
    progressStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

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

    /**
     * canvas模式下，控制渲染图表图片的像素比
     * 默认：1
     */
    pixelRatio: PropTypes.number,

    // 设置语言，可选的有'zh-CN'与'en-US'
    locale: PropTypes.oneOf(['zh-CN', 'en-US']),

    // 设置是否对超出绘图区域的几何元素进行裁剪
    limitInPlot: PropTypes.bool,

    // 配置标注相关参数
    annotations: annotationsBasePropTypes,

    // 配置动画相关参数
    animation: animationBasePropTypes,

    statistic: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.exact({
            // 配置统计内容标题，设置为false时隐藏标题
            title: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    // 配置统计文本的css样式
                    style: PropTypes.object,

                    // 配置标题文本内容，优先级：customHtml > formatter > content
                    content: PropTypes.string,

                    // 回调自定义标题文本信息
                    formatter: PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string
                    }),

                    // 回调自定义标题文本信息，优先级最高
                    // 格式：(container, view, datum, data) => string
                    customHtml: PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string
                    }),

                    // 设置标题的旋转角度
                    rotate: PropTypes.number,

                    // 设置标题的水平方向偏移像素值
                    offsetX: PropTypes.number,

                    // 设置标题的竖直方向偏移像素值
                    offsetY: PropTypes.number
                })
            ]),

            // 配置统计内容主体信息，设置为false时隐藏标题
            content: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    // 配置统计文本的css样式
                    style: PropTypes.object,

                    // 配置主体信息文本内容，优先级：customHtml > formatter > content
                    content: PropTypes.string,

                    // 回调自定义主体信息文本信息
                    formatter: PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string
                    }),

                    // 回调自定义标题文本信息，优先级最高
                    // 格式：(container, view, datum, data) => string
                    customHtml: PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string
                    }),

                    // 设置主体信息旋转角度
                    rotate: PropTypes.number,

                    // 设置主体信息的水平方向偏移像素值
                    offsetX: PropTypes.number,

                    // 设置主体信息的竖直方向偏移像素值
                    offsetY: PropTypes.number
                })
            ]),
            style: baseStyle
        })
    ]),

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
AntdRingProgress.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdRingProgress;

export const propTypes = AntdRingProgress.propTypes;
export const defaultProps = AntdRingProgress.defaultProps;