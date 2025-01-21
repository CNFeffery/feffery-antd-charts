/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable prefer-const */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    metaBasePropTypes,
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

const LazyAntdPie = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdPie.react'));

/**
 * 饼图组件AntdPie
 */
const AntdPie = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdPie {...props} />
        </Suspense>
    );
}

AntdPie.propTypes = {
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
     * css样式
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
     * 扇形角度字段
     */
    angleField: PropTypes.string,

    /**
     * 扇形颜色字段
     */
    colorField: PropTypes.string,

    /**
     * 饼图外半径，取值应在`0`到`1`之间
     */
    radius: PropTypes.number,

    /**
     * 饼图内半径，取值应在`0`到`1`之间
     */
    innerRadius: PropTypes.number,

    /**
     * 饼图起始角度，弧度制
     */
    startAngle: PropTypes.number,

    /**
     * 饼图结束角度，弧度制
     */
    endAngle: PropTypes.number,

    /**
     * 控制扇形填充颜色，具体见在线文档相关说明
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
     * `innerRadius`有效时可用，配置饼图中心统计内容，具体见在线文档相关说明
     */
    statistic: PropTypes.oneOfType([
        PropTypes.exact({
            /**
             * 配置统计内容标题，设置为`False`时将隐藏标题
             */
            title: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 统计内容标题css样式
                     */
                    style: PropTypes.object,
                    /**
                     * 配置统计内容标题文本
                     */
                    content: PropTypes.string,
                    /**
                     * 统计内容`javascript`格式化函数
                     */
                    formatter: PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string
                    }),
                    /**
                     * 统计内容标题动态html渲染`javascript`函数
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
        }),
        PropTypes.bool
    ]),

    /**
     * 控制扇形填充样式，具体见在线文档相关说明
     */
    pieStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

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
     * 事件监听属性，用于监听最近一次扇形点击事件
     */
    recentlySectorClickRecord: PropTypes.exact({
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

AntdPie.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdPie;

export const propTypes = AntdPie.propTypes;
export const defaultProps = AntdPie.defaultProps;