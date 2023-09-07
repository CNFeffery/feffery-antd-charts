/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import { Column } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import {
    metaBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    scrollbarBasePropTypes,
    sliderBasePropTypes,
    baseStyle,
    areaBaseStyle,
    textBaseStyle,
    themeBasePropTypes
} from './BasePropTypes.react';
import { difference } from './utils';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state',
    'recentlyTooltipChangeRecord',
    'recentlyColumnClickRecord',
    'recentlyLegendInfo'
];

// 定义柱状图AntdColumn，部分API参数参考https://charts.ant.design/zh-CN/demos/column
export default class AntdColumn extends Component {

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

        // 若changedPreventUpdateProps中所有prop都在preventUpdateProps中，则不触发重绘
        if (changedProps.every(key => preventUpdateProps.includes(key))) {
            return false;
        } else {
            // 取得plot实例
            const chart = this.chartRef.current.getChart()
            // 检查是否仅有data参数发生更新
            // 或除去data参数后其他变化的prop都在preventUpdateProps
            if (
                (changedProps.includes('data') && changedProps.length === 1) ||
                (changedProps.includes('data') && changedPreventUpdateProps.length === changedProps.length - 1)
            ) {
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
            seriesField,
            groupField,
            isStack,
            isGroup,
            isRange,
            isPercent,
            color,
            intervalPadding,
            dodgePadding,
            minColumnWidth,
            maxColumnWidth,
            columnStyle,
            columnBackground,
            columnWidthRatio,
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
            limitInPlot,
            legend,
            label,
            tooltip,
            annotations,
            slider,
            animation,
            theme,
            interactions,
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
            seriesField,
            groupField,
            isStack,
            isGroup,
            isRange,
            isPercent,
            intervalPadding,
            dodgePadding,
            minColumnWidth,
            maxColumnWidth,
            columnBackground,
            columnWidthRatio,
            marginRatio,
            scrollbar,
            connectedArea,
            width,
            height,
            autoFit,
            renderer,
            theme,
            interactions,
            locale,
            limitInPlot
        };

        // 进阶参数
        config.conversionTag = cloneDeep(conversionTag)
        // 若color具有自定义函数func属性
        if (conversionTag?.text?.formatter?.func) {
            config.conversionTag.text.formatter = eval(conversionTag.text.formatter.func)
        }

        // 色彩样式
        config.color = cloneDeep(color)
        // 若color具有自定义函数func属性
        if (color?.func) {
            config.color = eval(color.func)
        }

        config.columnStyle = cloneDeep(columnStyle)
        // 若columnStyle具有自定义函数func属性
        if (columnStyle?.func) {
            config.columnStyle = eval(columnStyle.func)
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

        // 缩略轴
        config.slider = cloneDeep(slider)
        // 若slider.formatter具有自定义函数func属性
        if (slider?.formatter?.func) {
            config.slider.formatter = eval(slider.formatter.func)
        }

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Column id={id}
            key={key}
            className={className}
            style={style}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
            ref={this.chartRef}
            // 绑定常用事件
            onReady={(plot) => {

                let recentlyTooltipChangeRecord;
                // 辅助的tooltip渲染事件
                plot.on('tooltip:change', (e) => {

                    // 更新recentlyTooltipChangeRecord
                    recentlyTooltipChangeRecord = {
                        timestamp: (new Date()).valueOf(),
                        data: e.data.items.map(item => item.data)
                    }
                    setProps({
                        recentlyTooltipChangeRecord: recentlyTooltipChangeRecord
                    })
                });

                plot.on('element:click', (e) => {
                    setProps({
                        recentlyColumnClickRecord: {
                            timestamp: (new Date()).valueOf(),
                            data: e.data.data
                        }
                    })
                });

                plot.on('legend-item:click', (e) => {
                    let component = e.target.get('delegateObject').component;
                    setProps({
                        recentlyLegendInfo: {
                            triggerItemName: e.target.attrs.text,
                            items: component.cfg.items.map(
                                item => {
                                    let { marker, showRadio, ...other } = item;
                                    return other
                                }
                            )
                        }
                    })
                });
            }}
            {...config} />;
    }
}

// 定义参数或属性
AntdColumn.propTypes = {
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

    // 定义作为y轴的字段名，格式为[左轴对应y轴字段, 右轴对应y轴字段]
    yField: PropTypes.string.isRequired,

    // 定义作为分组依据的字段名
    seriesField: PropTypes.string,

    // 用于在堆叠分组柱状图中指定分组字段，此时seriesField指定的字段会作为每个组内堆叠的分层依据
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

    // 配置缩略轴相关参数
    slider: sliderBasePropTypes,

    // 设置分组条形图组间像素间隔宽度
    intervalPadding: PropTypes.number,

    // 设置分组条形图组内像素间隔宽度
    dodgePadding: PropTypes.number,

    // 设置柱状图的最小像素宽度
    minColumnWidth: PropTypes.number,

    // 设置柱状图的最大像素宽度
    maxColumnWidth: PropTypes.number,

    // 设置柱体的样式
    columnStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 设置柱状图背景样式
    columnBackground: PropTypes.exact({
        // 具体样式
        style: areaBaseStyle
    }),

    // 设置柱状图宽度占比，0~1之间
    columnWidthRatio: PropTypes.number,

    // 设置分组柱状图中条形之间的间距，0~1之间
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

    // 单独column点击事件
    recentlyColumnClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.object
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

    // 柱体点击事件
    recentlyBarClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.object
    }),

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
AntdColumn.defaultProps = {
    downloadTrigger: 'download-trigger'
}