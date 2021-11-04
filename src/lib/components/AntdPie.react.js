import { Pie } from '@ant-design/charts';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
    metaBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    baseStyle
} from './BasePropTypes.react';

// 定义饼图组件AntdPie，部分API参数参考https://charts.ant.design/zh-CN/demos/pie
export default class AntdPie extends Component {
    render() {
        // 取得必要属性或参数
        let {
            id,
            className,
            style,
            data,
            meta,
            angleField,
            colorField,
            radius,
            innerRadius,
            startAngle,
            endAngle,
            color,
            statistic,
            pieStyle,
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
            angleField: angleField,
            colorField: colorField,
            radius: radius,
            innerRadius: innerRadius,
            startAngle: startAngle,
            endAngle: endAngle,
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

        if (typeof pieStyle == "undefined" || JSON.stringify(pieStyle) == "{}") {
            config.pieStyle = undefined
        } else if (pieStyle === false) {
            config.pieStyle = false
        } else if (pieStyle) {
            config.pieStyle = pieStyle?.func ? eval(pieStyle?.func) : pieStyle
        }

        if (typeof statistic == "undefined" || JSON.stringify(statistic) == "{}") {
            config.statistic = undefined
        } else if (statistic === false) {
            config.statistic = false
        } else if (statistic) {
            config.statistic = statistic

            if (statistic.title) {

                config.statistic.title.formatter = statistic.title?.formatter?.func
                    ? eval(statistic.title.formatter.func) : statistic.title.formatter
            }

            if (statistic.content) {

                config.statistic.content.formatter = statistic.content?.formatter?.func
                    ? eval(statistic.content.formatter.func) : statistic.content.formatter
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

        if (typeof tooltip == "undefined" || JSON.stringify(tooltip) == "{}") {
            config.annotations = undefined
        } else if (annotations === false) {
            config.annotations = false
        } else if (annotations) {
            config.annotations = annotations
        }

        return <Pie id={id}
            className={className}
            style={style}
            {...config} />;
    }
}

// 定义参数或属性
AntdPie.propTypes = {
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

    // 定义扇形切片弧度大小对应的数据字段名
    angleField: PropTypes.string,

    // 定义扇形颜色映射对应的数据字段名
    colorField: PropTypes.string,

    // 设置饼图的半径，原点为画布中心，取值在0~1之间，比如1代表饼图吃呢更慢绘图区域
    radius: PropTypes.number,

    // 设置饼图的内半径，原点为画布中心，取值在0~1之间
    innerRadius: PropTypes.number,

    // 设置饼图起始角度
    startAngle: PropTypes.number,

    // 设置饼图结束角度
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

    // 配置统计内容组件，当innerAngle大于0时生效
    statistic: PropTypes.exact({
        // 配置统计内容标题，设置为false时隐藏标题
        title: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.exact({
                // 配置统计文本的css样式
                style: PropTypes.object,

                // 配置标题文本内容，优先级：customHtml > formatter > content
                content: PropTypes.string,

                // 回调自定义标题文本信息
                formatter: PropTypes.exact({
                    // 回调模式
                    func: PropTypes.string
                }),

                // 设置标题的旋转角度
                rotate: PropTypes.number,

                // 设置标题的水平方向偏移像素值
                offsetX: PropTypes.number,

                // 设置标题的竖直方向偏移像素值
                offsetY: PropTypes.number
            })
        ]),

        // 配置统计内容主体信息，设置为false时隐藏标题
        content: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.exact({
                // 配置统计文本的css样式
                style: PropTypes.object,

                // 配置主体信息文本内容，优先级：customHtml > formatter > content
                content: PropTypes.string,

                // 回调自定义主体信息文本信息
                formatter: PropTypes.exact({
                    // 回调模式
                    func: PropTypes.string
                }),

                // 设置主体信息旋转角度
                rotate: PropTypes.number,

                // 设置主体信息的水平方向偏移像素值
                offsetX: PropTypes.number,

                // 设置主体信息的竖直方向偏移像素值
                offsetY: PropTypes.number
            })
        ]),
    }),

    // 设置扇区的样式，其中fill会覆盖一级color参数信息
    pieStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

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
AntdPie.defaultProps = {
}