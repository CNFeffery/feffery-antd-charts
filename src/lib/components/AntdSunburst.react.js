/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { Sunburst } from '@ant-design/plots';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { intersection } from 'lodash';
import { difference } from './utils';

// 定义不触发重绘的参数数组
const preventUpdateProps = ['loading_state'];

// 定义旭日图组件AntdSunburst，部分API参数参考https://charts.ant.design/zh/examples/more-plots/sunburst#basic
export default class AntdSunburst extends Component {

    constructor(props) {
        super(props);
        this.chartRef = React.createRef();
    }

    shouldComponentUpdate(nextProps) {

        // // 计算发生变化的参数名
        // const changedProps = Object.keys(difference(this.props, nextProps))

        // // 若无变化的props，则不触发重绘
        // if (changedProps.length === 0) {
        //     return false;
        // }

        // // 计算发生变化的参数名与需要阻止重绘的参数名数组的交集
        // let changedPreventUpdateProps = intersection(
        //     changedProps,
        //     preventUpdateProps
        // )

        // // 若有交集，则不触发重绘
        // if (changedPreventUpdateProps.length !== 0) {
        //     return false;
        // } else {
        //     // 取得plot实例
        //     const chart = this.chartRef.current.getChart()
        //     // 检查data参数是否发生更新
        //     if (changedProps.indexOf('data') !== -1) {
        //         // 动态调整数据
        //         chart.changeData(nextProps.data)
        //         return false;
        //     } else {
        //         chart.update({
        //             ...nextProps
        //         })
        //     }
        // }
        return true;
    }

    render() {
        // 取得必要属性或参数
        const {
            id,
            className,
            style,
            setProps,
            loading_state
        } = this.props;

        const data = {
            "name": "咖啡产地",
            "children": [
                {
                    "name": "非洲",
                    "value": 4,
                    "children": [
                        {
                            "continent": "非洲",
                            "country": "埃塞俄比亚",
                            "symbol": "🇪🇹",
                            "area": "耶加雪菲",
                            "name": "埃塞俄比亚",
                            "value": 1
                        },
                        {
                            "continent": "非洲",
                            "country": "肯尼亚",
                            "symbol": "🇰🇪",
                            "coffee": "阿拉比加卡豆",
                            "name": "肯尼亚",
                            "value": 1
                        },
                        {
                            "continent": "非洲",
                            "country": "坦桑尼亚",
                            "symbol": "🇹🇿",
                            "coffee": "乞力马扎罗咖啡",
                            "name": "坦桑尼亚",
                            "value": 1
                        },
                        {
                            "continent": "非洲",
                            "country": "乌干达",
                            "symbol": "🇺🇬",
                            "name": "乌干达",
                            "value": 1
                        }
                    ]
                },
                {
                    "name": "中南美洲",
                    "value": 6,
                    "children": [
                        {
                            "continent": "中南美洲",
                            "country": "巴西",
                            "symbol": "🇧🇷",
                            "name": "巴西",
                            "value": 1
                        },
                        {
                            "continent": "中南美洲",
                            "country": "哥伦比亚",
                            "symbol": "🇨🇴",
                            "name": "哥伦比亚",
                            "value": 1
                        },
                        {
                            "continent": "中南美洲",
                            "country": "牙买加",
                            "symbol": "🇯🇲",
                            "name": "牙买加",
                            "value": 1
                        },
                        {
                            "continent": "中南美洲",
                            "country": "巴拿马",
                            "symbol": "🇵🇦",
                            "name": "巴拿马",
                            "value": 1
                        },
                        {
                            "continent": "中南美洲",
                            "country": "危地马拉",
                            "symbol": "🇬🇹",
                            "name": "危地马拉",
                            "value": 1
                        },
                        {
                            "continent": "中南美洲",
                            "country": "哥斯达黎加",
                            "symbol": "🇨🇷",
                            "name": "哥斯达黎加",
                            "value": 1
                        }
                    ]
                },
                {
                    "name": "亚洲",
                    "value": 5,
                    "children": [
                        {
                            "continent": "亚洲",
                            "country": "印度尼西亚",
                            "symbol": "🇮🇩",
                            "area": "苏门答腊",
                            "coffee": "曼特宁咖啡",
                            "name": "印度尼西亚",
                            "value": 1
                        },
                        {
                            "continent": "亚洲",
                            "country": "印度",
                            "symbol": "🇮🇳",
                            "name": "印度",
                            "value": 1
                        },
                        {
                            "continent": "亚洲",
                            "country": "越南",
                            "symbol": "🇻🇳",
                            "name": "越南",
                            "value": 1
                        },
                        {
                            "continent": "亚洲",
                            "country": "也门",
                            "symbol": "🇾🇪",
                            "name": "也门",
                            "value": 1
                        },
                        {
                            "continent": "亚洲",
                            "country": "中国",
                            "symbol": "🇨🇳",
                            "name": "中国",
                            "value": 1
                        }
                    ]
                }
            ]
        };

        const config = {
            data,
            innerRadius: 0.3,
            interactions: [
                {
                    type: 'element-active',
                },
            ],
            label: {
                // label layout: limit label in shape, which means the labels out of shape will be hide
                layout: [
                    {
                        type: 'limit-in-shape',
                    },
                ],
            }
        };

        return <Sunburst {...config} />;

    }
}

// 定义参数或属性
AntdSunburst.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

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
AntdSunburst.defaultProps = {
}