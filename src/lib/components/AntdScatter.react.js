/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import { useLoading } from './utils';
import {
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    baseStyle,
    themeBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes,
    brushBasePropTypes
} from './BasePropTypes.react';

const LazyAntdScatter = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdScatter.react'));

/**
 * 散点图组件AntdScatter
 */
const AntdScatter = ({
    locale = 'zh-CN',
    downloadTrigger = 'download-trigger',
    ...others
}) => {

    const component_loading = useLoading();

    return (
        <Suspense fallback={null}>
            <LazyAntdScatter {
                ...{
                    locale,
                    downloadTrigger,
                    component_loading,
                    ...others
                }
            } />
        </Suspense>
    );
}

AntdScatter.propTypes = {
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
     * 必填，定义绘图所需数据
     */
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    /**
     * 以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明
     */
    meta: metaBasePropTypes,

    /**
     * 必填，图表x轴字段
     */
    xField: PropTypes.string.isRequired,

    /**
     * 必填，图表y轴字段
     */
    yField: PropTypes.string.isRequired,

    /**
     * 颜色映射字段
     */
    colorField: PropTypes.string,

    /**
     * 尺寸映射字段
     */
    sizeField: PropTypes.string,

    /**
     * 形状映射字段
     */
    shapeField: PropTypes.string,

    /**
     * 控制散点颜色，具体见在线文档相关说明
     */
    color: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
     * 控制散点尺寸，具体见在线文档相关说明
     */
    size: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
    * 控制散点形状，具体见在线文档相关说明
    */
    shape: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
     * 控制散点样式，具体见在线文档相关说明
     */
    pointStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
     * 是否为散点形状渲染图例
     */
    shapeLegend: legendBasePropTypes,

    /**
     * 是否为散点尺寸渲染图例
     */
    sizeLegend: legendBasePropTypes,

    /**
     * 配置象限相关参数，具体见在线文档相关说明
     */
    quadrant: PropTypes.exact({
        /**
         * 横轴基准分割线位置
         * 默认值：`0`
         */
        xBaseline: PropTypes.number,
        /**
         * 纵轴基准分割线位置
         * 默认值：`0`
         */
        yBaseline: PropTypes.number,
        /**
         * 配置分割线样式
         */
        lineStyle: baseStyle,
        /**
         * 配置象限样式，支持传入格式如`[左上, 右上, 右下, 左下]`格式的参数分别配置四个象限的样式
         */
        regionStyle: PropTypes.oneOfType([
            baseStyle,
            PropTypes.arrayOf(baseStyle)
        ]),
        /**
         * 配置各象限文字标注，格式如`[左上, 右上, 右下, 左下]`
         */
        labels: PropTypes.arrayOf(
            PropTypes.exact({
                /**
                 * 标注文字内容
                 */
                content: PropTypes.string,
                /**
                 * 标注坐标位置，格式如`[x, y]`
                 */
                position: PropTypes.arrayOf(PropTypes.number),
                /**
                 * 标注文字样式
                 */
                style: baseStyle
            })
        )
    }),

    /**
     * 配置回归线相关参数，具体见在线文档相关说明
     */
    regressionLine: PropTypes.exact({
        /**
         * 回归线类型，可选项有`'exp'`、`'linear'`、`'loess'`、`'log'`、`'poly'`、`'pow'`、`'quad'`
         */
        type: PropTypes.oneOf(['exp', 'linear', 'loess', 'log', 'poly', 'pow', 'quad']),
        /**
         * 回归线样式
         */
        style: baseStyle,
        /**
         * 自定义回归线数值映射算法
         */
        algorithm: PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        }),
        /**
         * 回归线是否置于顶层显示
         */
        top: PropTypes.bool
    }),

    /**
     * 配置横坐标轴相关参数，具体见在线文档相关说明
     */
    xAxis: axisBasePropTypes,

    /**
     * 配置纵坐标轴相关参数，具体见在线文档相关说明
     */
    yAxis: axisBasePropTypes,

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
        PropTypes.string
    ]),

    /**
     * 画布额外内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组
     */
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.string
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
     * 配置图例相关参数，具体见在线文档相关说明
     */
    legend: legendBasePropTypes,

    /**
     * 配置数值标签相关参数，具体见在线文档相关说明
     */
    label: labelBasePropTypes,

    /**
     * 配置信息框相关参数，具体见在线文档相关说明
     */
    tooltip: tooltipBasePropTypes,

    /**
     * 配置标注相关参数，具体见在线文档相关说明
     */
    annotations: annotationsBasePropTypes,

    /**
     * 配置动画相关参数，具体见在线文档相关说明
     */
    animation: animationBasePropTypes,

    /**
     * 事件监听属性，用于监听最近一次信息框显示事件
     */
    recentlyTooltipChangeRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.arrayOf(PropTypes.object)
    }),

    /**
     * 事件监听属性，用于监听最近一次散点点击事件
     */
    recentlyPointClickRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.object
    }),

    /**
     * 事件监听属性，用于监听最近一次散点双击事件
     */
    recentlyPointDoubleClickRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.object
    }),

    /**
     * 事件监听属性，用于监听最近一次图例点击事件
     */
    recentlyLegendInfo: PropTypes.exact({
        /**
         * 被点击图例项名称
         */
        triggerItemName: PropTypes.any,
        /**
         * 当前各图例项信息
         */
        items: PropTypes.arrayOf(
            PropTypes.object
        )
    }),

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
     * 配置刷选相关功能，具体见在线文档相关说明
     */
    brush: brushBasePropTypes,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default AntdScatter;

export const propTypes = AntdScatter.propTypes;
export const defaultProps = AntdScatter.defaultProps;