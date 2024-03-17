/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Liquid } from '@ant-design/plots';
import React, { Component } from 'react';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import { difference, withTheme } from '../../components/utils';
import { propTypes, defaultProps } from '../../components/AntdLiquid.react';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state'
];

// 定义水波图组件AntdLiquid，部分API参数参考https://charts.ant.design/zh/examples/progress-plots/liquid#basic
export default class AntdLiquid extends Component {

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
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            pixelRatio,
            locale,
            limitInPlot,
            liquidStyle,
            shape,
            color,
            outline,
            wave,
            statistic,
            animation,
            theme,
            pattern,
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
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            pixelRatio,
            locale,
            limitInPlot,
            shape,
            outline,
            wave,
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
        // 水波图样式
        config.liquidStyle = cloneDeep(liquidStyle)
        // 若liquidStyle具有自定义函数func属性
        if (liquidStyle?.func) {
            config.liquidStyle = eval(liquidStyle.func)
        }

        // 色彩样式
        config.color = cloneDeep(color)
        // 若color具有自定义函数func属性
        if (color?.func) {
            config.color = eval(color.func)
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

        return <Liquid
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

AntdLiquid.defaultProps = defaultProps;
AntdLiquid.propTypes = propTypes;