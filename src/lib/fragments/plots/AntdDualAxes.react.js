/* eslint-disable no-unused-vars */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import { DualAxes } from '@ant-design/plots';
import React, { Component } from 'react';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import { difference, withTheme } from '../../components/utils';
import { propTypes, defaultProps } from '../../components/AntdDualAxes.react';

// 定义不触发重绘的参数数组
const preventUpdateProps = ['loading_state', 'recentlyClickRecord'];

// 定义双轴图组件AntdDualAxes，部分API参数参考https://charts.ant.design/zh/examples/dual-axes/dual-line#dual-line
export default class AntdDualAxes extends Component {
    constructor(props) {
        super(props);
        this.chartRef = React.createRef();
    }

    shouldComponentUpdate(nextProps) {
        // 计算发生变化的参数名
        const changedProps = Object.keys(difference(this.props, nextProps));

        // 若无变化的props，则不触发重绘
        if (changedProps.length === 0) {
            return false;
        }

        // 计算发生变化的参数名与需要阻止重绘的参数名数组的交集
        let changedPreventUpdateProps = intersection(
            changedProps,
            preventUpdateProps
        );

        // 若有交集，则不触发重绘
        if (changedPreventUpdateProps.length !== 0) {
            return false;
        } else {
            // 取得plot实例
            const chart = this.chartRef.current.getChart();
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
            if (
                changedProps.indexOf('downloadTrigger') !== -1 &&
                changedProps.length === 1
            ) {
                // 导出当前图表为png格式文件
                chart.downloadImage();
                return false;
            }
        }
        return true;
    }

    render() {
        // 取得必要属性或参数
        let {
            id,
            key,
            className,
            style,
            data,
            meta,
            xField,
            yField,
            geometryOptions,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            pixelRatio,
            locale,
            limitInPlot,
            tooltip,
            xAxis,
            yAxis,
            annotations,
            slider,
            legend,
            animation,
            theme,
            interactions,
            state,
            setProps,
            loading_state,
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
            xField,
            yField,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            pixelRatio,
            locale,
            limitInPlot,
            theme: (
                // 融合内置主题与自定义主题
                theme && theme.withTheme ?
                    withTheme(theme.withTheme, theme) :
                    theme
            ),
            interactions,
            state
        };

        // 初始化左右轴config参数对象，每次渲染前的参数解析变动只在config中生效
        let configLeft = {};
        let configRight = {};
        // 进阶参数
        if (geometryOptions[0].geometry === 'line') {
            configLeft = cloneDeep(geometryOptions[0]);
            // 折线样式
            // 若lineStyle具有自定义函数func属性
            if (configLeft.lineStyle?.func) {
                configLeft.lineStyle = eval(configLeft.lineStyle.func);
            }

            // 折点样式
            // 若point.color具有自定义函数func属性
            if (configLeft.point?.color?.func) {
                configLeft.point.color = eval(configLeft.point.color.func);
            }
            // 若point.shape具有自定义函数func属性
            if (configLeft.point?.shape?.func) {
                configLeft.point.shape = eval(configLeft.point.shape.func);
            }
            // 若point.style具有自定义函数func属性
            if (configLeft.point?.style?.func) {
                configLeft.point.style = eval(configLeft.point.style.func);
            }

            // 数据标签
            // 若label.formatter具有自定义函数func属性
            if (configLeft.label?.formatter?.func) {
                configLeft.label.formatter = eval(
                    configLeft.label.formatter.func
                );
            }

            // 色彩样式
            // 若color具有自定义函数func属性
            if (configLeft.color?.func) {
                configLeft.color = eval(configLeft.color.func);
            }
        } else {
            configLeft = cloneDeep(geometryOptions[0]);
            // 若columnStyle具有自定义函数func属性
            if (configLeft.columnStyle?.func) {
                configLeft.columnStyle = eval(configLeft.columnStyle.func);
            }

            // 若label.formatter具有自定义函数func属性
            if (configLeft.label?.formatter?.func) {
                configLeft.label.formatter = eval(
                    configLeft.label.formatter.func
                );
            }

            // 若color具有自定义函数func属性
            if (configLeft.color?.func) {
                configLeft.color = eval(configLeft.color.func);
            }
        }

        if (geometryOptions[1].geometry === 'line') {
            configRight = cloneDeep(geometryOptions[1]);
            // 折线样式
            // 若lineStyle具有自定义函数func属性
            if (configRight.lineStyle?.func) {
                configRight.lineStyle = eval(configRight.lineStyle.func);
            }

            // 折点样式
            // 若point.color具有自定义函数func属性
            if (configRight.point?.color?.func) {
                configRight.point.color = eval(configRight.point.color.func);
            }
            // 若point.shape具有自定义函数func属性
            if (configRight.point?.shape?.func) {
                configRight.point.shape = eval(configRight.point.shape.func);
            }
            // 若point.style具有自定义函数func属性
            if (configRight.point?.style?.func) {
                configRight.point.style = eval(configRight.point.style.func);
            }

            // 数据标签
            // 若label.formatter具有自定义函数func属性
            if (configRight.label?.formatter?.func) {
                configRight.label.formatter = eval(
                    configRight.label.formatter.func
                );
            }

            // 色彩样式
            // 若color具有自定义函数func属性
            if (configRight.color?.func) {
                configRight.color = eval(configRight.color.func);
            }
        } else {
            configRight = cloneDeep(geometryOptions[1]);
            // 若columnStyle具有自定义函数func属性
            if (configRight.columnStyle?.func) {
                configRight.columnStyle = eval(configRight.columnStyle.func);
            }

            // 若label.formatter具有自定义函数func属性
            if (configRight.label?.formatter?.func) {
                configRight.label.formatter = eval(
                    configRight.label.formatter.func
                );
            }

            // 若color具有自定义函数func属性
            if (configRight.color?.func) {
                configRight.color = eval(configRight.color.func);
            }
        }

        // x轴样式
        config.xAxis = cloneDeep(xAxis);
        // 若xAxis.label.formatter具有自定义函数func属性
        if (xAxis?.label?.formatter?.func) {
            config.xAxis.label.formatter = eval(xAxis.label.formatter.func);
        }

        // y轴样式
        config.yAxis = cloneDeep(yAxis);
        // 针对可能存在的yField字段键值对，进行特殊处理
        for (let fieldName of yField) {
            if (config.yAxis && config.yAxis[fieldName]) {
                // 若yAxis[fieldName].label.formatter具有自定义函数func属性
                if (yAxis[fieldName]?.label?.formatter?.func) {
                    config.yAxis[fieldName].label.formatter = eval(
                        yAxis[fieldName].label.formatter.func
                    );
                }
            }
        }

        // 图例样式
        config.legend = cloneDeep(legend);
        // 若legend.itemName.formatter具有自定义函数func属性
        if (legend?.itemName?.formatter?.func) {
            config.legend.itemName.formatter = eval(
                legend.itemName.formatter.func
            );
        }
        // 若legend.itemValue.formatter具有自定义函数func属性
        if (legend?.itemValue?.formatter?.func) {
            config.legend.itemValue.formatter = eval(
                legend.itemValue.formatter.func
            );
        }

        // 悬浮提示
        config.tooltip = cloneDeep(tooltip);
        // 若tooltip.formatter具有自定义函数func属性
        if (tooltip?.formatter?.func) {
            config.tooltip.formatter = eval(tooltip.formatter.func);
        }
        // 若tooltip.customItems具有自定义函数func属性
        if (tooltip?.customItems?.func) {
            config.tooltip.customItems = eval(tooltip.customItems.func);
        }

        // 标注
        config.annotations = cloneDeep(annotations);
        for (let i = 0; i < (annotations || []).length; i++) {
            // 若annotations[i].html具有自定义函数func属性
            if (annotations[i]?.html?.func) {
                config.annotations[i].html = eval(annotations[i].html.func)
            }
        }

        // 缩略轴
        config.slider = cloneDeep(slider)
        // 若slider.formatter具有自定义函数func属性
        if (slider?.formatter?.func) {
            config.slider.formatter = eval(slider.formatter.func)
        }

        // 动画
        config.animation = cloneDeep(animation);

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined);
        configLeft = omitBy(configLeft, isUndefined);
        configRight = omitBy(configRight, isUndefined);

        return (
            <DualAxes
                id={id}
                key={key}
                className={className}
                style={style}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
                ref={this.chartRef}
                geometryOptions={[configLeft, configRight]}
                // 绑定常用事件
                onReady={(plot) => {
                    // 监听非数据要素区域点击事件
                    plot.on('plot:click', (e) => {
                        if (!e.data) {
                            setProps({
                                recentlyClickRecord: {
                                    timestamp: (new Date()).valueOf(),
                                    data: null
                                }
                            })
                        }
                    });

                    plot.on('element:click', (e) => {
                        setProps({
                            recentlyClickRecord: {
                                timestamp: new Date().valueOf(),
                                data: e.data.data,
                            },
                        });
                    });
                }}
                {...config}
            />
        );
    }
}

AntdDualAxes.defaultProps = defaultProps;
AntdDualAxes.propTypes = propTypes;