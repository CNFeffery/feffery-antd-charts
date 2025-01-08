/* eslint-disable no-magic-numbers */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Gauge, G2 } from '@ant-design/plots';
import React, { Component } from 'react';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import { difference, withTheme } from '../../components/utils';
import { propTypes, defaultProps } from '../../components/AntdGauge.react';

// 自定义指示器shape
const { registerShape, Util } = G2;

registerShape('point', 'cursor-gauge-indicator', {
    draw(cfg, container) {
        const { indicator, defaultColor } = cfg.customInfo;
        const { pointer } = indicator;
        const group = container.addGroup();

        const center = this.parsePoint({
            x: 0,
            y: 0,
        });

        if (pointer) {
            const { startAngle, endAngle } = Util.getAngle(cfg, this.coordinate);
            const radius = this.coordinate.getRadius();
            const midAngle = (startAngle + endAngle) / 2;
            const { x: x1, y: y1 } = Util.polarToCartesian(center.x, center.y, radius / 15, midAngle + 1 / Math.PI);
            const { x: x2, y: y2 } = Util.polarToCartesian(center.x, center.y, radius / 15, midAngle - 1 / Math.PI);
            const { x, y } = Util.polarToCartesian(center.x, center.y, radius * 0.65, midAngle);
            const path = [['M', center.x, center.y], ['L', x1, y1], ['L', x, y], ['L', x2, y2], ['Z']];

            group.addShape('path', {
                name: 'pointer',
                attrs: {
                    path,
                    fill: defaultColor,
                    ...pointer.style,
                },
            });
        }

        return group;
    },
});

registerShape('point', 'ring-cursor-gauge-indicator', {
    draw(cfg, container) {
        const { indicator, defaultColor } = cfg.customInfo;
        const { pointer, pin } = indicator;
        const group = container.addGroup();

        const center = this.parsePoint({
            x: 0,
            y: 0,
        });

        if (pointer) {
            const { startAngle, endAngle } = Util.getAngle(cfg, this.coordinate);
            const radius = this.coordinate.getRadius();
            const midAngle = (startAngle + endAngle) / 2;
            const { x: x1, y: y1 } = Util.polarToCartesian(center.x, center.y, radius / 15, midAngle + 1 / Math.PI);
            const { x: x2, y: y2 } = Util.polarToCartesian(center.x, center.y, radius / 15, midAngle - 1 / Math.PI);
            const { x, y } = Util.polarToCartesian(center.x, center.y, radius * 0.65, midAngle);
            const { x: x0, y: y0 } = Util.polarToCartesian(center.x, center.y, radius * 0.1, midAngle + Math.PI);
            const path = [['M', x0, y0], ['L', x1, y1], ['L', x, y], ['L', x2, y2], ['Z']];

            group.addShape('path', {
                name: 'pointer',
                attrs: {
                    path,
                    fill: defaultColor,
                    ...pointer.style,
                },
            });
        }

        if (pin) {
            const pinStyle = pin.style || {};
            const { lineWidth = 2, fill = defaultColor, stroke = defaultColor } = pinStyle;
            const r = 6;
            group.addShape('circle', {
                name: 'pin-outer',
                attrs: {
                    x: center.x,
                    y: center.y,
                    ...pin.style,
                    fill: 'transparent',
                    r: r * 1.5,
                    lineWidth,
                    stroke: stroke,
                },
            });
            group.addShape('circle', {
                name: 'pin-inner',
                attrs: {
                    x: center.x,
                    y: center.y,
                    r,
                    stroke: 'transparent',
                    fill,
                },
            });
        }

        return group;
    },
});

registerShape('point', 'simple-gauge-indicator', {
    draw(cfg, container) {
        const { indicator, defaultColor } = cfg.customInfo;
        const { pointer } = indicator;
        const group = container.addGroup()

        const center = this.parsePoint({
            x: 0,
            y: 0,
        });

        if (pointer) {
            const { startAngle, endAngle } = Util.getAngle(cfg, this.coordinate);
            const radius = this.coordinate.getRadius();
            const midAngle = (startAngle + endAngle) / 2;
            const { x: x1, y: y1 } = Util.polarToCartesian(center.x, center.y, radius * 0.52, midAngle + Math.PI / 30);
            const { x: x2, y: y2 } = Util.polarToCartesian(center.x, center.y, radius * 0.52, midAngle - Math.PI / 30);
            const { x, y } = Util.polarToCartesian(center.x, center.y, radius * 0.6, midAngle);
            const path = [['M', x1, y1], ['L', x, y], ['L', x2, y2], ['Z']];

            group.addShape('path', {
                name: 'pointer',
                attrs: {
                    path,
                    fill: defaultColor,
                    ...pointer.style,
                },
            });
        }

        return group;
    },
});

// 指针名称 -> 指针id映射
const name2indicator = new Map([
    ['default', 'gauge-indicator'],
    ['cursor', 'cursor-gauge-indicator'],
    ['ring-cursor', 'ring-cursor-gauge-indicator'],
    ['simple', 'simple-gauge-indicator'],
])

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state'
];

/**
 * 仪表盘组件AntdGauge
 */
export default class AntdGauge extends Component {

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
                // chart.changeData(nextProps.data)
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
            percent,
            radius,
            innerRadius,
            startAngle,
            endAngle,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            pixelRatio,
            locale,
            limitInPlot,
            range,
            type,
            meter,
            gaugeStyle,
            axis,
            indicator,
            statistic,
            animation,
            theme,
            interactions,
            state,
            setProps,
            loading_state
        } = this.props;

        // 初始化config参数对象，每次渲染前的参数解析变动只在config中生效
        let config = {};

        // 刷新基础参数
        config = {
            ...config,
            percent,
            radius,
            innerRadius,
            startAngle,
            endAngle,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            pixelRatio,
            locale,
            limitInPlot,
            range,
            type,
            meter,
            indicator,
            theme: (
                // 融合内置主题与自定义主题
                theme && theme.withTheme ?
                    withTheme(theme.withTheme, theme) :
                    theme
            ),
            interactions,
            state
        }
        // 映射指示器类型
        if (config.indicator?.shape) {
            config.indicator.shape = name2indicator.get(config.indicator.shape)
        }

        // 进阶参数
        // 仪表盘样式
        config.gaugeStyle = cloneDeep(gaugeStyle)
        // 若gaugeStyle具有自定义函数func属性
        if (gaugeStyle?.func) {
            config.gaugeStyle = eval(gaugeStyle.func)
        }

        // 坐标轴样式
        config.axis = cloneDeep(axis)
        // 若axis.label.formatter具有自定义函数func属性
        if (axis?.label?.formatter?.func) {
            config.axis.label.formatter = eval(axis.label.formatter.func)
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

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Gauge
            id={id}
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

AntdGauge.defaultProps = defaultProps;
AntdGauge.propTypes = propTypes;