/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    baseStyle
} from '../BasePropTypes.react';

const LazyAntdRadialTree = React.lazy(() => import(/* webpackChunkName: "graphs" */ '../../fragments/graphs/AntdRadialTree.react'));

/**
 * 辐射树图组件AntdRadialTree
 */
const AntdRadialTree = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdRadialTree {...props} />
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
     * css类名
     */
    className: PropTypes.string,

    /**
     * css样式
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

    // 设置图表是否自适应容器宽高，当设置为true时，width与height参数将失效，默认为true
    /**
     * 图表是否自适应容器宽高，设置为`true`时，`width`与`height`参数将失效
     * 默认值：`true`
     */
    autoFit: PropTypes.bool,

    /**
     * 配置节点相关参数
     */
    nodeCfg: PropTypes.exact({
        /**
         * 节点类型，可选项有`'icon-node'`、`'card'`、`'circle'`、`'rect'`、`'ellipse'`、`'diamond'`、`'triangle'`、
         * `'star'`、`'image'`、`'modelRect'`、`'donut'`
         */
        type: PropTypes.oneOf(['icon-node', 'card', 'circle', 'rect', 'ellipse', 'diamond', 'triangle', 'star', 'image', 'modelRect', 'donut']),

        // 设置节点最小尺寸，默认为[120, 40]
        /**
         * 节点最小像素尺寸，格式如：`[像素宽度, 像素高度]`
         * 默认值：`[100, 44]`
         */
        size: PropTypes.arrayOf(PropTypes.number),

        /**
         * 节点样式，支持`func`回调
         */
        style: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                /**
                 * 回调函数字符串
                 */
                func: PropTypes.string
            })
        ]),

        /**
         * 节点文本样式，支持`func`回调
         */
        label: PropTypes.exact({
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    /**
                     * 回调函数字符串
                     */
                    func: PropTypes.string
                })
            ])
        }),

        /**
         * 节点在不同状态下的样式
         */
        nodeStateStyles: PropTypes.objectOf(baseStyle)
    }),

    // 配置边
    edgeCfg: PropTypes.exact({
        /**
         * 边样式，支持`func`回调
         */
        style: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                /**
                 * 回调函数字符串
                 */
                func: PropTypes.string
            })
        ]),

        /**
         * 边类型，可选项有`'line'`、`'polyline'`、`'arc'`、`'quadratic'`、`'cubic'`、`'cubic-vertical'`、
         * `'cubic-horizontal'`、`'loop'`
         * 默认值：`'polyline'`
         */
        type: PropTypes.oneOf([
            'line', 'polyline', 'arc', 'quadratic', 'cubic',
            'cubic-vertical', 'cubic-horizontal', 'loop'
        ]),

        /**
         * 边文本样式，支持`func`回调
         */
        label: PropTypes.exact({
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    /**
                     * 回调函数字符串
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
         * 边在不同状态下的样式
         */
        edgeStateStyles: PropTypes.objectOf(baseStyle)
    }),

    /**
     * 启用的交互模式，可选项有`'drag-canvas'`（拖拽画布）、`'scroll-canvas'`（滚轮滚动画布）、
     * `'zoom-canvas'`（缩放画布）、`'drag-node'`（拖拽节点）、'click-select'（节点选择）
     * 默认值：`['drag-canvas', 'zoom-canvas']`
     */
    behaviors: PropTypes.arrayOf(
        PropTypes.oneOf(['drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node', 'click-select'])
    ),

    /**
     * 是否开启动画
     * 默认值：`false`
     */
    animate: PropTypes.bool,

    /**
     * 配置迷你图相关参数
     */
    minimapCfg: PropTypes.exact({
        /**
         * 是否开启迷你图
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
         * 迷你图像素尺寸，格式如：`[像素宽度, 像素高度]`
         */
        size: PropTypes.arrayOf(PropTypes.number),
        delegateStyle: baseStyle,
        refresh: PropTypes.bool,
        /**
         * 像素内边距
         */
        padding: PropTypes.number
    }),

    // 配置布局
    layout: PropTypes.exact({
        /**
         * 布局方向，可选项有`'TB'`、`'BT'`、`'LR'`、`'RL'`
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
     * 节点点击事件监听
     */
    recentlyNodeClickRecord: PropTypes.exact({
        /**
         * 事件触发时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 事件对应节点信息，点击空白处时为空[]
         */
        data: PropTypes.object
    }),

    /**
     * 节点双击事件监听
     */
    recentlyNodeDoubleClickRecord: PropTypes.exact({
        /**
         * 事件触发时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 事件对应节点信息，点击空白处时为空
         */
        data: PropTypes.object
    }),

    /**
     * 节点选中事件监听，需要在``behaviors``中开启``click-select``
     */
    selectedNodes: PropTypes.exact({
        /**
         * 事件触发时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 对应选中的节点信息数组
         */
        data: PropTypes.array
    }),

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
AntdRadialTree.defaultProps = {
    autoFit: true,
    behaviors: ['drag-canvas', 'zoom-canvas'],
    animate: false,
}

export default AntdRadialTree;

export const propTypes = AntdRadialTree.propTypes;
export const defaultProps = AntdRadialTree.defaultProps;