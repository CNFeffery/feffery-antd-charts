/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { RadialTreeGraph } from '@ant-design/graphs';
import React from 'react';
import { isUndefined, omitBy, cloneDeep } from 'lodash';
import { propTypes, defaultProps } from '../../components/graphs/AntdRadialTree.react';

/**
 * 辐射树图组件AntdRadialTree
 */
const AntdRadialTree = (props) => {
    const {
        id,
        key,
        className,
        style,
        data,
        width,
        height,
        autoFit,
        nodeCfg,
        edgeCfg,
        behaviors,
        animate,
        minimapCfg,
        layout,
        setProps,
        component_loading
    } = props;

    // 初始化config参数对象，每次渲染前的参数解析变动只在config中生效
    let config = {};

    // 刷新基础参数
    config = {
        ...config,
        data,
        width,
        height,
        autoFit,
        behaviors,
        animate,
        minimapCfg,
        layout
    }

    // 进阶参数
    config.nodeCfg = cloneDeep(nodeCfg)
    // 若nodeCfg.style具有自定义函数func属性
    if (nodeCfg?.style?.func) {
        config.nodeCfg.style = eval(nodeCfg.style.func)
    }
    // 若nodeCfg.label.style具有自定义函数func属性
    if (nodeCfg?.label?.style?.func) {
        config.nodeCfg.label.style = eval(nodeCfg.label.style.func)
    }

    config.edgeCfg = cloneDeep(edgeCfg)
    // 若nedgeCfg.style具有自定义函数func属性
    if (edgeCfg?.style?.func) {
        config.edgeCfg.style = eval(edgeCfg.style.func)
    }
    // edgeCfg.label.style具有自定义函数func属性
    if (edgeCfg?.label?.style?.func) {
        config.edgeCfg.label.style = eval(edgeCfg.label.style.func)
    }

    // 利用lodash移除所有值为undefined的属性
    config = omitBy(config, isUndefined)

    return <RadialTreeGraph
        id={id}
        key={key}
        className={className}
        style={style}
        // 绑定常用事件
        onReady={(plot) => {
            // 监听非数据要素区域点击事件
            plot.on('canvas:click', (e) => {
                setProps({
                    recentlyNodeClickRecord: {
                        timestamp: (new Date()).valueOf(),
                        data: null
                    },
                    recentlyEdgeClickRecord: {
                        timestamp: (new Date()).valueOf(),
                        data: null
                    }
                })
            });
            // 监听非数据要素区域双击事件
            plot.on('canvas:dblclick', (e) => {
                setProps({
                    recentlyNodeDoubleClickRecord: {
                        timestamp: (new Date()).valueOf(),
                        data: null
                    },
                    recentlyEdgeDoubleClickRecord: {
                        timestamp: (new Date()).valueOf(),
                        data: null
                    }
                })
            });

            plot.on('node:mousedown', (e) => {
                setProps({
                    recentlyNodeClickRecord: {
                        timestamp: (new Date()).valueOf(),
                        data: {
                            id: e.item._cfg.model.id,
                            value: e.item._cfg.model.value
                        }
                    }
                })
            });
            plot.on('node:dblclick', (e) => {
                setProps({
                    recentlyNodeDoubleClickRecord: {
                        timestamp: (new Date()).valueOf(),
                        data: {
                            id: e.item._cfg.model.id,
                            value: e.item._cfg.model.value
                        }
                    }
                })
            });

            plot.on('edge:mousedown', (e) => {
                setProps({
                    recentlyEdgeClickRecord: {
                        timestamp: (new Date()).valueOf(),
                        data: {
                            source: e.item._cfg.model.source,
                            target: e.item._cfg.model.target
                        }
                    }
                })
            });
            plot.on('edge:dblclick', (e) => {
                setProps({
                    recentlyEdgeDoubleClickRecord: {
                        timestamp: (new Date()).valueOf(),
                        data: {
                            source: e.item._cfg.model.source,
                            target: e.item._cfg.model.target
                        }
                    }
                })
            });

            plot.on('nodeselectchange', (e) => {
                setProps({
                    selectedNodes: {
                        timestamp: (new Date()).valueOf(),
                        data: e.selectedItems.nodes.map(
                            node => ({
                                id: node._cfg.model.id,
                                value: node._cfg.model.value
                            })
                        )
                    }
                })
            });
        }}
        data-dash-is-loading={component_loading}
        {...config} />;
}

AntdRadialTree.defaultProps = defaultProps;
AntdRadialTree.propTypes = propTypes;

export default AntdRadialTree;