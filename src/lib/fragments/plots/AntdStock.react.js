/* eslint-disable no-unused-vars */
/* eslint-disable no-else-return */
/* eslint-disable no-magic-numbers */
/* eslint-disable no-undefined */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Stock } from '@ant-design/plots';
import React, { Component } from 'react';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import { difference, withTheme } from '../../components/utils';
import { propTypes, defaultProps } from '../../components/AntdStock.react';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'setProps',
    'component_loading',
    'recentlyTooltipChangeRecord',
    'recentlyAreaClickRecord',
    'recentlyLegendInfo',
    'recentlySliderRange',
];

/**
 * 股票图组件AntdStock
 */
export default class AntdStock extends Component {

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
            pixelRatio,
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
            state,
            recentlySliderRange,
            component_loading,
            setProps
        } = this.props;

        // 初始化config参数对象，每次渲染前的参数解析变动只在config中生效
        let config = {};

        // 预处理元信息
        if (meta) {
            config.meta = cloneDeep(meta);
            for (let metaKey of Object.keys(meta)) {
                // 若meta中当前字段属性下的formatter具有自定义函数func属性
                if (meta[metaKey]?.formatter?.func) {
                    config.meta[metaKey].formatter = eval(meta[metaKey].formatter.func)
                }
            }
        }

        // 刷新基础参数
        config = {
            ...config,
            data,
            padding,
            appendPadding,
            xField,
            yField,
            risingFill,
            fallingFill,
            width,
            height,
            autoFit,
            renderer,
            pixelRatio,
            theme: (
                // 融合内置主题与自定义主题
                theme && theme.withTheme ?
                    withTheme(theme.withTheme, theme) :
                    theme
            ),
            interactions,
            state,
            locale,
            limitInPlot
        };

        // 进阶参数
        // 股票图图形样式
        config.stockStyle = stockStyle
        // 若stockStyle具有自定义函数func属性
        if (stockStyle?.func) {
            config.stockStyle = eval(stockStyle.func)
        }

        // x轴样式
        config.xAxis = xAxis
        // 若xAxis.label.formatter具有自定义函数func属性
        if (xAxis?.label?.formatter?.func) {
            config.xAxis.label.formatter = eval(xAxis.label.formatter.func)
        }

        // y轴样式
        config.yAxis = yAxis
        // 若yAxis.label.formatter具有自定义函数func属性
        if (yAxis?.label?.formatter?.func) {
            config.yAxis.label.formatter = eval(yAxis.label.formatter.func)
        }

        // 图例样式
        config.legend = legend
        // 若legend.itemName.formatter具有自定义函数func属性
        if (legend?.itemName?.formatter?.func) {
            config.legend.itemName.formatter = eval(legend.itemName.formatter.func)
        }
        // 若legend.itemValue.formatter具有自定义函数func属性
        if (legend?.itemValue?.formatter?.func) {
            config.legend.itemValue.formatter = eval(legend.itemValue.formatter.func)
        }

        // 数据标签
        config.label = label
        // 若label.formatter具有自定义函数func属性
        if (label?.formatter?.func) {
            config.label.formatter = eval(label.formatter.func)
        }

        // 标注
        config.annotations = annotations

        // 缩略轴
        config.slider = slider
        // 若slider.formatter具有自定义函数func属性
        if (slider?.formatter?.func) {
            config.slider.formatter = eval(slider.formatter.func)
        }

        // 悬浮提示
        config.tooltip = tooltip
        // 若tooltip.formatter具有自定义函数func属性
        if (tooltip?.formatter?.func) {
            config.tooltip.formatter = eval(tooltip.formatter.func)
        }
        // 若tooltip.customContent具有自定义函数func属性
        if (tooltip?.customContent?.func) {
            config.tooltip.customContent = eval(tooltip.customContent.func)
        }
        // 若tooltip.customItems具有自定义函数func属性
        if (tooltip?.customItems?.func) {
            config.tooltip.customItems = eval(tooltip.customItems.func)
        }

        // 补充指示器
        config.tooltip = {
            ...config.tooltip,
            crosshairs: {
                line: {
                    style: {
                        lineWidth: 0.5,
                        stroke: 'rgba(0,0,0,0.25)',
                    },
                },
                text: (type, defaultContent, items) => {
                    let textContent;
                    if (type === 'x') {
                        let item = items[0];
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
                }
            }
        }

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Stock id={id}
            key={key}
            className={className}
            style={style}
            data-dash-is-loading={component_loading}
            ref={this.chartRef}
            // 绑定常用事件
            onReady={(plot) => {
                // 监听非数据要素区域点击事件
                plot.on('plot:click', (e) => {
                    if (!e.data) {
                        setProps({
                            recentlyAreaClickRecord: {
                                timestamp: (new Date()).valueOf(),
                                data: null
                            }
                        })
                    }
                });

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
                        recentlyAreaClickRecord: {
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
                // 监听缩略轴最新变化后的范围
                plot.on('slider:valuechanged', (e) => {
                    let sliderRangeStart = e.gEvent.delegateObject.slider.cfg.start;
                    let sliderRangeEnd = e.gEvent.delegateObject.slider.cfg.end;
                    if (
                        recentlySliderRange?.range &&
                        recentlySliderRange.range[0] === Number(sliderRangeStart.toFixed(2)) &&
                        recentlySliderRange.range[1] === Number(sliderRangeEnd.toFixed(2))
                    ) {
                        return;
                    }
                    // 否则更新recentlySliderRange
                    setProps({
                        recentlySliderRange: {
                            timestamp: (new Date()).valueOf(),
                            range: [Number(sliderRangeStart.toFixed(2)), Number(sliderRangeEnd.toFixed(2))]
                        }
                    })
                })
            }}
            {...config} />;

    }
}

AntdStock.defaultProps = defaultProps;
AntdStock.propTypes = propTypes;