/* eslint-disable no-inline-comments */
/* eslint-disable prefer-const */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
import React, { Suspense } from 'react';
import PropTypes from 'prop-types';
import {
    annotationsBasePropTypes,
    themeBasePropTypes,
    animationBasePropTypes,
    baseStyle
} from './BasePropTypes.react';

const LazyAntdRingProgress = React.lazy(() => import(/* webpackChunkName: "plots" */ '../fragments/plots/AntdRingProgress.react'));

/**
 * 进度环图组件AntdRingProgress
 */
const AntdRingProgress = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyAntdRingProgress {...props} />
        </Suspense>
    );
}

AntdRingProgress.propTypes = {
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
     * 当前进度实际值，取值应在`0`到`1`之间
     */
    percent: PropTypes.number.isRequired,

    /**
     * 外环半径尺寸，取值应在`0`到`1`之间
     */
    radius: PropTypes.number,

    /**
     * 内环半径尺寸，取值应在`0`到`1`之间
     */
    innerRadius: PropTypes.number,

    /**
     * 控制进度环形填充颜色，具体见在线文档相关说明
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
     * 控制进度环形样式，具体见在线文档相关说明
     */
    progressStyle: PropTypes.oneOfType([
        baseStyle,
        PropTypes.exact({
            /**
             * js函数体字符串
             */
            func: PropTypes.string
        })
    ]),

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
     * 配置标注相关参数，具体见在线文档相关说明
     */
    annotations: annotationsBasePropTypes,

    /**
     * 配置动画相关参数，具体见在线文档相关说明
     */
    animation: animationBasePropTypes,

    /**
     * 配置饼图中心统计内容，具体见在线文档相关说明
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
                        /**
                         * js函数体字符串
                         */
                        func: PropTypes.string
                    }),
                    /**
                     * 配置统计内容标题原始html文本内容
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
                        /**
                         * js函数体字符串
                         */
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
            style: baseStyle
        })
    ]),

    /**
     * 对当前组件的`downloadTrigger`值进行更新，可实现主动下载当前图表为`png`格式图片
     */
    downloadTrigger: PropTypes.string,

    /**
     * 配置主题相关参数，具体见在线文档相关说明
     */
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

AntdRingProgress.defaultProps = {
    locale: 'zh-CN',
    downloadTrigger: 'download-trigger'
}

export default AntdRingProgress;

export const propTypes = AntdRingProgress.propTypes;
export const defaultProps = AntdRingProgress.defaultProps;