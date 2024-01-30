/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    metaBasePropTypes,
    areaBaseStyle,
    themeBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes
} from './BasePropTypes.react';

const LazyAntdSankey = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdSankey.react'));

const AntdSankey = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdSankey {...props} />
        </Suspense>
    );
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

    // 设置是否对超出绘图区域的几何元素进行裁剪
    limitInPlot: PropTypes.bool,

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

    // 配置动画相关参数
    animation: animationBasePropTypes,

    // 常用事件监听参数
    // tooltip显示事件
    recentlyTooltipChangeRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.arrayOf(PropTypes.object)
    }),

    // 单独区域点击事件
    recentlyAreaClickRecord: PropTypes.exact({
        // 事件触发的时间戳信息
        timestamp: PropTypes.number,

        // 对应的数据点信息
        data: PropTypes.object
    }),

    // 用于在回调中传入uuid、ulid之类的唯一标识，来主动下载当前图表为png格式图片
    downloadTrigger: PropTypes.string,

    // 主题配置
    theme: themeBasePropTypes,

    /**
     * 交互功能项配置
     */
    interactions: interactionsBasePropTypes,

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
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdSankey;

export const propTypes = AntdSankey.propTypes;
export const defaultProps = AntdSankey.defaultProps;