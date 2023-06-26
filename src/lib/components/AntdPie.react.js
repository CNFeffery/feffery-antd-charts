/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable prefer-const */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import { Pie } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import {
    metaBasePropTypes,
    legendBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    baseStyle,
    themeBasePropTypes
} from './BasePropTypes.react';
import { difference } from './utils';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state',
    'recentlyTooltipChangeRecord',
    'recentlySectorClickRecord',
    'recentlyLegendInfo'
];

// 定义饼图组件AntdPie，部分API参数参考https://charts.ant.design/zh-CN/demos/pie
export default class AntdPie extends Component {

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
            limitInPlot,
            legend,
            label,
            tooltip,
            annotations,
            animation,
            theme,
            loading_state,
            setProps
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
            padding,
            appendPadding,
            angleField,
            colorField,
            radius,
            innerRadius,
            startAngle,
            endAngle,
            width,
            height,
            autoFit,
            renderer,
            theme,
            locale,
            limitInPlot
        };

        // 进阶参数
        // 色彩样式
        config.color = cloneDeep(color)
        // 若color具有自定义函数func属性
        if (color?.func) {
            config.color = eval(color.func)
        }

        // 扇形样式
        config.pieStyle = cloneDeep(pieStyle)
        // 若pieStyle具有自定义函数func属性
        if (pieStyle?.func) {
            config.pieStyle = eval(pieStyle.func)
        }

        // 统计值样式
        config.statistic = cloneDeep(statistic)
        if (statistic?.title?.formatter?.func) {
            config.statistic.title.formatter = eval(statistic.title.formatter.func)
        }
        if (statistic?.title?.customHtml?.func) {
            config.statistic.title.customHtml = eval(statistic.title.customHtml.func)
        }
        if (statistic?.content?.formatter?.func) {
            config.statistic.content.formatter = eval(statistic.content.formatter.func)
        }
        if (statistic?.content?.customHtml?.func) {
            config.statistic.content.customHtml = eval(statistic.content.customHtml.func)
        }

        // 图例样式
        config.legend = cloneDeep(legend)
        if (legend?.itemName?.formatter?.func) {
            config.legend.itemName.formatter = eval(legend.itemName.formatter.func)
        }
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

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Pie id={id}
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
                    // 当有扇区被点击时
                    setProps({
                        recentlySectorClickRecord: {
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
AntdPie.propTypes = {
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

                // 回调自定义标题文本信息，优先级最高
                // 格式：(container, view, datum, data) => string
                customHtml: PropTypes.exact({
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

                // 回调自定义标题文本信息，优先级最高
                // 格式：(container, view, datum, data) => string
                customHtml: PropTypes.exact({
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

    // 配置交互相关功能
    interactions: PropTypes.arrayOf(PropTypes.exact({
        // 交互项类型，可选的有：
        type: PropTypes.oneOf([
            'element-active',
            'element-selected',
            'element-single-selected',
            'element-highlight',
            'element-highlight-by-color',
            'element-highlight-by-x',
            'legend-highlight',
            'axis-label-highlight',
            'pie-statistic-active'
        ])
    })),

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

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

    // 扇区点击事件
    recentlySectorClickRecord: PropTypes.exact({
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
    downloadTrigger: 'download-trigger'
}