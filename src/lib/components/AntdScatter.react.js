/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import { Scatter } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
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
    textBaseStyle,
    themeBasePropTypes
} from './BasePropTypes.react';
import { difference } from './utils';

// 定义不触发重绘的参数数组
const preventUpdateProps = ['loading_state'];

// 定义散点气泡图组件AntdScatter，部分API参数参考https://charts.ant.design/zh-CN/demos/scatter
export default class AntdScatter extends Component {

    constructor(props) {
        super(props);
        this.chartRef = React.createRef();
    }

    shouldComponentUpdate(nextProps) {

        // 计算发生变化的参数名
        const changedProps = Object.keys(difference(this.props, nextProps))

        // 若无变化的props，则不触发重绘
        if (changedProps.length === 0) {
            return false;
        }

        // 计算发生变化的参数名与需要阻止重绘的参数名数组的交集
        let changedPreventUpdateProps = intersection(
            changedProps,
            preventUpdateProps
        )

        // 若有交集，则不触发重绘
        if (changedPreventUpdateProps.length !== 0) {
            return false;
        } else {
            // 取得plot实例
            const chart = this.chartRef.current.getChart()
            // 检查是否仅有data参数发生更新
            if (changedProps.indexOf('data') !== -1 && changedProps.length === 1) {
                // 动态调整数据
                chart.changeData(nextProps.data)
                return false;
            }
            // 检查是否仅有downloadTrigger参数发生更新
            if (changedProps.indexOf('downloadTrigger') !== -1 && changedProps.length === 1) {
                // 导出当前图表为png格式文件
                chart.downloadImage()
                return false;
            }
        }
        return true;
    }

    render() {
        // 取得必要属性或参数
        const {
            id,
            key,
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
            theme,
            setProps,
            loading_state
        } = this.props;

        // 初始化config参数对象，每次渲染前的参数解析变动只在config中生效
        let config = {};

        // 预处理元信息
        if (meta) {
            config.meta = cloneDeep(meta);
            for (let i in Object.keys(meta)) {
                // 若meta中当前字段属性下的formatter具有自定义函数func属性
                if (meta[Object.keys(meta)[i]]?.formatter?.func) {
                    config.meta[Object.keys(meta)[i]].formatter = eval(meta[Object.keys(meta)[i]].formatter.func)
                }
            }
        }


        // 刷新基础参数
        config = {
            ...config,
            data,
            meta,
            padding,
            appendPadding,
            xField,
            yField,
            colorField,
            sizeField,
            shapeField,
            shapeLegend,
            sizeLegend,
            quadrant,
            width,
            height,
            autoFit,
            renderer,
            theme,
            locale
        };

        // 进阶参数
        // 色彩样式
        config.color = cloneDeep(color)
        // 若color具有自定义函数func属性
        if (color?.func) {
            config.color = eval(color.func)
        }

        config.size = cloneDeep(size)
        // 若size具有自定义函数func属性
        if (size?.func) {
            config.size = eval(size.func)
        }

        config.shape = cloneDeep(shape)
        // 若shape具有自定义函数func属性
        if (shape?.func) {
            config.shape = eval(shape.func)
        }

        config.pointStyle = cloneDeep(pointStyle)
        // 若pointStyle具有自定义函数func属性
        if (pointStyle?.func) {
            config.pointStyle = eval(pointStyle.func)
        }

        // x轴样式
        config.xAxis = cloneDeep(xAxis)
        // 若xAxis.label.formatter具有自定义函数func属性
        if (xAxis?.label?.formatter?.func) {
            config.xAxis.label.formatter = eval(xAxis.label.formatter.func)
        }

        // y轴样式
        config.yAxis = cloneDeep(yAxis)
        // 若yAxis.label.formatter具有自定义函数func属性
        if (yAxis?.label?.formatter?.func) {
            config.yAxis.label.formatter = eval(yAxis.label.formatter.func)
        }


        // 图例样式
        config.legend = cloneDeep(legend)
        // 若legend.itemName.formatter具有自定义函数func属性
        if (legend?.itemName?.formatter?.func) {
            config.legend.itemName.formatter = eval(legend.itemName.formatter.func)
        }
        // 若legend.itemValue.formatter具有自定义函数func属性
        if (legend?.itemValue?.formatter?.func) {
            config.legend.itemValue.formatter = eval(legend.itemValue.formatter.func)
        }

        // 数据标签
        config.label = cloneDeep(label)
        // 若label.formatter具有自定义函数func属性
        if (label?.formatter?.func) {
            config.label.formatter = eval(label.formatter.func)
        }

        // 悬浮提示
        config.tooltip = cloneDeep(tooltip)
        // 若tooltip.formatter具有自定义函数func属性
        if (tooltip?.formatter?.func) {
            config.tooltip.formatter = eval(tooltip.formatter.func)
        }
        // 若tooltip.customItems具有自定义函数func属性
        if (tooltip?.customItems?.func) {
            config.tooltip.customItems = eval(tooltip.customItems.func)
        }

        // 标注
        config.annotations = cloneDeep(annotations)

        // 回归拟合线
        config.regressionLine = cloneDeep(regressionLine)
        // 若regressionLine.algorithm具有自定义函数func属性
        if (regressionLine?.algorithm?.func) {
            config.regressionLine.algorithm = eval(regressionLine.algorithm.func)
        }

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Scatter id={id}
            key={key}
            className={className}
            style={style}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
            ref={this.chartRef}
            {...config} />;
    }
}

// 定义参数或属性
AntdScatter.propTypes = {
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

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

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
    downloadTrigger: 'download-trigger'
}