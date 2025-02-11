/* eslint-disable no-inline-comments */
/* eslint-disable no-magic-numbers */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import { useLoading } from './utils';
import {
    baseStyle,
    axisBasePropTypes,
    themeBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes
} from './BasePropTypes.react';

const LazyAntdGauge = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdGauge.react'));

/**
 * 仪表盘组件AntdGauge
 */
const AntdGauge = ({
    locale = 'zh-CN',
    downloadTrigger = 'download-trigger',
    radius = 0.95,
    ...others
}) => {

    const component_loading = useLoading();

    return (
        <Suspense fallback={null}>
            <LazyAntdGauge {
                ...{
                    locale,
                    downloadTrigger,
                    radius,
                    component_loading,
                    ...others
                }
            } />
        </Suspense>
    );
}

AntdGauge.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前仪表盘实际值，取值应在`0`到`1`之间
     */
    percent: PropTypes.number.isRequired,

    /**
     * 仪表盘相对画布的外环半径尺寸，取值应在`0`到`1`之间
     * 默认值：`0.95`
     */
    radius: PropTypes.number,

    /**
     * 仪表盘相对画布的内环半径大小，取值应在`0`到`1`之间
     * 默认值：`0.9`
     */
    innerRadius: PropTypes.number,

    /**
     * 仪表盘开始角度，弧度制
     * 默认值：`(-7 / 6) * π`
     */
    startAngle: PropTypes.number,

    /**
     * 仪表盘终止角度，弧度制
     * 默认值：`(1 / 6) * π`
     */
    endAngle: PropTypes.number,

    /**
     * 图表容器像素宽度
     */
    width: PropTypes.number,

    /**
     * 图表容器像素高度
     */
    height: PropTypes.number,

    /**
     * 图表是否自适应所在父容器宽高，当`autoFit=True`时，`width`和`height`参数将失效
     * 默认值：`true`
     */
    autoFit: PropTypes.bool,

    /**
     * 画布内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组，或传入`'auto'`开启底层自动计算
     */
    padding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.oneOf(['auto'])
    ]),

    /**
     * 画布额外内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组
     */
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number)
    ]),

    /**
     * 图表底层渲染方式，可选项有`'canvas'`和`'svg'`
     * 默认值：`'canvas'`
     */
    renderer: PropTypes.oneOf(['canvas', 'svg']),

    /**
     * `renderer='canvas'`时，控制渲染图表图片的像素比
     * 默认值：`1`
     */
    pixelRatio: PropTypes.number,

    /**
     * 图表文案语种，可选项有`'zh-CN'`、`'en-US'`
     * 默认值：`'zh-CN'`
     */
    locale: PropTypes.oneOf(['zh-CN', 'en-US']),

    /**
     * 是否对超出绘图区域的几何元素进行裁剪
     */
    limitInPlot: PropTypes.bool,

    /**
     * 配置仪表盘辅助圆弧，具体见在线文档相关说明
     */
    range: PropTypes.exact({
        /**
         * 辅助圆弧显示刻度值数组
         */
        ticks: PropTypes.arrayOf(PropTypes.number),
        /**
         * 辅助圆弧背景色，传入数组时表示渐变色
         */
        color: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        /**
         * 辅助圆弧像素宽度
         */
        width: PropTypes.number
    }),

    /**
     * 仪表盘类型，可选项有`'meter'`
     */
    type: PropTypes.oneOf(['meter']),

    /**
     * 针对`type='meter'`的仪表盘进行配置
     */
    meter: PropTypes.exact({
        /**
         * 仪表盘总步数
         * 默认值：`50`
         */
        steps: PropTypes.number,
        /**
         * 分步刻度与对应间距的宽度比例关系
         * 默认值：`0.5`
         */
        stepRatio: PropTypes.number
    }),

    /**
     * 控制仪表盘样式，具体见在线文档相关说明
     */
    gaugeStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
     * 配置坐标轴相关参数，具体见在线文档相关说明
     */
    axis: axisBasePropTypes,

    /**
     * 配置仪表盘指示器，具体见在线文档相关说明
     */
    indicator: PropTypes.exact({
        /**
         * 配置指示器指针
         */
        pointer: PropTypes.exact({
            /**
             * 配置指示器指针样式
             */
            style: baseStyle
        }),
        /**
         * 配置指示器圆盘
         */
        pin: PropTypes.exact({
            /**
             * 配置指示器圆盘样式
             */
            style: baseStyle
        }),
        /**
         * 指示器指针类型，可选项有`'default'`、`'cursor'`、`'ring-cursor'`、`'simple'`
         */
        shape: PropTypes.oneOf(['default', 'cursor', 'ring-cursor', 'simple'])
    }),

    /**
     * 配置仪表盘中心统计内容，具体见在线文档相关说明
     */
    statistic: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.exact({
            /**
             * 配置统计内容标题，设置为`False`时将隐藏标题
             */
            title: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 统计内容标题样式
                     */
                    style: PropTypes.object,
                    /**
                     * 配置统计内容标题文本
                     */
                    content: PropTypes.string,
                    /**
                     * 格式化统计内容标题文本函数
                     */
                    formatter: PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string
                    }),
                    /**
                     * 配置统计内容标题原始html文本内容
                     */
                    customHtml: PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string
                    }),
                    /**
                     * 标题旋转角度
                     */
                    rotate: PropTypes.number,
                    /**
                     * 标题水平像素偏移
                     */
                    offsetX: PropTypes.number,
                    /**
                     * 标题竖直像素偏移
                     */
                    offsetY: PropTypes.number
                })
            ]),
            /**
             * 配置统计内容，设置为`False`时将隐藏内容
             */
            content: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 统计内容样式
                     */
                    style: PropTypes.object,
                    /**
                     * 配置统计内容文本
                     */
                    content: PropTypes.string,
                    /**
                     * 格式化统计内容文本函数
                     */
                    formatter: PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string
                    }),
                    /**
                     * 配置统计内容原始html文本内容
                     */
                    customHtml: PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string
                    }),
                    /**
                     * 标题旋转角度
                     */
                    rotate: PropTypes.number,
                    /**
                     * 标题水平像素偏移
                     */
                    offsetX: PropTypes.number,
                    /**
                     * 标题竖直像素偏移
                     */
                    offsetY: PropTypes.number
                })
            ]),
            /**
             * 统计内容样式
             */
            style: baseStyle
        })
    ]),

    /**
     * 配置动画相关参数，具体见在线文档相关说明
     */
    animation: animationBasePropTypes,

    /**
     * 对当前组件的`downloadTrigger`值进行更新，可实现主动下载当前图表为`png`格式图片
     */
    downloadTrigger: PropTypes.string,

    /**
     * 配置主题相关参数，具体见在线文档相关说明
     */
    theme: themeBasePropTypes,

    /**
     * 配置交互功能相关参数，具体见在线文档相关说明
     */
    interactions: interactionsBasePropTypes,

    /**
     * 配置状态样式相关参数，具体见在线文档相关说明
     */
    state: stateBasePropTypes,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default AntdGauge;

export const propTypes = AntdGauge.propTypes;
export const defaultProps = AntdGauge.defaultProps;