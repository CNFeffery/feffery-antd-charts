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
    areaBaseStyle,
    labelBasePropTypes,
    tooltipBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    themeBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes
} from './BasePropTypes.react';

const LazyAntdBullet = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdBullet.react'));

const AntdBullet = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdBullet {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdBullet.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置子弹图绘图所需数据
    // 格式如：[{title: '满意度', ranges: [50,100], measures: [80], target: 85}]
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 设置作为子弹图长度的字段
    measureField: PropTypes.string.isRequired,

    // 设置作为子弹图背景色条长度的字段
    rangeField: PropTypes.string.isRequired,

    // 设置作为子弹图目标值位置的字段
    targetField: PropTypes.string.isRequired,

    // 用于设置分组依据字段
    xField: PropTypes.string,

    // 设置x坐标轴相关属性
    xAxis: axisBasePropTypes,

    // 设置y坐标轴相关属性
    yAxis: axisBasePropTypes,

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

    // 设置子弹图方向，可选的有'horizontal'、'vertical'
    // 默认为'horizontal'
    layout: PropTypes.oneOf(['horizontal', 'vertical']),

    // 配置子弹图各图形色彩
    color: PropTypes.exact({
        // 区间背景颜色
        range: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        // 实际值颜色
        measure: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        // 目标值颜色
        target: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ])
    }),

    // 设置子弹图各图形尺寸
    size: PropTypes.exact({
        // 区间背景像素尺寸，默认为30
        range: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number),
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ]),
        // 实际值像素尺寸，默认值为20
        measure: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number),
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ]),
        // 目标值像素尺寸，默认为20
        target: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number),
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ])
    }),

    // 配置子弹图各图形样式
    bulletStyle: PropTypes.exact({
        // 区间背景样式，默认为{ fillOpacity: 0.5 }
        range: PropTypes.oneOfType([
            areaBaseStyle,
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ]),
        // 实际值样式
        measure: PropTypes.oneOfType([
            areaBaseStyle,
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ]),
        // 目标值样式
        target: PropTypes.oneOfType([
            areaBaseStyle,
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ])
    }),

    // 配置子弹图各图形文本标签
    label: PropTypes.exact({
        // 区间文本标签
        range: labelBasePropTypes,
        // 实际值文本标签
        measure: labelBasePropTypes,
        // 目标值文本标签
        target: labelBasePropTypes
    }),

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

    // 配置图例相关参数
    legend: legendBasePropTypes,

    // 配置动画相关参数
    animation: animationBasePropTypes,

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

    /**
     * 交互功能项配置
     */
    interactions: interactionsBasePropTypes,

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
AntdBullet.defaultProps = {
    locale: 'zh-CN',
    layout: 'horizontal',
    downloadTrigger: 'download-trigger'
}

export default AntdBullet;

export const propTypes = AntdBullet.propTypes;
export const defaultProps = AntdBullet.defaultProps;