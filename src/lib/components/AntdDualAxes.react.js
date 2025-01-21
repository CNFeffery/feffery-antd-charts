/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    baseStyle,
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    sliderBasePropTypes,
    themeBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes
} from './BasePropTypes.react';

const LazyAntdDualAxes = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdDualAxes.react'));

/**
 * 双轴图组件AntdDualAxes
 */
const AntdDualAxes = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdDualAxes {...props} />
        </Suspense>
    );
}

AntdDualAxes.propTypes = {
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
    data: PropTypes.arrayOf(PropTypes.arrayOf(PropTypes.object)).isRequired,

    /**
     * 以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明
     */
    meta: metaBasePropTypes,

    /**
     * 必填，图表x轴字段
     */
    xField: PropTypes.string.isRequired,

    /**
     * 必填，图表y轴字段，格式如`[左轴字段, 右轴字段]`
     */
    yField: PropTypes.arrayOf(PropTypes.string).isRequired,

    /**
     * 分别配置左右轴相关参数，格式如`[左轴配置, 右轴配置]`，具体见在线文档相关说明
     */
    geometryOptions: PropTypes.arrayOf(
        PropTypes.oneOfType([
            /**
             * 适用于折线图类型的配置
             */
            PropTypes.shape({
                /**
                 * 当前轴图表类型，可选项为`'line'`（折线图）、`'column'`（柱状图）
                 */
                geometry: PropTypes.oneOf(['line', 'column']),
                /**
                 * 当前轴分组字段
                 */
                seriesField: PropTypes.string,
                /**
                 * 针对折线图是否渲染为光滑曲线
                 * 默认值：`false`
                 */
                smooth: PropTypes.bool,
                /**
                 * 针对折线图中的缺失值片段，是否对空数据段两端进行连线
                 * 默认值：`true`
                 */
                connectNulls: PropTypes.bool,
                /**
                 * 控制折线样式，具体见在线文档相关说明
                 */
                lineStyle: PropTypes.oneOfType([
                    baseStyle,
                    PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string,
                    }),
                ]),
                /**
                 * 配置折点相关参数，具体见在线文档相关说明
                 */
                point: PropTypes.exact({
                    /**
                     * 配置折点颜色，具体见在线文档相关说明
                     */
                    color: PropTypes.oneOfType([
                        PropTypes.string,
                        PropTypes.arrayOf(PropTypes.string),
                        PropTypes.exact({
                            /**
                             * js函数体字符串
                             */
                            func: PropTypes.string,
                        }),
                    ]),
                    /**
                     * 配置折点形状，具体见在线文档相关说明
                     */
                    shape: PropTypes.oneOfType([
                        PropTypes.string,
                        PropTypes.exact({
                            /**
                             * js函数体字符串
                             */
                            func: PropTypes.string,
                        }),
                    ]),
                    /**
                     * 配置折点样式，具体见在线文档相关说明
                     */
                    style: PropTypes.oneOfType([
                        baseStyle,
                        PropTypes.exact({
                            /**
                             * js函数体字符串
                             */
                            func: PropTypes.string,
                        }),
                    ]),
                }),
                /**
                 * 配置数值标签相关参数，具体见在线文档相关说明
                 */
                label: labelBasePropTypes,
                /**
                 * 控制折线颜色，具体见在线文档相关说明
                 */
                color: PropTypes.oneOfType([
                    PropTypes.string,
                    PropTypes.arrayOf(PropTypes.string),
                    PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string,
                    }),
                ]),
                /**
                 * 阶梯折线图类型，可选项有`'hv'`、`'vh'`、`'hvh'`、`'vhv'`，其中`'h'`代表水平方向，`'v'`代表竖直方向，譬如`'vh`就代表先竖直再水平
                 */
                stepType: PropTypes.string,
            }),
            /**
             * 适用于柱状图类型的配置
             */
            PropTypes.shape({
                /**
                 * 当前轴图表类型，可选项为`'line'`（折线图）、`'column'`（柱状图）
                 */
                geometry: PropTypes.oneOf(['line', 'column']),
                /**
                 * 当前轴分组字段
                 */
                seriesField: PropTypes.string,
                /**
                 * `isGroup=True`时有效，用于针对堆叠分组条形图指定分组字段
                 */
                groupField: PropTypes.string,
                /**
                 * `seriesField`有效时，是否渲染分组条形图
                 */
                isGroup: PropTypes.bool,
                /**
                 * `seriesField`有效时，是否渲染堆叠条形图
                 */
                isStack: PropTypes.bool,
                /**
                 * 柱体宽度比例，取值在`0`到`1`之间
                 */
                columnWidthRatio: PropTypes.number,
                /**
                 * 分组柱体间隔宽度比例，取值在`0`到`1`之间
                 */
                marginRatio: PropTypes.number,
                /**
                 * 控制柱体填充样式，具体见在线文档相关说明
                 */
                columnStyle: PropTypes.oneOfType([
                    baseStyle,
                    PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string,
                    }),
                ]),
                /**
                 * 配置数值标签相关参数，具体见在线文档相关说明
                 */
                label: labelBasePropTypes,
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
                        func: PropTypes.string,
                    }),
                ]),
            }),
        ])
    ),

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
        PropTypes.oneOf(['auto']),
    ]),

    /**
     * 画布额外内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组
     */
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
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
     * 配置信息框相关参数，具体见在线文档相关说明
     */
    tooltip: tooltipBasePropTypes,

    /**
     * 配置横坐标轴相关参数，具体见在线文档相关说明
     */
    xAxis: axisBasePropTypes,

    /**
     * 配置纵坐标轴相关参数，具体见在线文档相关说明
     */
    yAxis: PropTypes.objectOf(axisBasePropTypes),

    /**
     * 配置标注相关参数，具体见在线文档相关说明
     */
    annotations: PropTypes.objectOf(annotationsBasePropTypes),

    /**
     * 配置图例相关参数，具体见在线文档相关说明
     */
    legend: legendBasePropTypes,

    /**
     * 配置缩略轴相关参数，具体见在线文档相关说明
     */
    slider: sliderBasePropTypes,

    /**
     * 配置动画相关参数，具体见在线文档相关说明
     */
    animation: animationBasePropTypes,

    /**
     * 事件监听属性，用于监听最近一次数据项点击事件
     */
    recentlyClickRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.object,
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
        component_name: PropTypes.string,
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

AntdDualAxes.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger',
};

export default AntdDualAxes;

export const propTypes = AntdDualAxes.propTypes;
export const defaultProps = AntdDualAxes.defaultProps;