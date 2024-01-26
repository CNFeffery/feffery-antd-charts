/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Chord } from '@ant-design/plots';
import React, { Component } from 'react';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import { difference } from '../../components/utils';
import { propTypes, defaultProps } from '../../components/AntdChord.react';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state',
    'recentlyTooltipChangeRecord',
    'recentlyAreaClickRecord'
];

// 定义和弦图组件AntdChord，部分API参数参考https://charts.ant.design/zh/examples/relation-plots/chord#chord-population
export default class AntdChord extends Component {

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
            sourceField,
            targetField,
            weightField,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            limitInPlot,
            nodeStyle,
            edgeStyle,
            nodeWidthRatio,
            nodePaddingRatio,
            label,
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
            sourceField,
            targetField,
            weightField,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            limitInPlot,
            nodeWidthRatio,
            nodePaddingRatio,
            theme,
            interactions
        }

        // 进阶参数
        // 和弦图节点样式
        config.nodeStyle = cloneDeep(nodeStyle)
        // 若nodeStyle具有自定义函数func属性
        if (nodeStyle?.func) {
            config.nodeStyle = eval(nodeStyle.func)
        }

        // 和弦图边样式
        config.edgeStyle = cloneDeep(edgeStyle)
        // 若edgeStyle具有自定义函数func属性
        if (edgeStyle?.func) {
            config.edgeStyle = eval(edgeStyle.func)
        }

        // 数据标签
        config.label = cloneDeep(label)
        // 若label.formatter具有自定义函数func属性
        if (label?.formatter?.func) {
            config.label.formatter = eval(label.formatter.func)
        }

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Chord
            id={id}
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
                        data: e.data.items.map(item => {
                            const { x, y, ...other } = item.data;
                            return other;
                        })
                    }
                    setProps({
                        recentlyTooltipChangeRecord: recentlyTooltipChangeRecord
                    })
                });

                plot.on('element:click', (e) => {
                    const { x, y, ...other } = e.data.data;
                    setProps({
                        recentlyAreaClickRecord: {
                            timestamp: (new Date()).valueOf(),
                            data: other
                        }
                    })
                });
            }}
            {...config} />;
    }
}

AntdChord.defaultProps = defaultProps;
AntdChord.propTypes = propTypes;