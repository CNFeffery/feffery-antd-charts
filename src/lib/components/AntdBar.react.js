import { Bar } from '@ant-design/charts';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    scrollbarBasePropTypes,
    baseStyle,
    areaBaseStyle,
    textBaseStyle
} from './BasePropTypes.react';

// 定义条形图组件AntdBar，部分API参数参考https://charts.ant.design/zh-CN/demos/bar
export default class AntdBar extends Component {
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
            groupField,
            isStack,
            isGroup,
            isRange,
            isPercent,
            color,
            intervalPadding,
            dodgePadding,
            minBarWidth,
            maxBarWidth,
            barStyle,
            barBackground,
            barWidthRatio,
            marginRatio,
            scrollbar,
            conversionTag,
            connectedArea,
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
            seriesField: seriesField,
            groupField: groupField,
            isStack: isStack,
            isGroup: isGroup,
            isRange: isRange,
            isPercent: isPercent,
            intervalPadding: intervalPadding,
            dodgePadding: dodgePadding,
            minBarWidth: minBarWidth,
            maxBarWidth: maxBarWidth,
            barBackground: barBackground,
            barWidthRatio: barWidthRatio,
            marginRatio: marginRatio,
            scrollbar: scrollbar,
            connectedArea: connectedArea,
            width: width,
            height: height,
            autoFit: autoFit,
            padding: padding,
            renderer: renderer,
            locale: locale
        };

        // 进阶参数
        if (conversionTag) {
            config.conversionTag = conversionTag

            if (conversionTag?.text?.formatter?.func) {
                config.conversionTag.text.formatter = eval(conversionTag.text.formatter.func)
            }
        } else if (conversionTag === false) {
            config.conversionTag = false
        } else {
            delete config.conversionTag
        }

        if (color) {
            config.color = color?.func ? eval(color?.func) : color
        } else if (color === false) {
            config.color = false
        } else {
            delete config.color
        }

        if (barStyle) {
            config.barStyle = barStyle?.func ? eval(barStyle?.func) : barStyle
        } else if (barStyle === false) {
            config.barStyle = false
        } else {
            delete config.barStyle
        }

        if (xAxis) {
            config.xAxis = xAxis
            if (config.xAxis?.label?.formatter?.func) {
                config.xAxis.label.formatter = eval(xAxis.label.formatter.func)
            }
        } else if (xAxis === false) {
            config.xAxis = false
        } else {
            delete config.xAxis
        }

        if (yAxis) {
            config.yAxis = yAxis
            if (config.yAxis?.label?.formatter?.func) {
                config.yAxis.label.formatter = eval(yAxis.label.formatter.func)
            }
        } else if (yAxis === false) {
            config.yAxis = false
        } else {
            delete config.yAxis
        }

        if (legend) {
            config.legend = legend

            if (legend.itemName) {
                config.legend.itemName.formatter = legend.itemName?.formatter?.func
                    ? eval(legend.itemName.formatter.func) : legend.itemName.formatter
            }

            if (legend.itemValue) {
                config.legend.itemValue.formatter = legend.itemValue?.formatter?.func
                    ? eval(legend.itemValue.formatter.func) : legend.itemValue.formatter
            }
        } else if (legend === false) {
            config.legend = false
        } else {
            delete config.legend
        }

        if (label) {
            config.label = label
            if (label?.formatter?.func) {
                config.label.formatter = eval(label.formatter.func)
            }
        } else if (label === false) {
            config.label = false
        } else {
            delete config.label
        }

        if (tooltip) {
            config.tooltip = tooltip

            if (tooltip?.formatter?.func) {
                config.tooltip.formatter = eval(tooltip.formatter.func)
            }

            if (tooltip?.customItems?.func) {
                config.tooltip.customItems = eval(tooltip.customItems.func)
            }
        } else if (tooltip === false) {
            config.tooltip = false
        } else {
            delete config.tooltip
        }

        if (annotations) {
            config.annotations = annotations
        } else if (annotations === false) {
            config.annotations = false
        } else {
            delete config.annotations
        }

        return <Bar id={id}
            className={className}
            style={style}
            {...config} />;
    }
}

// 定义参数或属性
AntdBar.propTypes = {
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

    // 用于在堆叠分组条形图中指定分组字段，此时seriesField指定的字段会作为每个组内堆叠的分层依据
    groupField: PropTypes.string,

    // 在存在seriesField分组字段时，用于设置是否堆叠条形图
    isStack: PropTypes.bool,

    // 在存在seriesField分组字段时，用于设置是否分组条形图
    isGroup: PropTypes.bool,

    // 在xField的值格式为[number, number]时，用于设置是否区间条形图
    isRange: PropTypes.bool,

    // 在isStack=true时生效，用于设置是否百分比条形图
    isPercent: PropTypes.bool,

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

    // 设置分组条形图组间像素间隔宽度
    intervalPadding: PropTypes.number,

    // 设置分组条形图组内像素间隔宽度
    dodgePadding: PropTypes.number,

    // 设置条形图的最小像素宽度，默认会自适应
    minBarWidth: PropTypes.number,

    // 设置条形图的最大像素宽度，默认会自适应
    maxBarWidth: PropTypes.number,

    // 设置柱体的样式
    barStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 设置柱状图背景样式
    barBackground: PropTypes.exact({
        // 具体样式
        style: areaBaseStyle
    }),

    // 设置条形图宽度占比，0~1之间
    barWidthRatio: PropTypes.number,

    // 设置分组条形图中条形之间的间距，0~1之间
    marginRatio: PropTypes.number,

    // 设置条形图滚动条样式
    scrollbar: scrollbarBasePropTypes,

    // 设置转化标签相关属性
    conversionTag: PropTypes.exact({
        // 设置转化率标签像素尺寸大小
        size: PropTypes.number,

        // 设置转化率标签与柱体之间的像素间距
        spacing: PropTypes.number,

        // 设置组件与坐标轴之间的距离
        offset: PropTypes.number,

        // 配置转化率组件箭头样式，false时不显示箭头
        arrow: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.exact({
                // 设置箭头尺寸
                headSize: PropTypes.number
            })
        ]),

        // 配置转化率组件文本信息，false时不显示文本
        text: PropTypes.oneOfType([
            PropTypes.bool,
            PropTypes.exact({
                // 自定义转化率计算函数
                formatter: PropTypes.exact({
                    // 回调模式
                    func: PropTypes.string
                }),

                // 自定义转化率文字样式
                style: textBaseStyle
            })
        ])
    }),

    // 设置联通对比区域相关参数
    connectedArea: PropTypes.oneOfType([
        PropTypes.exact({
            // 设置触发方式，false表示不触发，可选的有'hover'、'click'
            trigger: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.string
            ])
        }),
        PropTypes.bool
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
AntdBar.defaultProps = {
}