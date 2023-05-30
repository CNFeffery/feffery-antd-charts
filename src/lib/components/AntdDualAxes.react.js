/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import { DualAxes } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import {
    baseStyle,
    pointBaseStyle,
    lineBaseStyle,
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    themeBasePropTypes
} from './BasePropTypes.react';
import { difference } from './utils';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state'
];

// 定义双轴图组件AntdDualAxes，部分API参数参考https://charts.ant.design/zh/examples/dual-axes/dual-line#dual-line
export default class AntdDualAxes extends Component {

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
        let {
            id,
            key,
            className,
            style,
            data,
            meta,
            xField,
            yField,
            geometryOptions,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            limitInPlot,
            tooltip,
            xAxis,
            yAxis,
            annotations,
            legend,
            animation,
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
            xField,
            yField,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            limitInPlot,
            theme
        };

        // 初始化左右轴config参数对象，每次渲染前的参数解析变动只在config中生效
        let configLeft = {};
        let configRight = {};
        // 进阶参数
        if (geometryOptions[0].geometry === 'line') {
            configLeft = cloneDeep(geometryOptions[0])
            // 折线样式
            // 若lineStyle具有自定义函数func属性
            if (configLeft.lineStyle?.func) {
                configLeft.lineStyle = eval(configLeft.lineStyle.func)
            }

            // 折点样式
            // 若point.color具有自定义函数func属性
            if (configLeft.point?.color?.func) {
                configLeft.point.color = eval(configLeft.point.color.func)
            }
            // 若point.shape具有自定义函数func属性
            if (configLeft.point?.shape?.func) {
                configLeft.point.shape = eval(configLeft.point.shape.func)
            }
            // 若point.style具有自定义函数func属性
            if (configLeft.point?.style?.func) {
                configLeft.point.style = eval(configLeft.point.style.func)
            }

            // 数据标签
            // 若label.formatter具有自定义函数func属性
            if (configLeft.label?.formatter?.func) {
                configLeft.label.formatter = eval(configLeft.label.formatter.func)
            }

            // 色彩样式
            // 若color具有自定义函数func属性
            if (configLeft.color?.func) {
                configLeft.color = eval(configLeft.color.func)
            }
        } else {
            configLeft = cloneDeep(geometryOptions[0])
            // 若columnStyle具有自定义函数func属性
            if (configLeft.columnStyle?.func) {
                configLeft.columnStyle = eval(configLeft.columnStyle.func)
            }

            // 若label.formatter具有自定义函数func属性
            if (configLeft.label?.formatter?.func) {
                configLeft.label.formatter = eval(configLeft.label.formatter.func)
            }

            // 若color具有自定义函数func属性
            if (configLeft.color?.func) {
                configLeft.color = eval(configLeft.color.func)
            }
        }

        if (geometryOptions[1].geometry === 'line') {
            configRight = cloneDeep(geometryOptions[1])
            // 折线样式
            // 若lineStyle具有自定义函数func属性
            if (configRight.lineStyle?.func) {
                configRight.lineStyle = eval(configRight.lineStyle.func)
            }

            // 折点样式
            // 若point.color具有自定义函数func属性
            if (configRight.point?.color?.func) {
                configRight.point.color = eval(configRight.point.color.func)
            }
            // 若point.shape具有自定义函数func属性
            if (configRight.point?.shape?.func) {
                configRight.point.shape = eval(configRight.point.shape.func)
            }
            // 若point.style具有自定义函数func属性
            if (configRight.point?.style?.func) {
                configRight.point.style = eval(configRight.point.style.func)
            }

            // 数据标签
            // 若label.formatter具有自定义函数func属性
            if (configRight.label?.formatter?.func) {
                configRight.label.formatter = eval(configRight.label.formatter.func)
            }

            // 色彩样式
            // 若color具有自定义函数func属性
            if (configRight.color?.func) {
                configRight.color = eval(configRight.color.func)
            }
        } else {
            configRight = cloneDeep(geometryOptions[1])
            // 若columnStyle具有自定义函数func属性
            if (configRight.columnStyle?.func) {
                configRight.columnStyle = eval(configRight.columnStyle.func)
            }

            // 若label.formatter具有自定义函数func属性
            if (configRight.label?.formatter?.func) {
                configRight.label.formatter = eval(configRight.label.formatter.func)
            }

            // 若color具有自定义函数func属性
            if (configRight.color?.func) {
                configRight.color = eval(configRight.color.func)
            }
        }

        // x轴样式
        config.xAxis = cloneDeep(xAxis)
        // 若xAxis.label.formatter具有自定义函数func属性
        if (xAxis?.label?.formatter?.func) {
            config.xAxis.label.formatter = eval(xAxis.label.formatter.func)
        }

        // y轴样式
        config.yAxis = cloneDeep(yAxis)
        // 针对可能存在的yField字段键值对，进行特殊处理
        for (let fieldName of yField) {
            if (config.yAxis && config.yAxis[fieldName]) {
                // 若yAxis[fieldName].label.formatter具有自定义函数func属性
                if (yAxis[fieldName]?.label?.formatter?.func) {
                    config.yAxis[fieldName].label.formatter = eval(yAxis[fieldName].label.formatter.func)
                }
            }
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

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)
        configLeft = omitBy(configLeft, isUndefined)
        configRight = omitBy(configRight, isUndefined)

        return <DualAxes id={id}
            key={key}
            className={className}
            style={style}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
            ref={this.chartRef}
            geometryOptions={[configLeft, configRight]}
            {...config} />;
    }
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
    data: PropTypes.arrayOf(
        PropTypes.arrayOf(PropTypes.object)
    ).isRequired,

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
                        func: PropTypes.string
                    })
                ])
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
                        func: PropTypes.string
                    })
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
                        func: PropTypes.string
                    })
                ])
            })
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

    // 配置动画相关参数
    animation: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.bool
    ]),

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
AntdDualAxes.defaultProps = {
    downloadTrigger: 'download-trigger'
}