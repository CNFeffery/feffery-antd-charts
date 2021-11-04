import { Area } from '@ant-design/charts';
import React, { Component } from 'react';
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
    sliderBasePropTypes
} from './BasePropTypes.react';

// 定义面积图组件AntdArea，部分API参数参考https://charts.ant.design/zh-CN/demos/area
export default class AntdArea extends Component {
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
            isPercent,
            startOnZero,
            isStack,
            color,
            areaStyle,
            line,
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
            isPercent: isPercent,
            startOnZero: startOnZero,
            isStack: isStack,
            width: width,
            height: height,
            autoFit: autoFit,
            padding: padding,
            renderer: renderer,
            locale: locale
        };


        // 进阶参数
        if (typeof color == "undefined" || JSON.stringify(color) == "{}") {
            config.color = undefined
        } else if (color === false) {
            config.color = false
        } else if (color) {
            config.color = color?.func ? eval(color?.func) : color
        }

        if (typeof areaStyle == "undefined" || JSON.stringify(areaStyle) == "{}") {
            config.areaStyle = undefined
        } else if (areaStyle === false) {
            config.areaStyle = false
        } else if (areaStyle) {
            config.areaStyle = areaStyle?.func ? eval(areaStyle.func) : areaStyle
        }

        if (typeof line == "undefined" || JSON.stringify(line) == "{}") {
            config.line = undefined
        } else if (line === false) {
            config.line = false
        } else if (line) {
            config.line = line
            config.line.color = line?.color?.func ? eval(line.color.func) : line.color
            config.line.style = line?.style?.func ? eval(line.style.func) : line.style
        }


        if (typeof point == "undefined" || JSON.stringify(point) == "{}") {
            config.point = undefined
        } else if (point === false) {
            config.point = false
        } else if (point) {
            config.point = {
                color: point?.color?.func ? eval(point?.color?.func) : point.color,

                shape: point?.shape?.func ? eval(point?.shape?.func) : point.shape,

                style: point?.style?.func ? eval(point?.style?.func) : point.style
            }
        }

        if (typeof xAxis == "undefined" || JSON.stringify(xAxis) == "{}") {
            config.xAxis = undefined
        } else if (xAxis === false) {
            config.xAxis = false
        } else if (xAxis) {
            config.xAxis = xAxis
            if (config.xAxis?.label?.formatter?.func) {
                config.xAxis.label.formatter = eval(xAxis.label.formatter.func)
            }
        }

        if (typeof yAxis == "undefined" || JSON.stringify(yAxis) == "{}") {
            config.yAxis = undefined
        } else if (yAxis === false) {
            config.yAxis = false
        } else if (yAxis) {
            config.yAxis = yAxis
            if (config.yAxis?.label?.formatter?.func) {
                config.yAxis.label.formatter = eval(config.yAxis.label.formatter.func)
            }
        }

        if (typeof legend == "undefined" || JSON.stringify(legend) == "{}") {
            config.legend = undefined
        } else if (legend === false) {
            config.legend = false
        } else if (legend) {
            config.legend = legend

            if (legend.itemName) {
                config.legend.itemName.formatter = legend.itemName?.formatter?.func
                    ? eval(legend.itemName.formatter.func) : legend.itemName.formatter
            }

            if (config.legend.itemValue) {
                config.legend.itemValue.formatter = legend.itemValue?.formatter?.func
                    ? eval(legend.itemValue.formatter.func) : legend.itemValue.formatter
            }
        }

        if (typeof label == "undefined" || JSON.stringify(label) == "{}") {
            config.label = undefined
        } else if (label === false) {
            config.label = false
        } else if (label) {
            config.label = label
            if (label?.formatter?.func) {
                config.label.formatter = eval(label.formatter.func)
            }
        }

        if (typeof tooltip == "undefined" || JSON.stringify(tooltip) == "{}") {
            config.tooltip = undefined
        } else if (tooltip === false) {
            config.tooltip = false
        } else if (tooltip) {
            config.tooltip = tooltip
            if (tooltip?.formatter?.func) {
                config.tooltip.formatter = eval(tooltip.formatter.func)
            }
            if (tooltip?.customItems?.func) {
                config.tooltip.customItems = eval(tooltip.customItems.func)
            }
        }

        if (typeof annotations == "undefined" || JSON.stringify(annotations) == "{}") {
            config.annotations = undefined
        } else if (annotations === false) {
            config.annotations = false
        } else if (annotations) {
            config.annotations = annotations
        }

        if (typeof slider == "undefined" || JSON.stringify(slider) == "{}") {
            config.slider = undefined
        } else if (slider === false) {
            config.slider = false
        } else if (slider) {
            config.slider = slider

            if (slider?.formatter?.func) {
                config.slider.formatter = eval(slider.formatter.func)
            }
        }

        return <Area id={id}
            className={className}
            style={style}
            {...config} />;
    }
}

// 定义参数或属性
AntdArea.propTypes = {
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

    // 设置是否开启百分比面积图，百分比时会自动激活isStack=true
    isPercent: PropTypes.bool,

    // 在存在seriesField分组字段时，用于设置是否将折线堆叠起来，默认为false
    isStack: PropTypes.bool,

    // 设置面积图是否从0基准线开始填充，使用时需要配合isStack=false
    startOnZero: PropTypes.bool,

    // 设置面积图形样式
    areaStyle: PropTypes.oneOfType([
        areaBaseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

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
    line: PropTypes.exact({
        // 设置面积图中折线的样式
        color: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string),
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            })
        ]),

        // 设置面积图中的线样式
        style: PropTypes.oneOfType([
            lineBaseStyle,
            PropTypes.exact({
                // 回调模式
                func: PropTypes.string
            })
        ])
    }),

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
AntdArea.defaultProps = {
}