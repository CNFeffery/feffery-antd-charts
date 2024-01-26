/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import { Column } from '@ant-design/plots';
import React, { Component } from 'react';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import { difference } from '../../components/utils';
import { propTypes, defaultProps } from '../../components/AntdColumn.react';

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
            pattern,
            interactions,
            setProps,
            loading_state
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

        // 图形填充贴图样式
        config.pattern = cloneDeep(pattern)
        // 若pattern具有自定义函数func属性
        if (pattern?.func) {
            config.pattern = eval(pattern.func)
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

AntdColumn.defaultProps = defaultProps;
AntdColumn.propTypes = propTypes;