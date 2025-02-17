/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import { useLoading } from '../utils';
import {
    baseStyle
} from '../BasePropTypes.react';

const LazyAntdRadialTree = React.lazy(() => import(/* webpackChunkName: "graphs" */ '../../fragments/graphs/AntdRadialTree.react'));

/**
 * 辐射树图组件AntdRadialTree
 */
const AntdRadialTree = ({
    autoFit = true,
    behaviors = ['drag-canvas', 'zoom-canvas'],
    animate = false,
    ...others
}) => {

    const component_loading = useLoading();

    return (
        <Suspense fallback={null}>
            <LazyAntdRadialTree {
                ...{
                    autoFit,
                    behaviors,
                    animate,
                    component_loading,
                    ...others
                }
            } />
        </Suspense>
    );
}

AntdRadialTree.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 必填，定义绘图所需数据
     */
    data: PropTypes.object.isRequired,

    /**
     * 图表容器像素宽度
     */
    width: PropTypes.number,

    /**
     * 图表容器像素高度
     */
    height: PropTypes.number,

    /**
     * 图表是否自适应所在父容器宽高，当`autoFit=True`时，`width`和`height`参数将失效
     * 默认值：`true`
     */
    autoFit: PropTypes.bool,

    /**
     * 配置节点相关参数，具体见在线文档相关说明
     */
    nodeCfg: PropTypes.exact({
        /**
         * 节点类型，可选项有`'icon-node'`、`'card'`、`'circle'`、`'rect'`、`'ellipse'`、`'diamond'`、`'triangle'`、`'star'`、`'image'`、`'modelRect'`、`'donut'`
         */
        type: PropTypes.oneOf(['icon-node', 'card', 'circle', 'rect', 'ellipse', 'diamond', 'triangle', 'star', 'image', 'modelRect', 'donut']),
        /**
         * 节点像素尺寸范围
         * 默认值：`[100, 44]`
         */
        size: PropTypes.arrayOf(PropTypes.number),
        /**
         * 节点样式
         */
        style: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            })
        ]),
        /**
         * 节点文本样式
         */
        label: PropTypes.exact({
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    /**
                     * js函数体字符串
                     */
                    func: PropTypes.string
                })
            ])
        }),
        /**
         * 配置节点不同状态下的样式，可用的状态有`'hover'`
         */
        nodeStateStyles: PropTypes.objectOf(baseStyle)
    }),

    /**
     * 配置边相关参数，具体见在线文档相关说明
     */
    edgeCfg: PropTypes.exact({
        /**
         * 边样式
         */
        style: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                /**
                 * js函数体字符串
                 */
                func: PropTypes.string
            })
        ]),
        /**
         * 边类型，可选项有`'line'`、`'polyline'`、`'arc'`、`'quadratic'`、`'cubic'`、`'cubic-vertical'`、`'cubic-horizontal'`、`'loop'`
         * 默认值：`'cubic-horizontal'`
         */
        type: PropTypes.oneOf([
            'line', 'polyline', 'arc', 'quadratic', 'cubic',
            'cubic-vertical', 'cubic-horizontal', 'loop'
        ]),
        /**
         * 边文本样式
         */
        label: PropTypes.exact({
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    /**
                     * js函数体字符串
                     */
                    func: PropTypes.string
                })
            ])
        }),
        /**
         * 配置边开始箭头
         */
        startArrow: PropTypes.exact({
            /**
             * 箭头类型，可选项有`'vee'`、`'triangle'`
             */
            type: PropTypes.oneOf(['vee', 'triangle']),
            /**
             * 箭头像素尺寸
             */
            size: PropTypes.number,
            /**
             * 像素偏移量
             */
            d: PropTypes.number,
            /**
             * 绘制路径
             */
            path: PropTypes.string,
            /**
             * 轮廓色
             */
            stroke: PropTypes.string,
            /**
             * 填充色
             */
            fill: PropTypes.string
        }),
        /**
         * 配置边结束箭头
         */
        endArrow: PropTypes.exact({
            /**
             * 箭头类型，可选项有`'vee'`、`'triangle'`
             */
            type: PropTypes.oneOf(['vee', 'triangle']),
            /**
             * 箭头像素尺寸
             */
            size: PropTypes.number,
            /**
             * 像素偏移量
             */
            d: PropTypes.number,
            /**
             * 绘制路径
             */
            path: PropTypes.string,
            /**
             * 轮廓色
             */
            stroke: PropTypes.string,
            /**
             * 填充色
             */
            fill: PropTypes.string
        }),
        /**
         * 配置边不同状态下的样式，可用的状态有`'hover'`
         */
        edgeStateStyles: PropTypes.objectOf(baseStyle)
    }),

    /**
     * 配置要启用的交互模式，支持多选，可选项有`'drag-canvas'`、`'scroll-canvas'`、`'zoom-canvas'`、`'drag-node'`、`'click-select'`
     * 默认值：`['drag-canvas', 'zoom-canvas']`
     */
    behaviors: PropTypes.arrayOf(
        PropTypes.oneOf(['drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node', 'click-select'])
    ),

    /**
     * 是否启用动画效果
     * 默认值：`true`
     */
    animate: PropTypes.bool,

    /**
     * 配置迷你图相关参数，具体见在线文档
     */
    minimapCfg: PropTypes.exact({
        /**
         * 是否展示迷你图
         * 默认值：`false`
         */
        show: PropTypes.bool,
        /**
         * 迷你图css类名
         */
        viewportClassName: PropTypes.string,
        /**
         * 迷你图类型，可选项有`'default'`、`'keyShape'`、`'delegate'`
         */
        type: PropTypes.oneOf(['default', 'keyShape', 'delegate']),
        /**
         * 配置迷你图像素尺寸，格式如`[宽度, 高度]`
         */
        size: PropTypes.arrayOf(PropTypes.number),
        /**
         * 内填充像素尺寸
         */
        padding: PropTypes.number
    }),

    /**
     * 配置布局相关参数，具体见在线文档
     */
    layout: PropTypes.exact({
        /**
         * 布局方式，可选项有`'TB'`、`'BT'`、`'LR'`、`'RL'`
         */
        direction: PropTypes.oneOf(['TB', 'BT', 'LR', 'RL']),
        /**
         * 节点垂直方向像素间隔大小
         */
        nodesep: PropTypes.number,
        /**
         * 节点水平方向像素间隔大小
         */
        ranksep: PropTypes.number
    }),

    /**
     * 事件监听属性，用于监听最近一次节点点击事件
     */
    recentlyNodeClickRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.object
    }),

    /**
     * 事件监听属性，用于监听最近一次节点双击事件
     */
    recentlyNodeDoubleClickRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.object
    }),

    /**
     * 事件监听属性，用于监听最近一次边点击事件
     */
    recentlyEdgeClickRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.object
    }),

    /**
     * 事件监听属性，用于监听最近一次边双击事件
     */
    recentlyEdgeDoubleClickRecord: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.object
    }),

    /**
     * 事件监听属性，用于监听最近一次节点选中事件，需要在``behaviors``中开启``click-select``
     */
    selectedNodes: PropTypes.exact({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 涉及数据信息
         */
        data: PropTypes.array
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default AntdRadialTree;

export const propTypes = AntdRadialTree.propTypes;
export const defaultProps = AntdRadialTree.defaultProps;