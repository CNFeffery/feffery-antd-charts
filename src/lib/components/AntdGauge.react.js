/* eslint-disable no-inline-comments */
/* eslint-disable no-magic-numbers */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    baseStyle,
    textBaseStyle,
    axisBasePropTypes,
    themeBasePropTypes
} from './BasePropTypes.react';

const LazyAntdGauge = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdGauge.react'));

const AntdGauge = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdGauge {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdGauge.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置当前仪表盘百分比，必填
    percent: PropTypes.number.isRequired,

    // 设置仪表盘相对画布的外环半径大小，取值应在0~1之间，默认为0.95
    radius: PropTypes.number,

    // 设置仪表盘相对画布的内环半径大小，取值应在0~1之间，默认为0.9
    innerRadius: PropTypes.number,

    // 设置仪表盘的开始角度，弧度制，默认为(-7 / 6) * pi
    startAngle: PropTypes.number,

    // 设置仪表盘的终止角度，弧度制，默认为(1 / 6) * pi
    endAngle: PropTypes.number,

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

    // 设置仪表盘辅助圆弧样式
    range: PropTypes.exact({
        // 设置辅助圆弧显示刻度的数值数组
        ticks: PropTypes.arrayOf(PropTypes.number),
        // 设置辅助圆弧的背景色
        color: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        // 设置辅助圆弧的像素宽度，不设置时圆弧宽度由radius、innerRadius参数按比例控制
        width: PropTypes.number
    }),

    // 设置仪表盘类型，可选项为'meter'
    type: PropTypes.oneOf(['meter']),

    // 当type='meter'时用于进行仪表盘样式的具体配置
    meter: PropTypes.exact({
        // 仪表盘总步数，默认为50
        steps: PropTypes.number,
        // 设置分步刻度与间距之间的宽度比例关系，默认为0.5
        stepRatio: PropTypes.number
    }),

    // 配置仪表盘样式
    gaugeStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调函数
            func: PropTypes.string
        })
    ]),

    // 设置坐标轴相关属性
    axis: axisBasePropTypes,

    // 配置仪表盘指示器样式
    indicator: PropTypes.exact({
        // 配置指示器指针样式
        pointer: PropTypes.exact({
            style: baseStyle
        }),
        // 配置指示器圆盘样式
        pin: PropTypes.exact({
            style: baseStyle
        }),

        // 配置指示器指针类型，可选的有'default'、'cursor'、'ring-cursor'、'simple'
        shape: PropTypes.oneOf(['default', 'cursor', 'ring-cursor', 'simple'])
    }),

    // 配置仪表盘中心文本内容
    statistic: PropTypes.exact({
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
        style: textBaseStyle
    }),

    // 配置动画相关参数
    animation: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.bool
    ]),

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
AntdGauge.defaultProps = {
    radius: 0.95,
    downloadTrigger: 'download-trigger'
}

export default AntdGauge;

export const propTypes = AntdGauge.propTypes;
export const defaultProps = AntdGauge.defaultProps;