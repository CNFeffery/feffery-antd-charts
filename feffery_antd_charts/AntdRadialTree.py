# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdRadialTree(Component):
    """An AntdRadialTree component.
辐射树图组件AntdRadialTree

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    css类名.

- style (dict; optional):
    css样式.

- data (dict; required):
    必填，定义绘图所需数据.

- width (number; optional):
    图表容器像素宽度.

- height (number; optional):
    图表容器像素高度.

- autoFit (boolean; default True):
    图表是否自适应容器宽高，设置为`True`时，`width`与`height`参数将失效  默认值：`True`.

- nodeCfg (dict; optional):
    配置节点相关参数.

    `nodeCfg` is a dict with keys:

    - type (a value equal to: 'icon-node', 'card', 'circle', 'rect', 'ellipse', 'diamond', 'triangle', 'star', 'image', 'modelRect', 'donut'; optional):
        节点类型，可选项有`'icon-node'`、`'card'`、`'circle'`、`'rect'`、`'ellipse'`、`'diamond'`、`'triangle'`、
        `'star'`、`'image'`、`'modelRect'`、`'donut'`.

    - size (list of numbers; optional):
        节点最小像素尺寸，格式如：`[像素宽度, 像素高度]`  默认值：`[100, 44]`.

    - style (dict; optional):
        节点样式，支持`func`回调.

        `style` is a dict with keys:

        - func (string; optional):

            回调函数字符串.

    - label (dict; optional):
        节点文本样式，支持`func`回调.

        `label` is a dict with keys:

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional):
        回调函数字符串.

    - nodeStateStyles (dict with strings as keys and values of type ; optional):
        节点在不同状态下的样式.

- edgeCfg (dict; optional)

    `edgeCfg` is a dict with keys:

    - style (dict; optional):
        边样式，支持`func`回调.

        `style` is a dict with keys:

        - func (string; optional):

            回调函数字符串.

    - type (a value equal to: 'line', 'polyline', 'arc', 'quadratic', 'cubic', 'cubic-vertical', 'cubic-horizontal', 'loop'; optional):
        边类型，可选项有`'line'`、`'polyline'`、`'arc'`、`'quadratic'`、`'cubic'`、`'cubic-vertical'`、
        `'cubic-horizontal'`、`'loop'`  默认值：`'polyline'`.

    - label (dict; optional):
        边文本样式，支持`func`回调.

        `label` is a dict with keys:

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional):
        回调函数字符串.

    - startArrow (dict; optional):
        配置边开始箭头.

        `startArrow` is a dict with keys:

        - type (a value equal to: 'vee', 'triangle'; optional):
            箭头类型，可选项有`'vee'`、`'triangle'`.

        - size (number; optional):
            箭头像素尺寸.

        - d (number; optional):
            像素偏移量.

        - path (string; optional):
            绘制路径.

        - stroke (string; optional):
            轮廓色.

        - fill (string; optional):
            填充色.

    - endArrow (dict; optional):
        配置边结束箭头.

        `endArrow` is a dict with keys:

        - type (a value equal to: 'vee', 'triangle'; optional):
            箭头类型，可选项有`'vee'`、`'triangle'`.

        - size (number; optional):
            箭头像素尺寸.

        - d (number; optional):
            像素偏移量.

        - path (string; optional):
            绘制路径.

        - stroke (string; optional):
            轮廓色.

        - fill (string; optional):
            填充色.

    - edgeStateStyles (dict with strings as keys and values of type ; optional):
        边在不同状态下的样式.

- behaviors (list of a value equal to: 'drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node', 'click-select's; default ['drag-canvas', 'zoom-canvas']):
    启用的交互模式，可选项有`'drag-canvas'`（拖拽画布）、`'scroll-canvas'`（滚轮滚动画布）、
    `'zoom-canvas'`（缩放画布）、`'drag-node'`（拖拽节点）、'click-select'（节点选择）
    默认值：`['drag-canvas', 'zoom-canvas']`.

- animate (boolean; default False):
    是否开启动画  默认值：`False`.

- minimapCfg (dict; optional):
    配置迷你图相关参数.

    `minimapCfg` is a dict with keys:

    - show (boolean; optional):
        是否开启迷你图  默认值：`False`.

    - viewportClassName (string; optional):
        迷你图css类名.

    - type (a value equal to: 'default', 'keyShape', 'delegate'; optional):
        迷你图类型，可选项有`'default'`、`'keyShape'`、`'delegate'`.

    - size (list of numbers; optional):
        迷你图像素尺寸，格式如：`[像素宽度, 像素高度]`.

    - delegateStyle (optional)

    - refresh (boolean; optional)

    - padding (number; optional):
        像素内边距.

- layout (dict; optional)

    `layout` is a dict with keys:

    - direction (a value equal to: 'TB', 'BT', 'LR', 'RL'; optional):
        布局方向，可选项有`'TB'`、`'BT'`、`'LR'`、`'RL'`.

    - nodesep (number; optional):
        节点垂直方向像素间隔大小.

    - ranksep (number; optional):
        节点水平方向像素间隔大小.

- recentlyNodeClickRecord (dict; optional):
    节点点击事件监听.

    `recentlyNodeClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件触发时间戳.

    - data (dict; optional):
        事件对应节点信息，点击空白处时为空.

- recentlyNodeDoubleClickRecord (dict; optional):
    节点双击事件监听.

    `recentlyNodeDoubleClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件触发时间戳.

    - data (dict; optional):
        事件对应节点信息，点击空白处时为空.

- recentlyEdgeClickRecord (dict; optional):
    边点击事件监听.

    `recentlyEdgeClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件触发时间戳.

    - data (dict; optional):
        事件对应节点信息，点击空白处时为空.

- recentlyEdgeDoubleClickRecord (dict; optional):
    边双击事件监听.

    `recentlyEdgeDoubleClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件触发时间戳.

    - data (dict; optional):
        事件对应节点信息，点击空白处时为空.

- selectedNodes (dict; optional):
    节点选中事件监听，需要在``behaviors``中开启``click-select``.

    `selectedNodes` is a dict with keys:

    - timestamp (number; optional):
        事件触发时间戳.

    - data (list; optional):
        对应选中的节点信息数组.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdRadialTree'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, nodeCfg=Component.UNDEFINED, edgeCfg=Component.UNDEFINED, behaviors=Component.UNDEFINED, animate=Component.UNDEFINED, minimapCfg=Component.UNDEFINED, layout=Component.UNDEFINED, recentlyNodeClickRecord=Component.UNDEFINED, recentlyNodeDoubleClickRecord=Component.UNDEFINED, recentlyEdgeClickRecord=Component.UNDEFINED, recentlyEdgeDoubleClickRecord=Component.UNDEFINED, selectedNodes=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'width', 'height', 'autoFit', 'nodeCfg', 'edgeCfg', 'behaviors', 'animate', 'minimapCfg', 'layout', 'recentlyNodeClickRecord', 'recentlyNodeDoubleClickRecord', 'recentlyEdgeClickRecord', 'recentlyEdgeDoubleClickRecord', 'selectedNodes', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'width', 'height', 'autoFit', 'nodeCfg', 'edgeCfg', 'behaviors', 'animate', 'minimapCfg', 'layout', 'recentlyNodeClickRecord', 'recentlyNodeDoubleClickRecord', 'recentlyEdgeClickRecord', 'recentlyEdgeDoubleClickRecord', 'selectedNodes', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdRadialTree, self).__init__(**args)
