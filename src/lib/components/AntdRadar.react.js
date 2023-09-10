/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    pointBaseStyle,
    lineBaseStyle,
    areaBaseStyle,
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    themeBasePropTypes
} from './BasePropTypes.react';

const LazyAntdRadar = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdRadar.react'));

const AntdRadar = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdRadar {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdRadar.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 定义绘图所需数据，必须参数
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 定义作为角度的字段名
    xField: PropTypes.string.isRequired,

    // 定义作为半径的字段名
    yField: PropTypes.string.isRequired,

    // 定义作为分组依据的字段名，不同的组会通过颜色进行区分并上下重叠
    seriesField: PropTypes.string,

    // 设置是否以平滑曲线方式渲染弧线，默认为false
    smooth: PropTypes.bool,

    // 设置雷达图的半径，原点为绘图区域中心，取值在0~1之间，1代表撑满绘图区域
    radius: PropTypes.number,

    // 设置起始角度，弧度制，默认为0
    startAngle: PropTypes.number,

    // 设置结束角度，弧度制，默认为pi
    endAngle: PropTypes.number,

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


    // 用于设置折线样式，常规方式下接受对象用于设置全局折线样式
    // 亦可传入字符串对应的js函数体，实现针对不同seriesField返回不同样式，例如
    // (ref) => {
    //     if (ref.seriesField === 'a'){
    //         return {
    //             lineDash: [4, 4],
    //             opacity: 1,
    //           };
    //     }
    //     return { opacity: 0.5 };
    // }
    lineStyle: PropTypes.oneOfType([
        lineBaseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 用于设置面积图折线折点的样式
    point: PropTypes.exact({
        // 设置折点颜色，支持单字符串、字符串数组以及对象传入func定义js函数体，函数格式同lineStyle
        color: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string),
            PropTypes.exact({
                func: PropTypes.string
            })
        ]),

        // 设置折点形状，支持单字符串或对象传入func定义js函数体，函数格式同lineStyle
        // 单字符时可选的样式有'circle'、'square'、'line'、'diamond'、'triangle'、'triangle-down'、'hexagon'、
        // 'bowtie'、'cross'、'tick'、'plus'及'hyphen'
        shape: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.exact({
                func: PropTypes.string
            })
        ]),

        // 设置折点通用style属性，支持对象传入，当对象中具有func属性时，会视作func回调模式处理
        style: PropTypes.oneOfType([
            pointBaseStyle,
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            })
        ])
    }),

    // 配置雷达图上的面积填充相关样式，可回调
    area: PropTypes.exact({
        // 配置是否平滑折线
        smooth: PropTypes.bool,

        // 配置填充面积颜色
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

        // 配置填充面积详细样式
        style: PropTypes.oneOfType([
            areaBaseStyle,
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            })
        ])
    }),

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
        PropTypes.string
    ]),

    // 定义在padding基础上额外的像素填充间距
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.string
    ]),

    // 设置图表渲染方式为'canvas'或'svg'模式，默认为'canvas'
    renderer: PropTypes.string,

    // 设置语言，可选的有'zh-CN'与'en-US'
    locale: PropTypes.string,

    // 设置是否对超出绘图区域的几何元素进行裁剪
    limitInPlot: PropTypes.bool,

    // 配置图例相关参数
    legend: legendBasePropTypes,

    // 配置文字标签相关参数
    label: labelBasePropTypes,

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

    // 配置标注相关参数
    annotations: annotationsBasePropTypes,

    // 配置动画相关参数
    animation: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.bool
    ]),

    // 常用事件监听参数
    // tooltip显示事件
    recentlyTooltipChangeRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.arrayOf(PropTypes.object)
    }),

    // 单独area点击事件
    recentlyAreaClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.any
    }),

    // 监听图例事件
    recentlyLegendInfo: PropTypes.exact({
        // 记录当前点击的图例项内容
        triggerItemName: PropTypes.any,
        // 记录当前各图例项信息
        items: PropTypes.arrayOf(
            PropTypes.object
        )
    }),

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
AntdRadar.defaultProps = {
    downloadTrigger: 'download-trigger'
}

export default AntdRadar;

export const propTypes = AntdRadar.propTypes;
export const defaultProps = AntdRadar.defaultProps;