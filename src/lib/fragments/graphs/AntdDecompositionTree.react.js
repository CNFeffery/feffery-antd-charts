/* eslint-disable no-unused-vars */
/* eslint-disable no-undefined */
/* eslint-disable no-else-return */
/* eslint-disable no-eval */
/* eslint-disable prefer-const */
import { DecompositionTreeGraph } from '@ant-design/graphs';
import React, { Component } from 'react';
import { isUndefined, omitBy, cloneDeep } from 'lodash';
import { propTypes, defaultProps } from '../../components/graphs/AntdDecompositionTree.react';

// 定义指标拆解图组件AntdDecompositionTree，部分API参数参考https://charts.ant.design/zh/examples/relation-graph/decomposition-tree-graph#basic
export default class AntdDecompositionTree extends Component {

    render() {
        // 取得必要属性或参数
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
            level,
            behaviors,
            markerCfg,
            animate,
            minimapCfg,
            layout,
            setProps,
            loading_state
        } = this.props;

        // 初始化config参数对象，每次渲染前的参数解析变动只在config中生效
        let config = {};

        // 刷新基础参数
        config = {
            ...config,
            data,
            width,
            height,
            autoFit,
            level,
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
        // 若nodeCfg.title.style具有自定义函数func属性
        if (nodeCfg?.title?.style?.func) {
            config.nodeCfg.title.style = eval(nodeCfg.title.style.func)
        }
        // 若nodeCfg.label.style具有自定义函数func属性
        if (nodeCfg?.label?.style?.func) {
            config.nodeCfg.label.style = eval(nodeCfg.label.style.func)
        }
        // 若nodeCfg.items.style具有自定义函数func属性
        if (nodeCfg?.items?.style?.func) {
            config.nodeCfg.items.style = eval(nodeCfg.items.style.func)
        }
        // 若nodeCfg.badge.style具有自定义函数func属性
        if (nodeCfg?.badge?.style?.func) {
            config.nodeCfg.badge.style = eval(nodeCfg.badge.style.func)
        }
        // 若nodeCfg.percent.style具有自定义函数func属性
        if (nodeCfg?.percent?.style?.func) {
            config.nodeCfg.percent.style = eval(nodeCfg.percent.style.func)
        }

        config.edgeCfg = cloneDeep(edgeCfg)
        // 若edgeCfg.style具有自定义函数func属性
        if (edgeCfg?.style?.func) {
            config.edgeCfg.style = eval(edgeCfg.style.func)
        }
        // edgeCfg.label.style具有自定义函数func属性
        if (edgeCfg?.label?.style?.func) {
            config.edgeCfg.label.style = eval(edgeCfg.label.style.func)
        }

        config.markerCfg = cloneDeep(markerCfg)
        // markerCfg.style具有自定义函数func属性
        if (markerCfg?.func) {
            config.markerCfg = eval(markerCfg.func)
        }

        // 利用lodash移除所有值为undefined的属性
        config = omitBy(config, isUndefined)

        return <DecompositionTreeGraph
            id={id}
            key={key}
            className={className}
            style={style}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
            {...config} />;
    }
}


AntdDecompositionTree.defaultProps = defaultProps;
AntdDecompositionTree.propTypes = propTypes;