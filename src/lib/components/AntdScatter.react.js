import { Scatter } from '@ant-design/charts';
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
    baseStyle,
    textBaseStyle
} from './BasePropTypes.react';

// 定义散点气泡图组件AntdScatter，部分API参数参考https://charts.ant.design/zh-CN/demos/scatter
export default class AntdScatter extends Component {
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
            colorField,
            sizeField,
            shapeField,
            size,
            shape,
            color,
            pointStyle,
            shapeLegend,
            sizeLegend,
            quadrant,
            regressionLine,
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
            colorField: colorField,
            sizeField: sizeField,
            shapeField: shapeField,
            shapeLegend: shapeLegend,
            sizeLegend: sizeLegend,
            quadrant: quadrant,
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

        if (typeof size == "undefined" || JSON.stringify(size) == "{}") {
            config.size = undefined
        } else if (size === false) {
            config.size = false
        } else if (size) {
            config.size = size?.func ? eval(size?.func) : size
        }

        if (typeof shape == "undefined" || JSON.stringify(shape) == "{}") {
            config.shape = undefined
        } else if (shape === false) {
            config.shape = false
        } else if (shape) {
            config.shape = shape?.func ? eval(shape?.func) : shape
        }

        if (typeof pointStyle == "undefined" || JSON.stringify(pointStyle) == "{}") {
            config.pointStyle = undefined
        } else if (pointStyle === false) {
            config.pointStyle = false
        } else if (pointStyle) {
            config.pointStyle = pointStyle?.func ? eval(pointStyle?.func) : pointStyle
        }

        if (typeof xAxis == "undefined" || JSON.stringify(xAxis) == "{}") {
            config.xAxis = undefined
        } else if (xAxis === false) {
            config.xAxis = false
        } else if (xAxis) {
            config.xAxis = xAxis
            if (xAxis?.label?.formatter?.func) {
                config.xAxis.label.formatter = eval(xAxis.label.formatter.func)
            }
        }

        if (typeof yAxis == "undefined" || JSON.stringify(yAxis) == "{}") {
            config.yAxis = undefined
        } else if (yAxis === false) {
            config.yAxis = false
        } else if (yAxis) {
            config.yAxis = yAxis
            if (yAxis?.label?.formatter?.func) {
                config.yAxis.label.formatter = eval(yAxis.label.formatter.func)
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

            if (legend.itemValue) {
                config.legend.itemValue.formatter = legend.itemValue?.formatter?.func
                    ? eval(legend.itemValue.formatter.func) : legend.itemValue.formatter
            }
        }

        if (typeof label == "undefined") {
            config.label = undefined
        } else if (JSON.stringify(label) == "{}") {
            config.label = {}
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
        } else if (tooltip) {
            config.annotations = annotations
        }

        if (typeof regressionLine == "undefined" || JSON.stringify(regressionLine) == "{}") {
            config.regressionLine = undefined
        } else if (regressionLine === false) {
            config.regressionLine = false
        } else if (regressionLine) {
            config.regressionLine = regressionLine

            config.regressionLine.algorithm = regressionLine?.algorithm?.func
                ? eval(regressionLine.algorithm.func) : regressionLine.algorithm
        }

        return <Scatter id={id}
            className={className}
            style={style}
            {...config} />;
    }
}

// 定义参数或属性
AntdScatter.propTypes = {
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

    // 定义作为色彩映射依据的字段
    colorField: PropTypes.string,

    // 定义作为尺寸映射依据的字段
    sizeField: PropTypes.string,

    // 定义作为形状映射依据的字段
    shapeField: PropTypes.string,

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

    // 用于设置散点像素尺寸大小
    size: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 用于设置形状相关参数
    shape: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 设置散点样式
    pointStyle: PropTypes.oneOfType([
        pointBaseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 当shapeField已设置时，且legend、shapeLegend均不为false时，则会渲染针对shape的图例
    shapeLegend: legendBasePropTypes,

    // 设置后会渲染散点尺寸相关的图例
    sizeLegend: legendBasePropTypes,

    // 设置四象限图组件相关参数
    quadrant: PropTypes.exact({
        // 设置x轴上的基准分割线位置，默认为0
        xBaseline: PropTypes.number,

        // 设置y轴上的基准分割线位置，默认为0
        yBaseline: PropTypes.number,

        // 配置分割线样式
        lineStyle: lineBaseStyle,

        // 配置四个象限的样式，单对象输入时全局设置，
        // 亦可按照上右下左的顺序分别传入四个对象构成的数组来分别设置四个象限的样式
        regionStyle: PropTypes.oneOfType([
            baseStyle,
            PropTypes.arrayOf(baseStyle)
        ]),

        // 分别设置四个象限的文字标注信息及其样式
        labels: PropTypes.arrayOf(
            PropTypes.exact({
                // 设置标注内容
                content: PropTypes.string,

                // 设置标注坐标位置，格式：[x坐标, y坐标]
                position: PropTypes.arrayOf(PropTypes.number),

                // 设置标注文字样式
                style: textBaseStyle
            })
        )
    }),

    // 设置回归线相关参数
    regressionLine: PropTypes.exact({
        // 设置回归线类型，可选的有'exp'、'linear'、'loess'、'log'、'poly'、'pow'、'quad'
        type: PropTypes.oneOf(['exp', 'linear', 'loess', 'log', 'poly', 'pow', 'quad']),

        // 设置回归线样式
        style: lineBaseStyle,

        // 自定义映射算法，优先级高于type
        algorithm: PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        }),

        // 设置是否置于图层顶层显示
        top: PropTypes.bool
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
AntdScatter.defaultProps = {
}