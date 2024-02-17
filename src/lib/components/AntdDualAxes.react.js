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

const AntdDualAxes = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdDualAxes {...props} />
        </Suspense>
    );
}

// 定义参数或属性
AntdDualAxes.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 定义绘图所需数据，必须参数
    data: PropTypes.arrayOf(PropTypes.arrayOf(PropTypes.object)).isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 定义作为x轴的字段名
    xField: PropTypes.string.isRequired,

    // 定义作为y轴的字段名
    yField: PropTypes.arrayOf(PropTypes.string).isRequired,

    // 分别配置双轴对应左右轴的图形相关参数，格式为
    // [左轴图形配置, 右轴图形配置]，每个配置对应Line或Column类型
    geometryOptions: PropTypes.arrayOf(
        PropTypes.oneOfType([
            // 折线图专用参数
            PropTypes.exact({
                // 设置当前对应轴的图表类型，可选的有'line'、'column'
                geometry: PropTypes.oneOf(['line', 'column']),
                // 设置作为分组依据的字段名
                seriesField: PropTypes.string,
                // 设置是否以平滑曲线方式渲染折线，默认为false
                smooth: PropTypes.bool,
                // 设置针对折线图中缺失值的绘制策略，true表示连接，false表示断开，默认为true
                connectNulls: PropTypes.bool,
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
                    baseStyle,
                    PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string,
                    }),
                ]),
                // 用于设置折线图折点的样式
                point: PropTypes.exact({
                    // 设置折点颜色，支持单字符串、字符串数组以及对象传入func定义js函数体，函数格式同lineStyle
                    color: PropTypes.oneOfType([
                        PropTypes.string,
                        PropTypes.arrayOf(PropTypes.string),
                        PropTypes.exact({
                            func: PropTypes.string,
                        }),
                    ]),
                    // 设置折点形状，支持单字符串或对象传入func定义js函数体，函数格式同lineStyle
                    // 单字符时可选的样式有'circle'、'square'、'line'、'diamond'、'triangle'、'triangle-down'、'hexagon'、
                    // 'bowtie'、'cross'、'tick'、'plus'及'hyphen'
                    shape: PropTypes.oneOfType([
                        PropTypes.string,
                        PropTypes.exact({
                            func: PropTypes.string,
                        }),
                    ]),
                    // 设置折点通用style属性，支持对象传入，当对象中具有func属性时，会视作func回调模式处理
                    style: PropTypes.oneOfType([
                        baseStyle,
                        PropTypes.exact({
                            // 回调模式
                            func: PropTypes.string,
                        }),
                    ]),
                }),
                // 配置文字标签相关参数
                label: labelBasePropTypes,
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
                        func: PropTypes.string,
                    }),
                ]),
            }),
            // 柱状图专用参数
            PropTypes.exact({
                // 设置当前对应轴的图表类型，可选的有'line'、'column'
                geometry: PropTypes.oneOf(['line', 'column']),
                // 设置作为分组依据的字段名
                seriesField: PropTypes.string,
                // 用于在堆叠分组柱状图中指定分组字段，此时seriesField指定的字段会作为每个组内堆叠的分层依据
                groupField: PropTypes.string,
                // 在存在seriesField分组字段时，用于设置是否分组条形图
                isGroup: PropTypes.bool,
                // 在存在seriesField分组字段时，用于设置是否堆叠条形图
                isStack: PropTypes.bool,
                // 设置柱状图宽度占比，0~1之间
                columnWidthRatio: PropTypes.number,
                // 设置分组柱状图中条形之间的间距，0~1之间
                marginRatio: PropTypes.number,
                // 设置柱体的样式
                columnStyle: PropTypes.oneOfType([
                    baseStyle,
                    PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string,
                    }),
                ]),
                // 配置文字标签相关参数
                label: labelBasePropTypes,
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
                        func: PropTypes.string,
                    }),
                ]),
            }),
        ])
    ),

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
        PropTypes.oneOf(['auto']),
    ]),

    // 定义在padding基础上额外的像素填充间距
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
    ]),

    // 设置图表渲染方式为'canvas'或'svg'模式，默认为'canvas'
    renderer: PropTypes.oneOf(['canvas', 'svg']),

    // 设置语言，可选的有'zh-CN'与'en-US'
    locale: PropTypes.oneOf(['zh-CN', 'en-US']),

    // 设置是否对超出绘图区域的几何元素进行裁剪
    limitInPlot: PropTypes.bool,

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

    // 设置x坐标轴相关属性
    xAxis: axisBasePropTypes,

    // 设置y坐标轴相关属性
    yAxis: PropTypes.objectOf(axisBasePropTypes),

    // 配置标注相关参数
    annotations: PropTypes.objectOf(annotationsBasePropTypes),

    // 配置图例相关参数
    legend: legendBasePropTypes,

    // 配置缩略轴相关参数
    slider: sliderBasePropTypes,

    // 配置动画相关参数
    animation: animationBasePropTypes,

    // 数据项点击事件
    recentlyClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.object,
    }),

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

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
        component_name: PropTypes.string,
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

// 设置默认参数
AntdDualAxes.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger',
};

export default AntdDualAxes;

export const propTypes = AntdDualAxes.propTypes;
export const defaultProps = AntdDualAxes.defaultProps;