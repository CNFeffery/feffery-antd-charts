import { Line } from '@ant-design/charts';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
    pointBaseStyle,
    lineBaseStyle,
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    sliderBasePropTypes
} from './BasePropTypes.react';

// 定义折线图组件AntdLine，部分API参数参考https://charts.ant.design/zh-CN/demos/line
export default class AntdLine extends Component {
    render() {
        // 取得必要属性或参数
        let {
            id,
            className,
            style,
            data,
            meta,
            xField,
            yField,
            seriesField,
            smooth,
            stepType,
            connectNulls,
            isStack,
            color,
            lineStyle,
            point,
            xAxis,
            yAxis,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            legend,
            label,
            tooltip,
            annotations,
            slider,
            setProps
        } = this.props;

        // 预处理元信息
        if (meta) {
            for (let i in Object.keys(meta)) {

                if (meta[Object.keys(meta)[i]].formatter) {
                    meta[Object.keys(meta)[i]].formatter = meta[Object.keys(meta)[i]]?.formatter?.func
                        ? eval(meta[Object.keys(meta)[i]]?.formatter?.func) : meta[Object.keys(meta)[i]]?.formatter
                }
            }
        }


        let config = {
            data: data,
            meta: meta,
            padding: padding,
            appendPadding: appendPadding,
            xField: xField,
            yField: yField,
            seriesField: seriesField,
            smooth: smooth,
            stepType: stepType,
            connectNulls: connectNulls,
            isStack: isStack,
            width: width,
            height: height,
            autoFit: autoFit,
            padding: padding,
            renderer: renderer,
            locale: locale
        };

        // 进阶参数
        if (color) {
            config.color = color?.func ? eval(color?.func) : color
        }

        if (lineStyle) {
            config.lineStyle = lineStyle?.func ? eval(lineStyle?.func) : lineStyle
        }

        if (point) {
            config.point = {
                color: point?.color?.func ? eval(point?.color?.func) : point?.color,

                shape: point?.shape?.func ? eval(point?.shape?.func) : point?.shape,

                style: point?.style?.func ? eval(point?.style?.func) : point?.style
            }
        }

        if (xAxis) {
            config.xAxis = xAxis
            if (config.xAxis?.label?.formatter?.func) {
                config.xAxis.label.formatter = eval(config.xAxis.label.formatter.func)
            }
        }

        if (yAxis) {
            config.yAxis = yAxis
            if (config.yAxis?.label?.formatter?.func) {
                config.yAxis.label.formatter = eval(config.yAxis.label.formatter.func)
            }
        }

        if (legend) {
            config.legend = legend

            if (config.legend.itemName) {
                config.legend.itemName.formatter = config.legend.itemName?.formatter?.func
                    ? eval(config.legend.itemName.formatter.func) : config.legend.itemName.formatter
            }

            if (config.legend.itemValue) {
                config.legend.itemValue.formatter = config.legend.itemValue?.formatter?.func
                    ? eval(config.legend.itemValue.formatter.func) : config.legend.itemValue.formatter
            }
        }

        if (label) {
            config.label = label
            if (config.label?.formatter?.func) {
                config.label.formatter = eval(config.label.formatter.func)
            }
        }

        if (tooltip) {
            config.tooltip = tooltip

            if (config.tooltip?.formatter?.func) {
                config.tooltip.formatter = eval(config.tooltip.formatter.func)
            }

            if (config.tooltip?.customItems?.func) {
                config.tooltip.customItems = eval(config.tooltip.customItems.func)
            }
        }

        if (annotations) {
            config.annotations = annotations
        }

        if (slider) {
            config.slider = slider

            if (config.slider?.formatter?.func) {
                config.slider.formatter = eval(config.slider.formatter.func)
            }
        }

        return <Line id={id}
            className={className}
            style={style}
            {...config} />;
    }
}

// 定义参数或属性
AntdLine.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 定义绘图所需数据，必须参数
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 定义作为x轴的字段名
    xField: PropTypes.string.isRequired,

    // 定义作为y轴的字段名
    yField: PropTypes.string.isRequired,

    // 定义作为分组依据的字段名
    seriesField: PropTypes.string,

    // 设置是否以平滑曲线方式渲染折线，默认为false
    smooth: PropTypes.bool,

    // 对应阶梯折线图类型的阶梯曲折方式，可选的有'hv'、'vh'、'hvh'及'vhv'
    // 其中'h'表示horizontal，'v'表示vertical，譬如`vh`就代表先竖直方向再水平方向
    stepType: PropTypes.string,

    // 设置针对折线图中缺失值的绘制策略，true表示连接，false表示断开，默认为true
    connectNulls: PropTypes.bool,

    // 在存在seriesField分组字段时，用于设置是否将折线堆叠起来，默认为false
    isStack: PropTypes.bool,

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


    // 用于设置折线图折点的样式
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

    // 配置图例相关参数
    legend: legendBasePropTypes,

    // 配置文字标签相关参数
    label: labelBasePropTypes,

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

    // 配置标注相关参数
    annotations: annotationsBasePropTypes,

    // 配置缩略轴相关参数
    slider: sliderBasePropTypes,

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
AntdLine.defaultProps = {
}