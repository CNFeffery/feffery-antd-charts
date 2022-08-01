/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Sankey } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { isUndefined, omitBy, intersection, cloneDeep } from 'lodash';
import {
    metaBasePropTypes,
    areaBaseStyle
} from './BasePropTypes.react';
import { difference } from './utils';

// 定义不触发重绘的参数数组
const preventUpdateProps = ['loading_state'];

// 定义桑基图组件AntdSankey，部分API参数参考https://charts.ant.design/zh/examples/relation-plots/sankey#alipay
export default class AntdSankey extends Component {

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
            sourceField,
            targetField,
            weightField,
            rawFields,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            nodeStyle,
            edgeStyle,
            color,
            nodeWidthRatio,
            nodePaddingRatio,
            nodeAlign,
            nodeDraggable,
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
            sourceField,
            targetField,
            weightField,
            rawFields,
            width,
            height,
            autoFit,
            padding,
            appendPadding,
            renderer,
            locale,
            nodeWidthRatio,
            nodePaddingRatio,
            nodeAlign,
            nodeDraggable
        }

        // 进阶参数
        // 桑基图节点样式
        config.nodeStyle = cloneDeep(nodeStyle)
        // 若nodeStyle具有自定义函数func属性
        if (nodeStyle?.func) {
            config.nodeStyle = eval(nodeStyle.func)
        }

        // 桑基图边样式
        config.edgeStyle = cloneDeep(edgeStyle)
        // 若edgeStyle具有自定义函数func属性
        if (edgeStyle?.func) {
            config.edgeStyle = eval(edgeStyle.func)
        }

        // 色彩样式
        config.color = cloneDeep(color)
        // 若color具有自定义函数func属性
        if (color?.func) {
            config.color = eval(color.func)
        }

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <Sankey
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
AntdSankey.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置和弦图绘图所需数据
    data: PropTypes.arrayOf(PropTypes.object),

    // 定义字段预处理元信息
    meta: metaBasePropTypes,

    // 设置作为和弦图来源节点的字段
    sourceField: PropTypes.string,

    // 设置作为和弦图目标节点的字段
    targetField: PropTypes.string,

    // 设置节点与边的权重字段，该数值越大，节点与边越大
    weightField: PropTypes.string,

    // 定义辅助用字段，以便于在tooltip、label等内容中显示
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

    // 配置桑基图节点样式
    nodeStyle: PropTypes.oneOfType([
        areaBaseStyle,
        PropTypes.exact({
            // 回调函数
            func: PropTypes.string
        })
    ]),

    // 配置桑基图边样式
    edgeStyle: PropTypes.oneOfType([
        areaBaseStyle,
        PropTypes.exact({
            // 回调函数
            func: PropTypes.string
        })
    ]),

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

    // 设置桑基图节点宽度比例，取值在0到1之间，以画布宽度为参考，默认为0.008
    nodeWidthRatio: PropTypes.number,

    // 设置桑基图节点之间垂直方向的间距比例，取值在0到1之间，以画布宽度为参考，默认为0.01
    nodePaddingRatio: PropTypes.number,

    // 设置桑基图节点的布局方式，可选的有'left'、'right'、'center'、'justify'，默认为'justify'
    nodeAlign: PropTypes.oneOf(['left', 'right', 'center', 'justify']),

    // 设置桑基图中的节点是否可拖拽调整位置，默认为false
    nodeDraggable: PropTypes.bool,

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

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
AntdSankey.defaultProps = {
}