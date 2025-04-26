# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class AntdSankey(Component):
    """An AntdSankey component.
桑基图组件AntdSankey

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- data (list of dicts; optional):
    必填，定义绘图所需数据.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- sourceField (string; optional):
    来源节点字段.

- targetField (string; optional):
    目标节点字段.

- weightField (string; optional):
    权重字段.

- rawFields (list of strings; optional):
    声明辅助额外字段.

- width (number; optional):
    图表容器像素宽度.

- height (number; optional):
    图表容器像素高度.

- autoFit (boolean; optional):
    图表是否自适应所在父容器宽高，当`autoFit=True`时，`width`和`height`参数将失效  默认值：`True`.

- padding (number | list of numbers | a value equal to: 'auto'; optional):
    画布内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组，或传入`'auto'`开启底层自动计算.

- appendPadding (number | list of numbers; optional):
    画布额外内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组.

- renderer (a value equal to: 'canvas', 'svg'; optional):
    图表底层渲染方式，可选项有`'canvas'`和`'svg'`  默认值：`'canvas'`.

- pixelRatio (number; optional):
    `renderer='canvas'`时，控制渲染图表图片的像素比  默认值：`1`.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN'):
    图表文案语种，可选项有`'zh-CN'`、`'en-US'`  默认值：`'zh-CN'`.

- limitInPlot (boolean; optional):
    是否对超出绘图区域的几何元素进行裁剪.

- nodeStyle (dict; optional):
    控制填充区域样式，具体见在线文档相关说明.

    `nodeStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- edgeStyle (dict; optional):
    控制轮廓样式，具体见在线文档相关说明.

    `edgeStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- color (dict; optional):
    控制填充区域颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- nodeWidthRatio (number; optional):
    节点宽度比例，取值应在`0`到`1`之间，以画布宽度为单位`1`  默认值：`0.008`.

- nodePaddingRatio (number; optional):
    节点之间间距比例，取值应在`0`到`1`之间，以画布宽度为单位`1`  默认值：`0.01`.

- nodeAlign (a value equal to: 'left', 'right', 'center', 'justify'; optional):
    节点布局方式，可选项有`'left'`、`'right'`、`'center'`、`'justify'`
    默认值：`'justify'`.

- nodeDraggable (boolean; optional):
    节点是否可拖拽调整位置  默认值：`False`.

- tooltip (optional):
    配置信息框相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

- recentlyTooltipChangeRecord (dict; optional):
    事件监听属性，用于监听最近一次信息框显示事件.

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (list of dicts; optional):
        涉及数据信息.

- recentlyAreaClickRecord (dict; optional):
    事件监听属性，用于监听最近一次区域点击事件.

    `recentlyAreaClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- downloadTrigger (string; default 'download-trigger'):
    对当前组件的`downloadTrigger`值进行更新，可实现主动下载当前图表为`png`格式图片.

- theme (optional):
    配置主题相关参数，具体见在线文档相关说明.

- interactions (optional):
    配置交互功能相关参数，具体见在线文档相关说明.

- state (optional):
    配置状态样式相关参数，具体见在线文档相关说明."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdSankey'
    NodeStyle = TypedDict(
        "NodeStyle",
            {
            "func": NotRequired[str]
        }
    )

    EdgeStyle = TypedDict(
        "EdgeStyle",
            {
            "func": NotRequired[str]
        }
    )

    Color = TypedDict(
        "Color",
            {
            "func": NotRequired[str]
        }
    )

    RecentlyTooltipChangeRecord = TypedDict(
        "RecentlyTooltipChangeRecord",
            {
            "timestamp": NotRequired[NumberType],
            "data": NotRequired[typing.Sequence[dict]]
        }
    )

    RecentlyAreaClickRecord = TypedDict(
        "RecentlyAreaClickRecord",
            {
            "timestamp": NotRequired[NumberType],
            "data": NotRequired[dict]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        data: typing.Optional[typing.Sequence[dict]] = None,
        meta: typing.Optional[typing.Any] = None,
        sourceField: typing.Optional[str] = None,
        targetField: typing.Optional[str] = None,
        weightField: typing.Optional[str] = None,
        rawFields: typing.Optional[typing.Sequence[str]] = None,
        width: typing.Optional[NumberType] = None,
        height: typing.Optional[NumberType] = None,
        autoFit: typing.Optional[bool] = None,
        padding: typing.Optional[typing.Union[NumberType, typing.Sequence[NumberType], Literal["auto"]]] = None,
        appendPadding: typing.Optional[typing.Union[NumberType, typing.Sequence[NumberType]]] = None,
        renderer: typing.Optional[Literal["canvas", "svg"]] = None,
        pixelRatio: typing.Optional[NumberType] = None,
        locale: typing.Optional[Literal["zh-CN", "en-US"]] = None,
        limitInPlot: typing.Optional[bool] = None,
        nodeStyle: typing.Optional[typing.Union[typing.Any, "NodeStyle"]] = None,
        edgeStyle: typing.Optional[typing.Union[typing.Any, "EdgeStyle"]] = None,
        color: typing.Optional[typing.Union[str, typing.Sequence[str], "Color"]] = None,
        nodeWidthRatio: typing.Optional[NumberType] = None,
        nodePaddingRatio: typing.Optional[NumberType] = None,
        nodeAlign: typing.Optional[Literal["left", "right", "center", "justify"]] = None,
        nodeDraggable: typing.Optional[bool] = None,
        tooltip: typing.Optional[typing.Any] = None,
        animation: typing.Optional[typing.Any] = None,
        recentlyTooltipChangeRecord: typing.Optional["RecentlyTooltipChangeRecord"] = None,
        recentlyAreaClickRecord: typing.Optional["RecentlyAreaClickRecord"] = None,
        downloadTrigger: typing.Optional[str] = None,
        theme: typing.Optional[typing.Any] = None,
        interactions: typing.Optional[typing.Any] = None,
        state: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'sourceField', 'targetField', 'weightField', 'rawFields', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'nodeStyle', 'edgeStyle', 'color', 'nodeWidthRatio', 'nodePaddingRatio', 'nodeAlign', 'nodeDraggable', 'tooltip', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'sourceField', 'targetField', 'weightField', 'rawFields', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'nodeStyle', 'edgeStyle', 'color', 'nodeWidthRatio', 'nodePaddingRatio', 'nodeAlign', 'nodeDraggable', 'tooltip', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdSankey, self).__init__(**args)

setattr(AntdSankey, "__init__", _explicitize_args(AntdSankey.__init__))
