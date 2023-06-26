/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Sunburst } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import {
    textBaseStyle,
    areaBaseStyle,
    metaBasePropTypes,
    labelBasePropTypes,
    tooltipBasePropTypes,
    annotationsBasePropTypes,
    themeBasePropTypes
} from './BasePropTypes.react';
import { difference } from './utils';

// 定义不触发重绘的参数数组
const preventUpdateProps = [
    'loading_state',
    'recentlyTooltipChangeRecord',
    'recentlyAreaClickRecord'
];

// 定义旭日图组件AntdSunburst，部分API参数参考https://charts.ant.design/zh/examples/more-plots/sunburst#basic
export default class AntdSunburst extends Component {

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
            colorField,
            rawFields,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            limitInPlot,
            hierarchyConfig,
            drilldown,
            radius,
            innerRadius,
            color,
            sunburstStyle,
            reflect,
            label,
            tooltip,
            annotations,
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
            colorField,
            rawFields,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            limitInPlot,
            radius,
            innerRadius,
            drilldown,
            theme,
            reflect: reflect ? 'y' : undefined,
        }

        // 进阶参数
        // 色彩样式
        config.color = cloneDeep(color)
        // 若color具有自定义函数func属性
        if (color?.func) {
            config.color = eval(color.func)
        }

        // 层次布局配置参数
        config.hierarchyConfig = cloneDeep(hierarchyConfig)

        // 色彩样式
        config.sunburstStyle = cloneDeep(sunburstStyle)
        // 若sunburstStyle具有自定义函数func属性
        if (sunburstStyle?.func) {
            config.sunburstStyle = eval(sunburstStyle.func)
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

        // 动画
        config.animation = cloneDeep(animation)

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Sunburst
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
                            return {
                                name: item.data.name,
                                path: item.data.path,
                                ancestor_node: item.data['ancestor-node']
                            }
                        })
                    }
                    setProps({
                        recentlyTooltipChangeRecord: recentlyTooltipChangeRecord
                    })
                });

                plot.on('element:click', (e) => {

                    setProps({
                        recentlyAreaClickRecord: {
                            timestamp: (new Date()).valueOf(),
                            data: {
                                name: e.data.data.name,
                                path: e.data.data.path,
                                ancestor_node: e.data.data['ancestor-node']
                            }
                        }
                    })
                });
            }}
            {...config} />;
    }
}

// 定义参数或属性
AntdSunburst.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 定义绘图所需数据，必须参数
    data: PropTypes.object.isRequired,

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 定义色彩区分所依据的字段，默认为祖先节点的name字段
    colorField: PropTypes.string,

    // 定义额外的原始字段名数组，可在tooltip等回调函数中用于取得辅助用数据
    rawFields: PropTypes.arrayOf(PropTypes.string),

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

    // 图形样式类参数

    // 层级布局配置参数
    hierarchyConfig: PropTypes.exact({
        // 数据节点权重映射字段，默认为'value'
        field: PropTypes.string,

        // 设置是否忽略父节点实际权重，默认为true
        ignoreParentValue: PropTypes.bool
    }),

    // 配置下钻相关参数
    drilldown: PropTypes.exact({
        // 设置是否允许下钻交互，默认为true
        enabled: PropTypes.bool,

        // 配置层级面包屑相关参数
        breadCrumb: PropTypes.exact({
            // 设置根节点文案，默认：'Root'，中文默认：'根节点'
            rootText: PropTypes.string,

            // 设置面包屑分割文字，默认为'/'
            dividerText: PropTypes.string,

            // 设置面包屑字体样式
            textStyle: textBaseStyle,

            // 设置激活状态下的字体样式
            activeTextStyle: textBaseStyle,

            // 设置下钻层级面包屑的方位，可选的有'top-left'、'bottom-left'
            // 默认为'top-left'
            position: PropTypes.oneOf(['top-left', 'bottom-left'])
        })
    }),

    // 设置半径比例，取值应在0到1之间，默认为0.85
    radius: PropTypes.number,

    // 设置内径比例，取值应在0到1之间，默认为0
    innerRadius: PropTypes.number,

    // 用于手动设置调色方案，接受css中合法的所有颜色值，当传入单个字符串时，所有折线沿用此颜色值
    // 当传入数组时，会视作调色盘方案对seriesField区分的不同系列进行着色
    // 当传入对象时，会解析出其'func'属性对应的字符串，解析为函数，以支持更为自由的seriesField->色彩映射
    color: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            // 传入字符串形式的js函数体源码，例如
            // (ref) => {
            //     if (ref.series === '系列一'){
            //         return 'red'
            //     }
            //     return 'blue'
            // }
            func: PropTypes.string
        })
    ]),

    // // 设置图形的贴图样式
    // pattern: PropTypes.object,

    // 设置填充区域样式，其中透明度默认随着层级增加会逐渐减少填充透明度，可通过sunburstStyle
    // 自定义func回调来自主控制样式
    sunburstStyle: PropTypes.oneOfType([
        areaBaseStyle,
        PropTypes.exact({
            // 回调模式
            func: PropTypes.string
        })
    ]),

    // 设置是否进行径向反转，默认为false，当设置为true后旭日图将会以从外向内的方式进行层次的递进
    reflect: PropTypes.bool,

    // 配置文字标签相关参数
    label: labelBasePropTypes,

    // 设置tooltip相关参数
    tooltip: tooltipBasePropTypes,

    // 配置标注相关参数
    annotations: annotationsBasePropTypes,

    // 配置动画相关参数
    animation: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.bool
    ]),

    // 常用事件监听参数
    // tooltip显示事件
    recentlyTooltipChangeRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.any
    }),

    // 单独折线点击事件
    recentlyAreaClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.any
    }),

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
AntdSunburst.defaultProps = {
    reflect: false,
    downloadTrigger: 'download-trigger'
}