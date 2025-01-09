/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    baseStyle,
    metaBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    themeBasePropTypes,
    patternBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes
} from './BasePropTypes.react';

const LazyAntdSunburst = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdSunburst.react'));

/**
 * 旭日图组件AntdSunburst
 */
const AntdSunburst = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdSunburst {...props} />
        </Suspense>
    );
}

AntdSunburst.propTypes = {
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
    data: PropTypes.object.isRequired,

    /**
     * 以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明
     */
    meta: metaBasePropTypes,

    /**
     * 色彩区分字段，默认为根节点的`name`字段
     */
    colorField: PropTypes.string,

    /**
     * 声明额外辅助字段
     */
    rawFields: PropTypes.arrayOf(PropTypes.string),

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
     * 配置层次布局相关参数，具体见在线文档相关说明
     */
    hierarchyConfig: PropTypes.exact({
        /**
         * 节点权重字段
         * 默认值：`'value'`
         */
        field: PropTypes.string,
        /**
         * 是否忽略父节点实际权重
         * 默认值：`true`
         */
        ignoreParentValue: PropTypes.bool
    }),

    /**
     * 配置下钻交互相关参数，具体见在线文档相关说明
     */
    drilldown: PropTypes.exact({
        /**
         * 是否开启下钻交互
         * 默认值：`true`
         */
        enabled: PropTypes.bool,
        /**
         * 配置下钻层级指示面包屑相关参数
         */
        breadCrumb: PropTypes.exact({
            /**
             * 根节点文案
             */
            rootText: PropTypes.string,
            /**
             * 面包屑分隔符
             * 默认值：`'/'`
             */
            dividerText: PropTypes.string,
            /**
             * 面包屑文字样式
             */
            textStyle: baseStyle,
            /**
             * 面包屑激活状态字体样式
             */
            activeTextStyle: baseStyle,
            /**
             * 面包屑显示位置，可选项有`'top-left'`、`'bottom-left'`
             * 默认值：`'bottom-left'`
             */
            position: PropTypes.oneOf(['top-left', 'bottom-left'])
        })
    }),

    /**
     * 外半径大小，取值应在`0`到`1`之间
     * 默认值：`0.85`
     */
    radius: PropTypes.number,

    /**
     * 内半径大小，取值应在`0`到`1`之间
     * 默认值：`0`
     */
    innerRadius: PropTypes.number,

    /**
     * 控制填充区域颜色，具体见在线文档相关说明
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
     * 控制填充区域样式，具体见在线文档相关说明
     */
    sunburstStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
     * 是否进行径向反转
     * 默认值：`false`
     */
    reflect: PropTypes.bool,

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
        data: PropTypes.any
    }),

    /**
     * 事件监听属性，用于监听最近一次折点点击事件
     */
    recentlyAreaClickRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.any
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

AntdSunburst.defaultProps = {
    locale: 'zh-CN',
    reflect: false,
    downloadTrigger: 'download-trigger'
}

export default AntdSunburst;

export const propTypes = AntdSunburst.propTypes;
export const defaultProps = AntdSunburst.defaultProps;