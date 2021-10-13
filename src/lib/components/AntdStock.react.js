import { Stock } from '@ant-design/charts';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    sliderBasePropTypes,
    baseStyle
} from './BasePropTypes.react';

// 定义股票图组件AntdStock，部分API参数参考https://charts.ant.design/demos/stock/
export default class AntdStock extends Component {
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
            risingFill,
            fallingFill,
            stockStyle,
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
            risingFill: risingFill,
            fallingFill: fallingFill,
            width: width,
            height: height,
            autoFit: autoFit,
            padding: padding,
            renderer: renderer,
            locale: locale
        };

        // 进阶参数
        if (stockStyle) {
            config.stockStyle = stockStyle?.func ? eval(stockStyle?.func) : stockStyle
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

        if (annotations) {
            config.annotations = annotations
        }

        if (slider) {
            config.slider = slider

            if (config.slider?.formatter?.func) {
                config.slider.formatter = eval(config.slider.formatter.func)
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

            tooltip.crosshairs = {
                line: {
                    style: {
                        lineWidth: 0.5,
                        stroke: 'rgba(0,0,0,0.25)',
                    },
                },
                text: function text(type, defaultContent, items) {
                    var textContent;
                    if (type === 'x') {
                        var item = items[0];
                        textContent = item ? item.title : defaultContent;
                    } else {
                        textContent = ''.concat(defaultContent.toFixed(2));
                    }
                    return {
                        position: type === 'y' ? 'start' : 'end',
                        content: textContent,
                        style: { fill: '#dfdfdf' },
                    };
                },
                textBackground: {
                    padding: [4, 8],
                    style: { fill: '#363636' },
                },
            }
        } else {
            config.tooltip = {
                crosshairs: {
                    line: {
                        style: {
                            lineWidth: 0.5,
                            stroke: 'rgba(0,0,0,0.25)',
                        },
                    },
                    text: function text(type, defaultContent, items) {
                        var textContent;
                        if (type === 'x') {
                            var item = items[0];
                            textContent = item ? item.title : defaultContent;
                        } else {
                            textContent = ''.concat(defaultContent.toFixed(2));
                        }
                        return {
                            position: type === 'y' ? 'start' : 'end',
                            content: textContent,
                            style: { fill: '#dfdfdf' },
                        };
                    },
                    textBackground: {
                        padding: [4, 8],
                        style: { fill: '#363636' },
                    },
                }
            }
        }

        return <Stock id={id}
            className={className}
            style={style}
            {...config} />;

    }
}

// 定义参数或属性
AntdStock.propTypes = {
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

    // 定义作为y轴的字段名，格式为对应[开盘价字段, 收盘价字段, 最高价字段, 最低价字段]
    yField: PropTypes.arrayOf(PropTypes.string).isRequired,

    // 配置股票图上涨状态颜色，默认为#ef5350
    risingFill: PropTypes.string,

    // 配置股票图下跌状态颜色，默认为#26a69a
    fallingFill: PropTypes.string,

    // 用于设置股票图图形样式
    stockStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

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
AntdStock.defaultProps = {
    risingFill: '#ef5350',
    fallingFill: '#26a69a'
}