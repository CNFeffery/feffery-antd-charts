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

const LazyAntdFundFlow = React.lazy(() => import(/* webpackChunkName: "graphs" */ '../../fragments/graphs/AntdFundFlow.react'));

/**
 * 资金流向图组件AntdFundFlow
 */
const AntdFundFlow = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdFundFlow {...props} />
        </Suspense>
    );
}

AntdFundFlow.propTypes = {
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
         * 节点类型，可选项有`'fund-card'`
         */
        type: PropTypes.oneOf(['fund-card']),
        /**
         * 节点像素尺寸范围
         * 默认值：`[120, 40]`
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
         * 边相对于节点的锚点位置
         * 默认值：`[[0.5, 0], [0.5, 1]]`
         */
        anchorPoints: PropTypes.arrayOf(
            PropTypes.arrayOf(PropTypes.number)
        ),
        /**
         * 配置节点标题
         */
        title: PropTypes.exact({
            /**
             * 标题容器样式
             */
            containerStyle: baseStyle,
            /**
             * 标题样式
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
             * 文本是否超出范围后自动隐藏
             */
            autoEllipsis: PropTypes.bool
        }),
        /**
         * 配置节点内容
         */
        items: PropTypes.exact({
            /**
             * 节点内容容器样式
             */
            containerStyle: baseStyle,
            /**
             * 节点内容样式
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
             * 布局方式，可选项有`'bundled'`、`'flex'`、`'follow'`
             * 默认值：`'bundled'`
             */
            layout: PropTypes.oneOf(['bundled', 'flex', 'follow']),
            /**
             * 是否按照节点顺序渲染
             */
            sort: PropTypes.bool,
            /**
             * 节点内容容器填充
             */
            padding: PropTypes.oneOfType([
                PropTypes.number,
                PropTypes.arrayOf(PropTypes.number)
            ])
        }),
        /**
         * 文本填充
         */
        padding: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number)
        ]),
        /**
         * 配置节点标记
         */
        badge: PropTypes.exact({
            /**
             * 标记位置，可选项有`'left'`、`'top'`、`'right'`、`'bottom'`
             */
            position: PropTypes.oneOf(['left', 'top', 'right', 'bottom']),
            /**
             * 标记尺寸
             */
            size: PropTypes.oneOfType([
                PropTypes.number,
                PropTypes.arrayOf(PropTypes.number)
            ]),
            /**
             * 标记样式
             */
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
         * 配置节点占比内容
         */
        percent: PropTypes.exact({
            /**
             * 占比内容位置，可选项有`'top'`、`'bottom'`
             */
            position: PropTypes.oneOf(['top', 'bottom']),
            /**
             * 占比内容背景像素高度
             */
            size: PropTypes.number,
            /**
             * 占比内容样式
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
             * 占比内容背景样式
             */
            backgroundStyle: baseStyle
        }),
        /**
         * 是否动态调整节点宽度
         */
        autoWidth: PropTypes.bool,
        /**
         * 配置节点不同状态下的样式，可用的状态有`'hover'`
         */
        nodeStateStyles: PropTypes.oneOfType([
            PropTypes.objectOf(
                baseStyle
            ),
            PropTypes.bool
        ])
    }),

    /**
     * 配置边相关参数，具体见在线文档相关说明
     */
    edgeCfg: PropTypes.exact({
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
             * 像素偏移量
             */
            d: PropTypes.number,
            /**
             * 绘制路径
             */
            path: PropTypes.string,
            /**
             * 描边色
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
             * 填充色
             */
            fill: PropTypes.string,
            /**
             * 是否展示结束箭头
             */
            show: PropTypes.bool
        }),
        /**
         * 配置边不同状态下的样式，可用的状态有`'hover'`
         */
        edgeStateStyles: PropTypes.oneOfType([
            PropTypes.objectOf(
                baseStyle
            ),
            PropTypes.bool
        ]),
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
        ])
    }),

    /**
     * 配置要启用的交互模式，支持多选，可选项有`'drag-canvas'`、`'scroll-canvas'`、`'zoom-canvas'`、`'drag-node'`、`'click-select'`
     * 默认值：`['drag-canvas', 'zoom-canvas']`
     */
    behaviors: PropTypes.arrayOf(
        PropTypes.oneOf(['drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node'])
    ),

    /**
     * 配置标记相关参数，具体见在线文档
     */
    markerCfg: PropTypes.oneOfType([
        PropTypes.exact({
            /**
             * 是否展示标记
             */
            show: PropTypes.bool,
            /**
             * 是否显示为折叠状态
             */
            collapsed: PropTypes.bool,
            /**
             * 标记位置，可选项有`'left'`、`'right'`、`'top'`、`'bottom'`
             */
            position: PropTypes.oneOf(['left', 'right', 'top', 'bottom']),
            /**
             * 标记样式
             */
            style: baseStyle
        }),
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

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
         * 节点垂直方向像素间隔
         */
        nodesep: PropTypes.number,
        /**
         * 节点水平方向像素间隔
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

AntdFundFlow.defaultProps = {}

export default AntdFundFlow;

export const propTypes = AntdFundFlow.propTypes;
export const defaultProps = AntdFundFlow.defaultProps;