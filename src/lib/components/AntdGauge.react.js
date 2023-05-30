/* eslint-disable no-magic-numbers */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Gauge, G2 } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import {
    baseStyle,
    textBaseStyle,
    axisBasePropTypes,
    themeBasePropTypes
} from './BasePropTypes.react';
import { difference } from './utils';

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

// 定义仪表盘AntdGauge，部分API参数参考https://charts.ant.design/zh/examples/progress-plots/gauge#basic
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
            if (changedProps.indexOf('data') !== -1 && changedProps.length === 1) {
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
            locale,
            limitInPlot,
            range,
            type,
            meter,
            indicator,
            theme
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

// 定义参数或属性
AntdGauge.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置当前仪表盘百分比，必填
    percent: PropTypes.number.isRequired,

    // 设置仪表盘相对画布的外环半径大小，取值应在0~1之间，默认为0.95
    radius: PropTypes.number,

    // 设置仪表盘相对画布的内环半径大小，取值应在0~1之间，默认为0.9
    innerRadius: PropTypes.number,

    // 设置仪表盘的开始角度，弧度制，默认为(-7 / 6) * pi
    startAngle: PropTypes.number,

    // 设置仪表盘的终止角度，弧度制，默认为(1 / 6) * pi
    endAngle: PropTypes.number,

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

    // 设置仪表盘辅助圆弧样式
    range: PropTypes.exact({
        // 设置辅助圆弧显示刻度的数值数组
        ticks: PropTypes.arrayOf(PropTypes.number),
        // 设置辅助圆弧的背景色
        color: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        // 设置辅助圆弧的像素宽度，不设置时圆弧宽度由radius、innerRadius参数按比例控制
        width: PropTypes.number
    }),

    // 设置仪表盘类型，可选项为'meter'
    type: PropTypes.oneOf(['meter']),

    // 当type='meter'时用于进行仪表盘样式的具体配置
    meter: PropTypes.exact({
        // 仪表盘总步数，默认为50
        steps: PropTypes.number,
        // 设置分步刻度与间距之间的宽度比例关系，默认为0.5
        stepRatio: PropTypes.number
    }),

    // 配置仪表盘样式
    gaugeStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            // 回调函数
            func: PropTypes.string
        })
    ]),

    // 设置坐标轴相关属性
    axis: axisBasePropTypes,

    // 配置仪表盘指示器样式
    indicator: PropTypes.exact({
        // 配置指示器指针样式
        pointer: PropTypes.exact({
            style: baseStyle
        }),
        // 配置指示器圆盘样式
        pin: PropTypes.exact({
            style: baseStyle
        }),

        // 配置指示器指针类型，可选的有'default'、'cursor'、'ring-cursor'、'simple'
        shape: PropTypes.oneOf(['default', 'cursor', 'ring-cursor', 'simple'])
    }),

    // 配置仪表盘中心文本内容
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
        style: textBaseStyle
    }),

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
AntdGauge.defaultProps = {
    radius: 0.95,
    downloadTrigger: 'download-trigger'
}