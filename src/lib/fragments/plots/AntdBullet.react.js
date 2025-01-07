/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Bullet } from '@ant-design/plots';
import React, { Component } from 'react';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import { difference, withTheme } from '../../components/utils';
import { propTypes, defaultProps } from '../../components/AntdBullet.react';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state'
];

/**
 * 子弹图组件AntdBullet
 */
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
            pixelRatio,
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
            interactions,
            state,
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
            pixelRatio,
            locale,
            limitInPlot,
            layout,
            color,
            theme: (
                // 融合内置主题与自定义主题
                theme && theme.withTheme ?
                    withTheme(theme.withTheme, theme) :
                    theme
            ),
            interactions,
            state
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

AntdBullet.defaultProps = defaultProps;
AntdBullet.propTypes = propTypes;