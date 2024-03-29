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

const AntdSunburst = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdSunburst {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdSunburst.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 定义绘图所需数据，必须参数
    data: PropTypes.object.isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 定义色彩区分所依据的字段，默认为祖先节点的name字段
    colorField: PropTypes.string,

    // 定义额外的原始字段名数组，可在tooltip等回调函数中用于取得辅助用数据
    rawFields: PropTypes.arrayOf(PropTypes.string),

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

    // 图形样式类参数

    // 层级布局配置参数
    hierarchyConfig: PropTypes.exact({
        // 数据节点权重映射字段，默认为'value'
        field: PropTypes.string,

        // 设置是否忽略父节点实际权重，默认为true
        ignoreParentValue: PropTypes.bool
    }),

    // 配置下钻相关参数
    drilldown: PropTypes.exact({
        // 设置是否允许下钻交互，默认为true
        enabled: PropTypes.bool,

        // 配置层级面包屑相关参数
        breadCrumb: PropTypes.exact({
            // 设置根节点文案，默认：'Root'，中文默认：'根节点'
            rootText: PropTypes.string,

            // 设置面包屑分割文字，默认为'/'
            dividerText: PropTypes.string,

            // 设置面包屑字体样式
            textStyle: baseStyle,

            // 设置激活状态下的字体样式
            activeTextStyle: baseStyle,

            // 设置下钻层级面包屑的方位，可选的有'top-left'、'bottom-left'
            // 默认为'top-left'
            position: PropTypes.oneOf(['top-left', 'bottom-left'])
        })
    }),

    // 设置半径比例，取值应在0到1之间，默认为0.85
    radius: PropTypes.number,

    // 设置内径比例，取值应在0到1之间，默认为0
    innerRadius: PropTypes.number,

    // 用于手动设置调色方案，接受css中合法的所有颜色值，当传入单个字符串时，所有折线沿用此颜色值
    // 当传入数组时，会视作调色盘方案对seriesField区分的不同系列进行着色
    // 当传入对象时，会解析出其'func'属性对应的字符串，解析为函数，以支持更为自由的seriesField->色彩映射
    color: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            // 传入字符串形式的js函数体源码，例如
            // (ref) => {
            //     if (ref.series === '系列一'){
            //         return 'red'
            //     }
            //     return 'blue'
            // }
            func: PropTypes.string
        })
    ]),

    // // 设置图形的贴图样式
    // pattern: PropTypes.object,

    // 设置填充区域样式，其中透明度默认随着层级增加会逐渐减少填充透明度，可通过sunburstStyle
    // 自定义func回调来自主控制样式
    sunburstStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 设置是否进行径向反转，默认为false，当设置为true后旭日图将会以从外向内的方式进行层次的递进
    reflect: PropTypes.bool,

    // 配置文字标签相关参数
    label: labelBasePropTypes,

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

    // 配置标注相关参数
    annotations: annotationsBasePropTypes,

    // 配置动画相关参数
    animation: animationBasePropTypes,

    // 常用事件监听参数
    // tooltip显示事件
    recentlyTooltipChangeRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.any
    }),

    // 单独折线点击事件
    recentlyAreaClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.any
    }),

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

    /**
     * 配置图形填充贴图样式
     */
    pattern: patternBasePropTypes,

    /**
     * 交互功能项配置
     */
    interactions: interactionsBasePropTypes,

    /**
     * 状态样式配置
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

// 设置默认参数
AntdSunburst.defaultProps = {
    locale: 'zh-CN',
    reflect: false,
    downloadTrigger: 'download-trigger'
}

export default AntdSunburst;

export const propTypes = AntdSunburst.propTypes;
export const defaultProps = AntdSunburst.defaultProps;