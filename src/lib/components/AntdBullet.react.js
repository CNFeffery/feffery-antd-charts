/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    metaBasePropTypes,
    baseStyle,
    labelBasePropTypes,
    tooltipBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    themeBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes
} from './BasePropTypes.react';

const LazyAntdBullet = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdBullet.react'));

/**
 * 子弹图组件AntdBullet
 */
const AntdBullet = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdBullet {...props} />
        </Suspense>
    );
}

AntdBullet.propTypes = {
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
     * 必填，定义绘图所需数据，格式如`[{title: '满意度', ranges: [50, 100], measures: [80], target: 85}]`
     */
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    /**
     * 以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明
     */
    meta: metaBasePropTypes,

    /**
     * 必填，子弹图长度字段
     */
    measureField: PropTypes.string.isRequired,

    /**
     * 必填，子弹图背景条字段
     */
    rangeField: PropTypes.string.isRequired,

    /**
     * 必填，子弹图目标值字段
     */
    targetField: PropTypes.string.isRequired,

    /**
     * 必填，子弹图分组字段
     */
    xField: PropTypes.string,

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
     * 布局方向，可选项有`'horizontal'`、`'vertical'`
     * 默认值：`'horizontal'`
     */
    layout: PropTypes.oneOf(['horizontal', 'vertical']),

    /**
     * 控制子弹图各部分填充颜色，具体见在线文档相关说明
     */
    color: PropTypes.exact({
        /**
         * 区间背景颜色
         */
        range: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        /**
         * 实际值颜色
         */
        measure: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        /**
         * 目标值颜色
         */
        target: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ])
    }),

    /**
     * 配置子弹图各部分尺寸，具体见在线文档相关说明
     */
    size: PropTypes.exact({
        /**
         * 区间背景像素尺寸
         */
        range: PropTypes.oneOfType([
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
         * 实际值像素尺寸
         */
        measure: PropTypes.oneOfType([
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
         * 目标值像素尺寸
         */
        target: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number),
            PropTypes.exact({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            })
        ])
    }),

    /**
     * 控制子弹图各部分样式，具体见在线文档相关说明
     */
    bulletStyle: PropTypes.exact({
        /**
         * 区间背景样式
         */
        range: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            })
        ]),
        /**
         * 实际值样式
         */
        measure: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            })
        ]),
        /**
         * 目标值样式
         */
        target: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            })
        ])
    }),

    /**
     * 配置子弹图各部分数值标签，具体见在线文档相关说明
     */
    label: PropTypes.exact({
        /**
         * 区间数值标签
         */
        range: labelBasePropTypes,
        /**
         * 实际值标签
         */
        measure: labelBasePropTypes,
        /**
         * 目标值标签
         */
        target: labelBasePropTypes
    }),

    /**
     * 配置信息框相关参数，具体见在线文档相关说明
     */
    tooltip: tooltipBasePropTypes,

    /**
     * 配置图例相关参数，具体见在线文档相关说明
     */
    legend: legendBasePropTypes,

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

AntdBullet.defaultProps = {
    locale: 'zh-CN',
    layout: 'horizontal',
    downloadTrigger: 'download-trigger'
}

export default AntdBullet;

export const propTypes = AntdBullet.propTypes;
export const defaultProps = AntdBullet.defaultProps;