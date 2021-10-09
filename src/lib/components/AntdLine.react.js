import { Line } from '@ant-design/charts';
import React, { Component } from 'react';
import PropTypes from 'prop-types';

// 定义折线图组件AntdLine，部分API参数参考https://charts.ant.design/zh-CN/demos/line
export default class AntdLine extends Component {
    render() {
        // 取得必要属性或参数
        let {
            id,
            className,
            style,
            data,
            xField,
            yField,
            seriesField,
            smooth,
            stepType,
            connectNulls,
            isStack,
            color,
            lineStyle,
            point,
            width,
            height,
            autoFit,
            padding,
            renderer,
            locale,
            legend,
            setProps
        } = this.props;


        let config = {
            data: data,
            padding: 'auto',
            xField: xField,
            yField: yField,
            seriesField: seriesField,
            smooth: smooth,
            stepType: stepType,
            connectNulls: connectNulls,
            isStack: isStack,
            width: width,
            height: height,
            autoFit: autoFit,
            padding: padding,
            renderer: renderer,
            locale: locale,
            xAxis: { tickCount: 5 }
        };

        // 进阶参数
        if (color) {
            config.color = color?.func ? eval(color?.func) : color
        }

        if (lineStyle) {
            config.lineStyle = typeof lineStyle === typeof '' ? eval(lineStyle) : lineStyle
        }

        if (point) {
            config.point = {
                color: point?.color?.func ? eval(point?.color?.func) : point?.color,

                shape: point?.shape?.func ? eval(point?.shape?.func) : point?.shape,

                size: point?.size?.func ? eval(point?.size?.func) : point?.size
            }
        }

        if (legend) {
            config.legend = legend
        }

        return <Line id={id}
            className={className}
            style={style}
            {...config} />;
    }
}

// 定义参数或属性
AntdLine.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 定义绘图所需数据，必须参数
    data: PropTypes.arrayOf(PropTypes.object).isRequired,

    // 定义作为x轴的字段名
    xField: PropTypes.string.isRequired,

    // 定义作为y轴的字段名
    yField: PropTypes.string.isRequired,

    // 定义作为分组依据的字段名
    seriesField: PropTypes.string,

    // 设置是否以平滑曲线方式渲染折线，默认为false
    smooth: PropTypes.bool,

    // 对应阶梯折线图类型的阶梯曲折方式，可选的有'hv'、'vh'、'hvh'及'vhv'
    // 其中'h'表示horizontal，'v'表示vertical，譬如`vh`就代表先竖直方向再水平方向
    stepType: PropTypes.string,

    // 设置针对折线图中缺失值的绘制策略，true表示连接，false表示断开，默认为true
    connectNulls: PropTypes.bool,

    // 在存在seriesField分组字段时，用于设置是否将折线堆叠起来，默认为false
    isStack: PropTypes.bool,

    // 用于手动设置调色方案，接受css中合法的所有颜色值，当传入单个字符串时，所有折线沿用此颜色值
    // 当传入数组时，会视作调色盘方案对seriesField区分的不同系列进行着色
    // 当传入对象时，会解析出其'func'属性对应的字符串，解析为函数，以支持更为自由的seriesField->色彩映射
    color: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.exact({
            // 传入字符串形式的js函数体源码，例如
            // (type) => {
            //     if (type === 'a'){
            //         return 'red'
            //     }
            //     return 'yellow'
            // }
            func: PropTypes.string
        })
    ]),

    // 用于设置折线样式，常规方式下接受对象用于设置全局折线样式
    // 亦可传入字符串对应的js函数体，实现针对不同seriesField返回不同样式，例如
    // (ref) => {
    //     if (ref.seriesField === 'a'){
    //         return {
    //             lineDash: [4, 4],
    //             opacity: 1,
    //           };
    //     }
    //     return { opacity: 0.5 };
    // }
    lineStyle: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.exact({
            // 设置图形描边的宽度
            lineWidth: PropTypes.number,

            // 设置描边的虚线配置，第一个值为虚线每个分段的长度，第二个值为分段间隔的距离。lineDash 设为[0,0]的效果为没有描边
            lineDash: PropTypes.arrayOf(PropTypes.number),

            // 设置描边的透明度
            lineOpacity: PropTypes.number,

            // 设置图形阴影颜色
            shadowColor: PropTypes.string,

            // 设置图形阴影的高斯模糊系数
            shadowBlur: PropTypes.number,

            // 设置阴影距图形的水平距离
            shadowOffsetX: PropTypes.number,

            // 设置阴影距图形的垂直距离
            shadowOffsetY: PropTypes.number,

            // 设置鼠标样式，同 css 的鼠标样式，默认 'default'
            cursor: PropTypes.string
        })
    ]),


    // 用于设置折线图折点的样式
    point: PropTypes.exact({
        // 设置折点颜色，支持单字符串、字符串数组以及对象传入func定义js函数体，函数格式同lineStyle
        color: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.arrayOf(PropTypes.string),
            PropTypes.exact({
                func: PropTypes.string
            })
        ]),

        // 设置折点形状，支持单字符串或对象传入func定义js函数体，函数格式同lineStyle
        // 单字符时可选的样式有'circle'、'square'、'line'、'diamond'、'triangle'、'triangle-down'、'hexagon'、
        // 'bowtie'、'cross'、'tick'、'plus'及'hyphen'
        shape: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.exact({
                func: PropTypes.string
            })
        ]),

        // 设置折点尺寸像素大小，支持单数值或对象传入func定义js函数体，函数格式同lineStyle
        size: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.exact({
                func: PropTypes.string
            })
        ])
    }),

    // 定义图表容器像素宽度，默认为400
    width: PropTypes.number,

    // 定义图表容器像素高度，默认为400
    height: PropTypes.number,

    // 设置图表是否自适应容器宽高，当设置为true时，width与height参数将失效，默认为true
    autoFit: PropTypes.bool,

    // 定义图表四个方向的空白间距值，可以为单个数字譬如16，也可以为四个数字构成的数组，按顺序代表上-右-下-左分别的像素间距
    padding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number)
    ]),

    // 设置图表渲染方式为'canvas'或'svg'模式，默认为'canvas'
    renderer: PropTypes.string,

    // 设置语言，可选的有'zh-CN'与'en-US'
    locale: PropTypes.string,

    // 配置图例相关参数
    legend: PropTypes.oneOfType([
        PropTypes.exact({
            // 设置图例位置，可选的有'top'、'top-left'、'top-right'、'left'、'left-top'、
            // 'left-bottom'、'right'、'right-top'、'right-bottom'、'bottom'、'bottom-left'及'bottom-right'
            position: PropTypes.string,

            // 设置图例布局方式，可选的有'horizontal'及'vertical'
            layout: PropTypes.string,

            // 设置图例整体在x方向上的偏移
            offsetX: PropTypes.number,

            // 设置图例整体在y方向上的偏移
            offsetY: PropTypes.number,

            // 配置背景框
            background: PropTypes.exact({
                // 设置背景框内部留白宽度
                padding: PropTypes.oneOfType([
                    PropTypes.number,
                    PropTypes.arrayOf(PropTypes.number)
                ])
            }),

            // 在图例元素较多时设置是否分页
            flipPage: PropTypes.bool,

            // 设置图例项最大宽度值，当layout设置为'horizontal'且图例项宽度总和超出maxWidth时
            // 会强制激活flipPage: true进行分页展示
            maxWidth: PropTypes.number,

            // 设置图例项最大高度值，当layout设置为'vertical'且图例项高度总和超出maxHeight时
            // 会强制激活flipPage: true进行分页展示
            maxHeight: PropTypes.number,

            // 设置是否以逆序方式展示图例项
            reversed: PropTypes.bool,

            // 设置图例的高度，默认为null
            itemHeight: PropTypes.number,

            // 设置图例的宽度，默认为null
            itemWidth: PropTypes.number,

            // 设置图例文本的相关格式
            itemName: PropTypes.exact({
                // 设置图例项marker同后面name的间距
                spacing: PropTypes.number
            }),

            // 设置图例数值的相关格式
            itemValue: PropTypes.exact({
                // 设施是否右对齐，默认为false，仅当设置图例项宽度时生效
                alignRight: PropTypes.bool
            }),

            // 设置图例项水平方向的间距
            itemSpacing: PropTypes.number,

            // 用于自定义图例的高亮状态，譬如：
            // selected: {
            //     '分类一': true,
            //     '分类二': false,
            //     '分类三': false,
            // }
            selected: PropTypes.object
        }),
        // 设置为false时会关闭图例显示
        PropTypes.bool
    ]),

    // 设置tooltip相关参数
    tooltip: PropTypes.exact({
        // 设置tooltip中要展示的字段
        fields: PropTypes.arrayOf(PropTypes.string),

        // 设置tooltip内容是否跟随鼠标移动，默认为true
        follow: PropTypes.bool,

        // 设置tooltip是否允许鼠标划入，默认为false
        enterable: PropTypes.bool,

        // 设置是否展示tooltip的标题，默认为false
        showTitle: PropTypes.bool,

        // 设置tooltip的标题内容，可传入字段名从而显示对应数据点的对应字段信息，若传入的字段名不存在
        // 则会直接显示原始的title内容
        title: PropTypes.string,

        // 设置tooltip相对于数据点的展示方位，可选的有'top'、'bottom'、'left'及'right'
        position: PropTypes.string
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
AntdLine.defaultProps = {
}