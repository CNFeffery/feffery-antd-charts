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


class AntdHeatmap(Component):
    """An AntdHeatmap component.
热力图组件AntdHeatmap

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- data (list of dicts; required):
    必填，用于定义绘图所需数据.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- xField (string; required):
    必填，图表x轴字段.

- yField (string; required):
    必填，图表y轴字段.

- colorField (string; optional):
    定义作为色彩映射依据的字段.

- sizeField (string; optional):
    图表尺寸映射字段.

- reflect (a value equal to: 'x', 'y'; optional):
    坐标轴映射类型，可选项有`'x'`、`'y'`.

- color (dict; optional):
    控制热力网格填充颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- shape (a value equal to: 'rect', 'square', 'circle'; optional):
    热力网格形状，可选项有`'rect'`、`'square'`、`'circle'`.

- coordinate (dict; optional):
    配置坐标系相关参数，具体见在线文档相关说明.

    `coordinate` is a dict with keys:

    - type (a value equal to: 'cartesian', 'polar', 'helix', 'theta'; optional):
        坐标系类型，可选项有`'cartesian'`（笛卡尔坐标系）、`'polar'`（极坐标系）、`'helix'`（螺旋坐标系）、`'theta'`（角度映射坐标系）.

    - cfg (dict; optional):
        坐标系配置项，适用于极坐标系.

        `cfg` is a dict with keys:

        - startAngle (number; optional):
            起始弧度.

        - endAngle (number; optional):
            结束弧度.

        - radius (number; optional):
            极坐标系半径，取值应在`0`到`1`之间.

        - innerRadius (number; optional):
            极坐标系内半径，取值应在`0`到`1`之间.

- sizeRatio (number; optional):
    热力网格中图形的尺寸比例，需有效定义`shape`或`sizeField`.

- heatmapStyle (dict; optional):
    控制热力网格填充样式，具体见在线文档相关说明.

    `heatmapStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- xAxis (optional):
    配置横坐标轴相关参数，具体见在线文档相关说明.

- yAxis (optional):
    配置纵坐标轴相关参数，具体见在线文档相关说明.

- width (number; optional):
    图表容器像素宽度.

- height (number; optional):
    图表容器像素高度.

- autoFit (boolean; optional):
    图表是否自适应所在父容器宽高，当`autoFit=True`时，`width`和`height`参数将失效  默认值：`True`.

- padding (number | list of numbers | string; optional):
    画布内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组，或传入`'auto'`开启底层自动计算.

- appendPadding (number | list of numbers | string; optional):
    画布额外内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组.

- renderer (a value equal to: 'canvas', 'svg'; optional):
    图表底层渲染方式，可选项有`'canvas'`和`'svg'`  默认值：`'canvas'`.

- pixelRatio (number; optional):
    `renderer='canvas'`时，控制渲染图表图片的像素比  默认值：`1`.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN'):
    图表文案语种，可选项有`'zh-CN'`、`'en-US'`  默认值：`'zh-CN'`.

- limitInPlot (boolean; optional):
    是否对超出绘图区域的几何元素进行裁剪.

- legend (optional):
    配置图例相关参数，具体见在线文档相关说明.

- label (optional):
    配置数值标签相关参数，具体见在线文档相关说明.

- tooltip (optional):
    配置信息框相关参数，具体见在线文档相关说明.

- annotations (optional):
    配置标注相关参数，具体见在线文档相关说明.

- pattern (optional):
    配置图形填充贴图相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

- recentlyTooltipChangeRecord (dict; optional):
    事件监听属性，用于监听最近一次信息框显示事件.

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (list of dicts; optional):
        涉及数据信息.

- recentlyGridClickRecord (dict; optional):
    事件监听属性，用于监听最近一次热力网格点击事件.

    `recentlyGridClickRecord` is a dict with keys:

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
    _type = 'AntdHeatmap'
    Color = TypedDict(
        "Color",
            {
            "func": NotRequired[str]
        }
    )

    CoordinateCfg = TypedDict(
        "CoordinateCfg",
            {
            "startAngle": NotRequired[NumberType],
            "endAngle": NotRequired[NumberType],
            "radius": NotRequired[NumberType],
            "innerRadius": NotRequired[NumberType]
        }
    )

    Coordinate = TypedDict(
        "Coordinate",
            {
            "type": NotRequired[Literal["cartesian", "polar", "helix", "theta"]],
            "cfg": NotRequired["CoordinateCfg"]
        }
    )

    HeatmapStyle = TypedDict(
        "HeatmapStyle",
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

    RecentlyGridClickRecord = TypedDict(
        "RecentlyGridClickRecord",
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
        xField: typing.Optional[str] = None,
        yField: typing.Optional[str] = None,
        colorField: typing.Optional[str] = None,
        sizeField: typing.Optional[str] = None,
        reflect: typing.Optional[Literal["x", "y"]] = None,
        color: typing.Optional[typing.Union[str, typing.Sequence[str], "Color"]] = None,
        shape: typing.Optional[Literal["rect", "square", "circle"]] = None,
        coordinate: typing.Optional["Coordinate"] = None,
        sizeRatio: typing.Optional[NumberType] = None,
        heatmapStyle: typing.Optional[typing.Union[typing.Any, "HeatmapStyle"]] = None,
        xAxis: typing.Optional[typing.Any] = None,
        yAxis: typing.Optional[typing.Any] = None,
        width: typing.Optional[NumberType] = None,
        height: typing.Optional[NumberType] = None,
        autoFit: typing.Optional[bool] = None,
        padding: typing.Optional[typing.Union[NumberType, typing.Sequence[NumberType], str]] = None,
        appendPadding: typing.Optional[typing.Union[NumberType, typing.Sequence[NumberType], str]] = None,
        renderer: typing.Optional[Literal["canvas", "svg"]] = None,
        pixelRatio: typing.Optional[NumberType] = None,
        locale: typing.Optional[Literal["zh-CN", "en-US"]] = None,
        limitInPlot: typing.Optional[bool] = None,
        legend: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        tooltip: typing.Optional[typing.Any] = None,
        annotations: typing.Optional[typing.Any] = None,
        pattern: typing.Optional[typing.Any] = None,
        animation: typing.Optional[typing.Any] = None,
        recentlyTooltipChangeRecord: typing.Optional["RecentlyTooltipChangeRecord"] = None,
        recentlyGridClickRecord: typing.Optional["RecentlyGridClickRecord"] = None,
        downloadTrigger: typing.Optional[str] = None,
        theme: typing.Optional[typing.Any] = None,
        interactions: typing.Optional[typing.Any] = None,
        state: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'colorField', 'sizeField', 'reflect', 'color', 'shape', 'coordinate', 'sizeRatio', 'heatmapStyle', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'pattern', 'animation', 'recentlyTooltipChangeRecord', 'recentlyGridClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'colorField', 'sizeField', 'reflect', 'color', 'shape', 'coordinate', 'sizeRatio', 'heatmapStyle', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'pattern', 'animation', 'recentlyTooltipChangeRecord', 'recentlyGridClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdHeatmap, self).__init__(**args)

setattr(AntdHeatmap, "__init__", _explicitize_args(AntdHeatmap.__init__))
