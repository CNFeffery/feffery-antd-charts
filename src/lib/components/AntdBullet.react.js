/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Bullet } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import {
    metaBasePropTypes,
    areaBaseStyle,
    labelBasePropTypes,
    tooltipBasePropTypes,
    axisBasePropTypes,
    legendBasePropTypes,
    themeBasePropTypes
} from './BasePropTypes.react';
import { difference } from './utils';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state'
];

// 定义子弹图组件AntdBullet，部分API参数参考https://charts.ant.design/zh/examples/progress-plots/bullet#basic
export default class AntdBullet extends Component {

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
            measureField,
            rangeField,
            targetField,
            xField,
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
            layout,
            color,
            size,
            bulletStyle,
            label,
            tooltip,
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
            measureField,
            rangeField,
            targetField,
            xField,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            limitInPlot,
            layout,
            color,
            theme
        }

        // 进阶参数
        // 子弹图各图形尺寸
        config.size = cloneDeep(size)
        // 若size.range具有自定义函数func属性
        if (size?.range?.func) {
            config.size.range = eval(size.range.func)
        }
        // 若size.measure具有自定义函数func属性
        if (size?.measure?.func) {
            config.size.measure = eval(size.measure.func)
        }
        // 若size.target具有自定义函数func属性
        if (size?.target?.func) {
            config.size.target = eval(size.target.func)
        }

        // 子弹图各图形样式
        config.bulletStyle = cloneDeep(bulletStyle)
        // 若bulletStyle.range具有自定义函数func属性
        if (bulletStyle?.range?.func) {
            config.bulletStyle.range = eval(bulletStyle.range.func)
        }
        // 若bulletStyle.measure具有自定义函数func属性
        if (bulletStyle?.measure?.func) {
            config.bulletStyle.measure = eval(bulletStyle.measure.func)
        }
        // 若bulletStyle.target具有自定义函数func属性
        if (bulletStyle?.target?.func) {
            config.bulletStyle.target = eval(bulletStyle.target.func)
        }

        // 数据标签
        config.label = cloneDeep(label)
        // 若label.range.formatter具有自定义函数func属性
        if (label?.range?.formatter?.func) {
            config.label.range.formatter = eval(label.range.formatter.func)
        }
        // 若label.measure.formatter具有自定义函数func属性
        if (label?.measure?.formatter?.func) {
            config.label.measure.formatter = eval(label.measure.formatter.func)
        }
        // 若label.target.formatter具有自定义函数func属性
        if (label?.target?.formatter?.func) {
            config.label.target.formatter = eval(label.target.formatter.func)
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

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Bullet
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
AntdBullet.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置子弹图绘图所需数据
    // 格式如：[{title: '满意度', ranges: [50,100], measures: [80], target: 85}]
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 设置作为子弹图长度的字段
    measureField: PropTypes.string.isRequired,

    // 设置作为子弹图背景色条长度的字段
    rangeField: PropTypes.string.isRequired,

    // 设置作为子弹图目标值位置的字段
    targetField: PropTypes.string.isRequired,

    // 用于设置分组依据字段
    xField: PropTypes.string,

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

    // 设置子弹图方向，可选的有'horizontal'、'vertical'
    // 默认为'horizontal'
    layout: PropTypes.oneOf(['horizontal', 'vertical']),

    // 配置子弹图各图形色彩
    color: PropTypes.exact({
        // 区间背景颜色
        range: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        // 实际值颜色
        measure: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ]),
        // 目标值颜色
        target: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string)
        ])
    }),

    // 设置子弹图各图形尺寸
    size: PropTypes.exact({
        // 区间背景像素尺寸，默认为30
        range: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number),
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ]),
        // 实际值像素尺寸，默认值为20
        measure: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number),
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ]),
        // 目标值像素尺寸，默认为20
        target: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number),
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ])
    }),

    // 配置子弹图各图形样式
    bulletStyle: PropTypes.exact({
        // 区间背景样式，默认为{ fillOpacity: 0.5 }
        range: PropTypes.oneOfType([
            areaBaseStyle,
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ]),
        // 实际值样式
        measure: PropTypes.oneOfType([
            areaBaseStyle,
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ]),
        // 目标值样式
        target: PropTypes.oneOfType([
            areaBaseStyle,
            PropTypes.exact({
                // 回调函数
                func: PropTypes.string
            })
        ])
    }),

    // 配置子弹图各图形文本标签
    label: PropTypes.exact({
        // 区间文本标签
        range: labelBasePropTypes,
        // 实际值文本标签
        measure: labelBasePropTypes,
        // 目标值文本标签
        target: labelBasePropTypes
    }),

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

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
AntdBullet.defaultProps = {
    layout: 'horizontal',
    downloadTrigger: 'download-trigger'
}