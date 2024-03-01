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

const AntdFundFlow = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdFundFlow {...props} />
        </Suspense>
    );
}


// 定义参数或属性
AntdFundFlow.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 辅助强制刷新
    key: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置指标拆解图绘图所需数据
    data: PropTypes.object.isRequired,

    // 定义图表容器像素宽度，默认为500
    width: PropTypes.number,

    // 定义图表容器像素高度，默认为500
    height: PropTypes.number,

    // 设置图表是否自适应容器宽高，当设置为true时，width与height参数将失效，默认为true
    autoFit: PropTypes.bool,

    // 配置节点
    nodeCfg: PropTypes.exact({
        // 设置节点类型，可选的有'fund-card'
        type: PropTypes.oneOf(['fund-card']),

        // 设置节点最小尺寸，默认为[120, 40]
        size: PropTypes.arrayOf(PropTypes.number),

        // 设置节点样式，支持func回调
        style: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                // 传入回调函数字符串
                func: PropTypes.string
            })
        ]),

        // 设置节点文本样式，支持回调
        label: PropTypes.exact({
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    // 传入回调函数字符串
                    func: PropTypes.string
                })
            ])
        }),

        // 设置边在节点上的锚点位置，默认为[[0.5, 0], [0.5, 1]]
        anchorPoints: PropTypes.arrayOf(
            PropTypes.arrayOf(PropTypes.number)
        ),

        // 配置节点标题
        title: PropTypes.exact({
            // 设置容器样式
            containerStyle: baseStyle,

            // 设置标题样式
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    // 传入回调函数字符串
                    func: PropTypes.string
                })
            ]),

            // 设置文字超出范围是否自动隐藏
            autoEllipsis: PropTypes.bool
        }),

        // 配置节点内容
        items: PropTypes.exact({
            // 设置节点内容容器样式
            containerStyle: baseStyle,

            // 设置节点内容样式
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    // 传入回调函数字符串
                    func: PropTypes.string
                })
            ]),

            // 设置布局方式，可选的有'bundled'、'flex'、'follow'
            // 默认为'bundled'
            layout: PropTypes.oneOf(['bundled', 'flex', 'follow']),

            // 设置是否根据节点顺序绘制
            sort: PropTypes.bool,

            // 设置节点内容容器填充
            padding: PropTypes.oneOfType([
                PropTypes.number,
                PropTypes.arrayOf(PropTypes.number)
            ])
        }),

        // 设置文本填充
        padding: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.arrayOf(PropTypes.number)
        ]),

        // 配置节点状态，其中style支持回调
        badge: PropTypes.exact({
            // 设置标记位置，可选的有'left'、'top'、'right'、'bottom'
            position: PropTypes.oneOf(['left', 'top', 'right', 'bottom']),

            // 设置标记大小
            size: PropTypes.oneOfType([
                PropTypes.number,
                PropTypes.arrayOf(PropTypes.number)
            ]),

            // 设置标记样式
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    // 传入回调函数字符串
                    func: PropTypes.string
                })
            ])
        }),

        // 配置节点占比，其中style支持回调
        percent: PropTypes.exact({
            // 设置占比位置，可选的有'top'、'bottom'
            position: PropTypes.oneOf(['top', 'bottom']),

            // 设置背景高度
            size: PropTypes.number,

            // 设置占比样式
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    // 传入回调函数字符串
                    func: PropTypes.string
                })
            ]),

            // 设置占比背景样式
            backgroundStyle: baseStyle
        }),

        // 设置是否动态调整节点宽度
        autoWidth: PropTypes.bool,

        // 配置节点在不同状态下的样式，可用的状态有
        // 'hover'
        nodeStateStyles: PropTypes.oneOfType([
            PropTypes.objectOf(
                baseStyle
            ),
            PropTypes.bool
        ])
    }),

    // 配置边
    edgeCfg: PropTypes.exact({
        // 设置边类型，可选的有'line'、'polyline'、'arc'、'quadratic'
        // 'cubic'、'cubic-vertical'、'cubic-horizontal'、'loop'
        // 默认为'cubic-horizontal'
        type: PropTypes.oneOf([
            'line', 'polyline', 'arc', 'quadratic', 'cubic',
            'cubic-vertical', 'cubic-horizontal', 'loop'
        ]),

        // 设置边文本的样式，style支持回调
        label: PropTypes.exact({
            style: PropTypes.oneOfType([
                baseStyle,
                PropTypes.exact({
                    // 传入回调函数字符串
                    func: PropTypes.string
                })
            ])
        }),

        // 配置边开始箭头样式
        startArrow: PropTypes.exact({
            // 设置箭头类型，可选的有'vee'、'triangle'
            type: PropTypes.oneOf(['vee', 'triangle']),

            // 设置像素偏移量
            d: PropTypes.number,

            // 设置绘制路径
            path: PropTypes.string,

            // 设置描边色
            stroke: PropTypes.string,

            // 设置填充色
            fill: PropTypes.string
        }),

        // 配置边结束箭头样式
        endArrow: PropTypes.exact({
            // 设置填充色
            fill: PropTypes.string,

            // 设置是否展示结束箭头
            show: PropTypes.bool
        }),

        // 配置边在不同状态下的样式，可用的状态有
        // 'hover'
        edgeStateStyles: PropTypes.oneOfType([
            PropTypes.objectOf(
                baseStyle
            ),
            PropTypes.bool
        ]),

        // 配置边样式，支持回调
        style: PropTypes.oneOfType([
            baseStyle,
            PropTypes.exact({
                // 传入回调函数字符串
                func: PropTypes.string
            })
        ])
    }),

    // 配置启用的交互模式，可选的有'drag-canvas'、'scroll-canvas'、'zoom-canvas'、'drag-node'
    // 默认为['drag-canvas', 'zoom-canvas']
    behaviors: PropTypes.arrayOf(
        PropTypes.oneOf(['drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node'])
    ),

    // 配置marker，支持回调
    markerCfg: PropTypes.oneOfType([
        PropTypes.exact({
            // 设置是否展示
            show: PropTypes.bool,

            // 设置是否显示折叠状态
            collapsed: PropTypes.bool,

            // 设置位置，可选的有'left'、'right'、'top'、'bottom'
            position: PropTypes.oneOf(['left', 'right', 'top', 'bottom']),

            // 设置样式
            style: baseStyle
        }),
        PropTypes.exact({
            func: PropTypes.string
        })
    ]),

    // 配置迷你图
    minimapCfg: PropTypes.exact({
        // 设置是否展示迷你图，默认为false
        show: PropTypes.bool,

        // 设置迷你图class类名
        viewportClassName: PropTypes.string,

        // 设置迷你图类型，可选的有'default'、'keyShape'、'delegate'
        type: PropTypes.oneOf(['default', 'keyShape', 'delegate']),

        // 设置尺寸
        size: PropTypes.arrayOf(PropTypes.number),

        delegateStyle: baseStyle,

        refresh: PropTypes.bool,

        // 设置填充
        padding: PropTypes.number
    }),

    // 配置布局
    layout: PropTypes.exact({
        // 设置节点垂直方向像素间隔大小
        nodesep: PropTypes.number,

        // 设置节点水平方向像素间隔大小
        ranksep: PropTypes.number
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
AntdFundFlow.defaultProps = {
}

export default AntdFundFlow;

export const propTypes = AntdFundFlow.propTypes;
export const defaultProps = AntdFundFlow.defaultProps;