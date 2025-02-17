/* eslint-disable no-inline-comments */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import { useLoading } from './utils';
import {
    baseStyle,
    themeBasePropTypes,
    patternBasePropTypes,
    animationBasePropTypes,
    interactionsBasePropTypes,
    stateBasePropTypes
} from './BasePropTypes.react';

const LazyAntdLiquid = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdLiquid.react'));

/**
 * 水波图组件AntdLiquid
 */
const AntdLiquid = ({
    locale = 'zh-CN',
    downloadTrigger = 'download-trigger',
    radius = 0.9,
    shape = 'circle',
    ...others
}) => {

    const component_loading = useLoading();

    return (
        <Suspense fallback={null}>
            <LazyAntdLiquid {
                ...{
                    locale,
                    downloadTrigger,
                    radius,
                    shape,
                    component_loading,
                    ...others
                }
            } />
        </Suspense>
    );
}

AntdLiquid.propTypes = {
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
     * css样式
     */
    style: PropTypes.object,

    /**
     * 当前水波图实际值，取值应在`0`到`1`之间
     */
    percent: PropTypes.number.isRequired,

    /**
     * 水波图相对画布的外环半径尺寸，取值应在`0`到`1`之间
     * 默认值：`0.9`
     */
    radius: PropTypes.number,

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
     * 画布内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组，或传入`'auto'`开启底层自动计算
     */
    padding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
        PropTypes.oneOf(['auto'])
    ]),

    /**
     * 画布额外内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组
     */
    appendPadding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number)
    ]),

    /**
     * 图表底层渲染方式，可选项有`'canvas'`和`'svg'`
     * 默认值：`'canvas'`
     */
    renderer: PropTypes.oneOf(['canvas', 'svg']),

    /**
     * `renderer='canvas'`时，控制渲染图表图片的像素比
     * 默认值：`1`
     */
    pixelRatio: PropTypes.number,

    /**
     * 图表文案语种，可选项有`'zh-CN'`、`'en-US'`
     * 默认值：`'zh-CN'`
     */
    locale: PropTypes.oneOf(['zh-CN', 'en-US']),

    /**
     * 是否对超出绘图区域的几何元素进行裁剪
     */
    limitInPlot: PropTypes.bool,

    /**
     * 控制水波图样式，具体见在线文档相关说明
     */
    liquidStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
     * 水波图形状，可选项有`'circle'`、`'diamond'`、`'triangle'`、`'pin'`、`'rect'
     * 默认值：`'circle'`
     */
    shape: PropTypes.oneOf([
        'circle', 'diamond', 'triangle', 'pin', 'rect'
    ]),

    /**
     * 控制水波图颜色，具体见在线文档相关说明
     */
    color: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

    /**
     * 配置水波图外轮廓，具体见在线文档相关说明
     */
    outline: PropTypes.exact({
        /**
         * 水波图外轮廓像素宽度
         * 默认值：`2`
         */
        border: PropTypes.number,
        /**
         * 水波图外轮廓与内部波形之间的像素间距
         * 默认值：`0`
         */
        distance: PropTypes.number,
        /**
         * 配置水波图外轮廓
         */
        style: PropTypes.exact({
            /**
             * 外轮廓填充色
             */
            stroke: PropTypes.string,
            /**
             * 外轮廓填充透明度
             */
            strokeOpacity: PropTypes.number
        })
    }),

    /**
     * 配置水波图波形，具体见在线文档相关说明
     */
    wave: PropTypes.exact({
        /**
         * 水波数量
         * 默认值：`3`
         */
        count: PropTypes.number,
        /**
         * 水波像素长度
         * 默认值：`192`
         */
        length: PropTypes.number
    }),

    /**
     * 配置水波图中心统计内容，具体见在线文档相关说明
     */
    statistic: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.exact({
            /**
             * 配置统计内容标题，设置为`False`时将隐藏标题
             */
            title: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 统计内容标题样式
                     */
                    style: PropTypes.object,
                    /**
                     * 配置统计内容标题文本
                     */
                    content: PropTypes.string,
                    /**
                     * 格式化统计内容标题文本函数
                     */
                    formatter: PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string
                    }),
                    /**
                     * 配置统计内容标题原始html文本内容
                     */
                    customHtml: PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string
                    }),
                    /**
                     * 标题旋转角度
                     */
                    rotate: PropTypes.number,
                    /**
                     * 标题水平像素偏移
                     */
                    offsetX: PropTypes.number,
                    /**
                     * 标题竖直像素偏移
                     */
                    offsetY: PropTypes.number
                })
            ]),
            /**
             * 配置统计内容，设置为`False`时将隐藏内容
             */
            content: PropTypes.oneOfType([
                PropTypes.bool,
                PropTypes.exact({
                    /**
                     * 统计内容样式
                     */
                    style: PropTypes.object,
                    /**
                     * 配置统计内容文本
                     */
                    content: PropTypes.string,
                    /**
                     * 格式化统计内容文本函数
                     */
                    formatter: PropTypes.exact({
                        // 回调模式
                        func: PropTypes.string
                    }),
                    /**
                     * 配置统计内容原始html文本内容
                     */
                    customHtml: PropTypes.exact({
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string
                    }),
                    /**
                     * 标题旋转角度
                     */
                    rotate: PropTypes.number,
                    /**
                     * 标题水平像素偏移
                     */
                    offsetX: PropTypes.number,
                    /**
                     * 标题竖直像素偏移
                     */
                    offsetY: PropTypes.number
                })
            ]),
        })
    ]),

    /**
     * 配置动画相关参数，具体见在线文档相关说明
     */
    animation: animationBasePropTypes,

    /**
     * 对当前组件的`downloadTrigger`值进行更新，可实现主动下载当前图表为`png`格式图片
     */
    downloadTrigger: PropTypes.string,

    /**
     * 配置主题相关参数，具体见在线文档相关说明
     */
    theme: themeBasePropTypes,

    /**
     * 配置图形填充贴图相关参数，具体见在线文档相关说明
     */
    pattern: patternBasePropTypes,

    /**
     * 配置交互功能相关参数，具体见在线文档相关说明
     */
    interactions: interactionsBasePropTypes,

    /**
     * 配置状态样式相关参数，具体见在线文档相关说明
     */
    state: stateBasePropTypes,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default AntdLiquid;

export const propTypes = AntdLiquid.propTypes;
export const defaultProps = AntdLiquid.defaultProps;