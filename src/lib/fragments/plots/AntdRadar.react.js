/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import { Radar } from '@ant-design/plots';
import React, { Component } from 'react';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import { difference, withTheme } from '../../components/utils';
import { propTypes, defaultProps } from '../../components/AntdRadar.react';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'setProps',
    'component_loading',
    'recentlyTooltipChangeRecord',
    'recentlyAreaClickRecord',
    'recentlyLegendInfo'
];

/**
 * 雷达图组件AntdRadar
 */
export default class AntdRadar extends Component {

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
            seriesField,
            smooth,
            radius,
            startAngle,
            endAngle,
            color,
            lineStyle,
            point,
            area,
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
            animation,
            theme,
            interactions,
            state,
            setProps,
            component_loading
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
            smooth,
            radius,
            startAngle,
            endAngle,
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
        // 色彩样式
        config.color = cloneDeep(color)
        // 若color具有自定义函数func属性
        if (color?.func) {
            config.color = eval(color.func)
        }

        // 折线样式
        config.lineStyle = cloneDeep(lineStyle)
        // 若lineStyle具有自定义函数func属性
        if (lineStyle?.func) {
            config.lineStyle = eval(lineStyle.func)
        }


        // 折点样式
        config.point = cloneDeep(point)
        // 若point.color具有自定义函数func属性
        if (point?.color?.func) {
            config.point.color = eval(point.color.func)
        }
        // 若point.shape具有自定义函数func属性
        if (point?.shape?.func) {
            config.point.shape = eval(point.shape.func)
        }
        // 若point.style具有自定义函数func属性
        if (point?.style?.func) {
            config.point.style = eval(point.style.func)
        }

        // 区域填充样式
        config.area = cloneDeep(area)
        // 若area.color具有自定义函数func属性
        if (area?.color?.func) {
            config.area.color = eval(area.color.func)
        }
        // 若area.style具有自定义函数func属性
        if (area?.style?.func) {
            config.area.style = eval(area.style.func)
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
        // 若tooltip.customContent具有自定义函数func属性
        if (tooltip?.customContent?.func) {
            config.tooltip.customContent = eval(tooltip.customContent.func)
        }
        // 若tooltip.customItems具有自定义函数func属性
        if (tooltip?.customItems?.func) {
            config.tooltip.customItems = eval(tooltip.customItems.func)
        }

        // 标注
        config.annotations = cloneDeep(annotations)
        for (let i = 0; i < (annotations || []).length; i++) {
            // 若annotations[i].html具有自定义函数func属性
            if (annotations[i]?.html?.func) {
                config.annotations[i].html = eval(annotations[i].html.func)
            }
        }

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Radar id={id}
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
            }}
            {...config} />;
    }
}

AntdRadar.defaultProps = defaultProps;
AntdRadar.propTypes = propTypes;