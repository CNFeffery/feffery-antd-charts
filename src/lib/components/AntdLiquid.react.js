/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Liquid } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import {
    areaBaseStyle,
    themeBasePropTypes
} from './BasePropTypes.react';
import { difference } from './utils';

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
            locale,
            limitInPlot,
            shape,
            outline,
            wave,
            theme
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

// 定义参数或属性
AntdLiquid.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置当前水波图百分比，必填
    percent: PropTypes.number.isRequired,

    // 设置水波图相对画布的外环半径大小，取值应在0~1之间，默认为0.9
    radius: PropTypes.number,

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

    // 配置水波图样式
    liquidStyle: PropTypes.oneOfType([
        areaBaseStyle,
        PropTypes.exact({
            // 回调函数
            func: PropTypes.string
        })
    ]),

    // 设置水波图形状类型，可选的有'circle'、'diamond'、'triangle'、'pin'
    // 'rect'，默认为'circle'
    shape: PropTypes.oneOf([
        'circle', 'diamond', 'triangle', 'pin', 'rect'
    ]),

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

    // 配置水波图外轮廓
    outline: PropTypes.exact({
        // 设置水波图外轮廓像素宽度，默认为2
        border: PropTypes.number,
        // 设置水波图外轮廓与内部波形之间的像素间距，默认为0
        distance: PropTypes.number,
        // 设置水波图外轮廓样式
        style: PropTypes.exact({
            // 设置外轮廓填充色，默认为与color一致
            stroke: PropTypes.string,
            // 设置外轮廓填充透明度
            strokeOpacity: PropTypes.number
        })
    }),

    // 配置水波图的波形
    wave: PropTypes.exact({
        // 设置水波的数量，默认为3
        count: PropTypes.number,
        // 设置水波的像素波长度，默认为192
        length: PropTypes.number
    }),

    // 配置水波图中心文本内容
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
AntdLiquid.defaultProps = {
    radius: 0.9,
    shape: 'circle',
    downloadTrigger: 'download-trigger'
}