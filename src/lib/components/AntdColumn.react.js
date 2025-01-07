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
    themeBasePropTypes,
    patternBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes
} from './BasePropTypes.react';

const LazyAntdColumn = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdColumn.react'));

/**
 * 柱状图组件AntdColumn
 */
const AntdColumn = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdColumn {...props} />
        </Suspense>
    );
}

AntdColumn.propTypes = {
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
     * 图表分组字段
     */
    seriesField: PropTypes.string,

    /**
     * `isGroup=True`时有效，用于针对堆叠分组条形图指定分组字段
     */
    groupField: PropTypes.string,

    /**
     * `seriesField`有效时，是否渲染堆叠条形图
     */
    isStack: PropTypes.bool,

    /**
     * `seriesField`有效时，是否渲染分组条形图
     */
    isGroup: PropTypes.bool,

    /**
     * 当`yField`对应数据项满足格式`[区间开始值, 区间结束值]`时，用于控制是否渲染区间条形图
     */
    isRange: PropTypes.bool,

    /**
     * 是否渲染为百分比条形图，需配合设置`isStack=True`
     */
    isPercent: PropTypes.bool,

    /**
     * 控制柱体填充颜色，具体见在线文档相关说明
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
     * 配置缩略轴相关参数，具体见在线文档相关说明
     */
    slider: sliderBasePropTypes,

    /**
     * 分组柱状图组间间隔像素宽度
     */
    intervalPadding: PropTypes.number,

    /**
     * 分组柱状图组内间隔像素宽度
     */
    dodgePadding: PropTypes.number,

    /**
     * 柱状图最小像素宽度
     */
    minColumnWidth: PropTypes.number,

    /**
     * 柱状图最大像素宽度
     */
    maxColumnWidth: PropTypes.number,

    /**
     * 控制柱体填充样式，具体见在线文档相关说明
     */
    columnStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
     * 配置柱体背景相关参数，具体见在线文档相关说明
     */
    columnBackground: PropTypes.exact({
        /**
         * 柱体背景颜色
         */
        style: baseStyle
    }),

    /**
     * 柱体宽度比例，取值在`0`到`1`之间
     */
    columnWidthRatio: PropTypes.number,

    /**
     * 分组柱体间隔宽度比例，取值在`0`到`1`之间
     */
    marginRatio: PropTypes.number,

    /**
     * 配置滚动条相关参数，具体见在线文档相关说明
     */
    scrollbar: scrollbarBasePropTypes,

    /**
     * 配置转化标签相关参数，具体见在线文档相关说明
     */
    conversionTag: PropTypes.exact({
        /**
         * 转化率标签像素尺寸
         */
        size: PropTypes.number,
        /**
         * 转化率标签与条形之间的像素间距
         */
        spacing: PropTypes.number,
        /**
         * 组件与坐标轴之间的像素距离
         */
        offset: PropTypes.number,
        /**
         * 配置转化率组件箭头样式，设置为`False`时不显示箭头
         */
        arrow: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.exact({
                /**
                 * 箭头像素尺寸
                 */
                headSize: PropTypes.number
            })
        ]),
        /**
         * 配置转化率组件文本，设置为`False`时不显示文本
         */
        text: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.exact({
                /**
                 * 自定义转化率计算参数
                 */
                formatter: PropTypes.exact({
                    /**
                     * js函数体字符串
                     */
                    func: PropTypes.string
                }),
                /**
                 * 转化率文本样式
                 */
                style: baseStyle
            })
        ])
    }),

    /**
     * 配置联通对比区域相关参数，具体见在线文档相关说明
     */
    connectedArea: PropTypes.oneOfType([
        PropTypes.exact({
            /**
             * 触发方式，可选项有`'hover'`、`'click'`，设置为`False`时不触发
             */
            trigger: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.string
            ])
        }),
        PropTypes.bool
    ]),

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
     * 事件监听属性，用于监听最近一次柱体点击事件
     */
    recentlyColumnClickRecord: PropTypes.exact({
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
     * 配置图形填充贴图相关参数，具体见在线文档相关说明
     */
    pattern: patternBasePropTypes,

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

AntdColumn.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdColumn;

export const propTypes = AntdColumn.propTypes;
export const defaultProps = AntdColumn.defaultProps;