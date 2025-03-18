# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AntdRadialTree(Component):
    """An AntdRadialTree component.
辐射树图组件AntdRadialTree

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- data (dict; required):
    必填，定义绘图所需数据.

- width (number; optional):
    图表容器像素宽度.

- height (number; optional):
    图表容器像素高度.

- autoFit (boolean; default True):
    图表是否自适应所在父容器宽高，当`autoFit=True`时，`width`和`height`参数将失效  默认值：`True`.

- nodeCfg (dict; optional):
    配置节点相关参数，具体见在线文档相关说明.

    `nodeCfg` is a dict with keys:

    - type (a value equal to: 'icon-node', 'card', 'circle', 'rect', 'ellipse', 'diamond', 'triangle', 'star', 'image', 'modelRect', 'donut'; optional):
        节点类型，可选项有`'icon-node'`、`'card'`、`'circle'`、`'rect'`、`'ellipse'`、`'diamond'`、`'triangle'`、`'star'`、`'image'`、`'modelRect'`、`'donut'`.

    - size (list of numbers; optional):
        节点像素尺寸范围  默认值：`[100, 44]`.

    - style (dict; optional):
        节点样式.

        `style` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - label (dict; optional):
        节点文本样式.

        `label` is a dict with keys:

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

    - nodeStateStyles (dict with strings as keys and values of type ; optional):
        配置节点不同状态下的样式，可用的状态有`'hover'`.

- edgeCfg (dict; optional):
    配置边相关参数，具体见在线文档相关说明.

    `edgeCfg` is a dict with keys:

    - style (dict; optional):
        边样式.

        `style` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - type (a value equal to: 'line', 'polyline', 'arc', 'quadratic', 'cubic', 'cubic-vertical', 'cubic-horizontal', 'loop'; optional):
        边类型，可选项有`'line'`、`'polyline'`、`'arc'`、`'quadratic'`、`'cubic'`、`'cubic-vertical'`、`'cubic-horizontal'`、`'loop'`
        默认值：`'cubic-horizontal'`.

    - label (dict; optional):
        边文本样式.

        `label` is a dict with keys:

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

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
        配置边不同状态下的样式，可用的状态有`'hover'`.

- behaviors (list of a value equal to: 'drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node', 'click-select's; default ['drag-canvas', 'zoom-canvas']):
    配置要启用的交互模式，支持多选，可选项有`'drag-canvas'`、`'scroll-canvas'`、`'zoom-canvas'`、`'drag-node'`、`'click-select'`
    默认值：`['drag-canvas', 'zoom-canvas']`.

- animate (boolean; default False):
    是否启用动画效果  默认值：`True`.

- minimapCfg (dict; optional):
    配置迷你图相关参数，具体见在线文档.

    `minimapCfg` is a dict with keys:

    - show (boolean; optional):
        是否展示迷你图  默认值：`False`.

    - viewportClassName (string; optional):
        迷你图css类名.

    - type (a value equal to: 'default', 'keyShape', 'delegate'; optional):
        迷你图类型，可选项有`'default'`、`'keyShape'`、`'delegate'`.

    - size (list of numbers; optional):
        配置迷你图像素尺寸，格式如`[宽度, 高度]`.

    - padding (number; optional):
        内填充像素尺寸.

- layout (dict; optional):
    配置布局相关参数，具体见在线文档.

    `layout` is a dict with keys:

    - direction (a value equal to: 'TB', 'BT', 'LR', 'RL'; optional):
        布局方式，可选项有`'TB'`、`'BT'`、`'LR'`、`'RL'`.

    - nodesep (number; optional):
        节点垂直方向像素间隔大小.

    - ranksep (number; optional):
        节点水平方向像素间隔大小.

- recentlyNodeClickRecord (dict; optional):
    事件监听属性，用于监听最近一次节点点击事件.

    `recentlyNodeClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- recentlyNodeDoubleClickRecord (dict; optional):
    事件监听属性，用于监听最近一次节点双击事件.

    `recentlyNodeDoubleClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- recentlyEdgeClickRecord (dict; optional):
    事件监听属性，用于监听最近一次边点击事件.

    `recentlyEdgeClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- recentlyEdgeDoubleClickRecord (dict; optional):
    事件监听属性，用于监听最近一次边双击事件.

    `recentlyEdgeDoubleClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- selectedNodes (dict; optional):
    事件监听属性，用于监听最近一次节点选中事件，需要在``behaviors``中开启``click-select``.

    `selectedNodes` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (list; optional):
        涉及数据信息."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdRadialTree'
    NodeCfgStyle = TypedDict(
        "NodeCfgStyle",
            {
            "func": NotRequired[str]
        }
    )

    NodeCfgLabelStyle = TypedDict(
        "NodeCfgLabelStyle",
            {
            "func": NotRequired[str]
        }
    )

    NodeCfgLabel = TypedDict(
        "NodeCfgLabel",
            {
            "style": NotRequired[typing.Union[typing.Any, "NodeCfgLabelStyle"]]
        }
    )

    NodeCfg = TypedDict(
        "NodeCfg",
            {
            "type": NotRequired[Literal["icon-node", "card", "circle", "rect", "ellipse", "diamond", "triangle", "star", "image", "modelRect", "donut"]],
            "size": NotRequired[typing.Sequence[typing.Union[int, float, numbers.Number]]],
            "style": NotRequired[typing.Union[typing.Any, "NodeCfgStyle"]],
            "label": NotRequired["NodeCfgLabel"],
            "nodeStateStyles": NotRequired[typing.Dict[typing.Union[str, float, int], typing.Any]]
        }
    )

    EdgeCfgStyle = TypedDict(
        "EdgeCfgStyle",
            {
            "func": NotRequired[str]
        }
    )

    EdgeCfgLabelStyle = TypedDict(
        "EdgeCfgLabelStyle",
            {
            "func": NotRequired[str]
        }
    )

    EdgeCfgLabel = TypedDict(
        "EdgeCfgLabel",
            {
            "style": NotRequired[typing.Union[typing.Any, "EdgeCfgLabelStyle"]]
        }
    )

    EdgeCfgStartArrow = TypedDict(
        "EdgeCfgStartArrow",
            {
            "type": NotRequired[Literal["vee", "triangle"]],
            "size": NotRequired[typing.Union[int, float, numbers.Number]],
            "d": NotRequired[typing.Union[int, float, numbers.Number]],
            "path": NotRequired[str],
            "stroke": NotRequired[str],
            "fill": NotRequired[str]
        }
    )

    EdgeCfgEndArrow = TypedDict(
        "EdgeCfgEndArrow",
            {
            "type": NotRequired[Literal["vee", "triangle"]],
            "size": NotRequired[typing.Union[int, float, numbers.Number]],
            "d": NotRequired[typing.Union[int, float, numbers.Number]],
            "path": NotRequired[str],
            "stroke": NotRequired[str],
            "fill": NotRequired[str]
        }
    )

    EdgeCfg = TypedDict(
        "EdgeCfg",
            {
            "style": NotRequired[typing.Union[typing.Any, "EdgeCfgStyle"]],
            "type": NotRequired[Literal["line", "polyline", "arc", "quadratic", "cubic", "cubic-vertical", "cubic-horizontal", "loop"]],
            "label": NotRequired["EdgeCfgLabel"],
            "startArrow": NotRequired["EdgeCfgStartArrow"],
            "endArrow": NotRequired["EdgeCfgEndArrow"],
            "edgeStateStyles": NotRequired[typing.Dict[typing.Union[str, float, int], typing.Any]]
        }
    )

    MinimapCfg = TypedDict(
        "MinimapCfg",
            {
            "show": NotRequired[bool],
            "viewportClassName": NotRequired[str],
            "type": NotRequired[Literal["default", "keyShape", "delegate"]],
            "size": NotRequired[typing.Sequence[typing.Union[int, float, numbers.Number]]],
            "padding": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Layout = TypedDict(
        "Layout",
            {
            "direction": NotRequired[Literal["TB", "BT", "LR", "RL"]],
            "nodesep": NotRequired[typing.Union[int, float, numbers.Number]],
            "ranksep": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    RecentlyNodeClickRecord = TypedDict(
        "RecentlyNodeClickRecord",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[dict]
        }
    )

    RecentlyNodeDoubleClickRecord = TypedDict(
        "RecentlyNodeDoubleClickRecord",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[dict]
        }
    )

    RecentlyEdgeClickRecord = TypedDict(
        "RecentlyEdgeClickRecord",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[dict]
        }
    )

    RecentlyEdgeDoubleClickRecord = TypedDict(
        "RecentlyEdgeDoubleClickRecord",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[dict]
        }
    )

    SelectedNodes = TypedDict(
        "SelectedNodes",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[typing.Sequence]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        data: typing.Optional[dict] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        autoFit: typing.Optional[bool] = None,
        nodeCfg: typing.Optional["NodeCfg"] = None,
        edgeCfg: typing.Optional["EdgeCfg"] = None,
        behaviors: typing.Optional[typing.Sequence[Literal["drag-canvas", "scroll-canvas", "zoom-canvas", "drag-node", "click-select"]]] = None,
        animate: typing.Optional[bool] = None,
        minimapCfg: typing.Optional["MinimapCfg"] = None,
        layout: typing.Optional["Layout"] = None,
        recentlyNodeClickRecord: typing.Optional["RecentlyNodeClickRecord"] = None,
        recentlyNodeDoubleClickRecord: typing.Optional["RecentlyNodeDoubleClickRecord"] = None,
        recentlyEdgeClickRecord: typing.Optional["RecentlyEdgeClickRecord"] = None,
        recentlyEdgeDoubleClickRecord: typing.Optional["RecentlyEdgeDoubleClickRecord"] = None,
        selectedNodes: typing.Optional["SelectedNodes"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'width', 'height', 'autoFit', 'nodeCfg', 'edgeCfg', 'behaviors', 'animate', 'minimapCfg', 'layout', 'recentlyNodeClickRecord', 'recentlyNodeDoubleClickRecord', 'recentlyEdgeClickRecord', 'recentlyEdgeDoubleClickRecord', 'selectedNodes']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'width', 'height', 'autoFit', 'nodeCfg', 'edgeCfg', 'behaviors', 'animate', 'minimapCfg', 'layout', 'recentlyNodeClickRecord', 'recentlyNodeDoubleClickRecord', 'recentlyEdgeClickRecord', 'recentlyEdgeDoubleClickRecord', 'selectedNodes']
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
