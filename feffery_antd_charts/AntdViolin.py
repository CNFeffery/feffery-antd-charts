# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AntdViolin(Component):
    """An AntdViolin component.
小提琴图组件AntdViolin

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- data (list of dicts; required):
    必填，定义绘图所需数据.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- xField (string; required):
    必填，图表x轴字段.

- yField (string; required):
    必填，图表y轴字段.

- seriesField (string; optional):
    图表分组字段.

- box (boolean; optional):
    是否展示内部箱线图  默认值：`True`.

- shape (a value equal to: 'smooth', 'hollow', 'hollow-smooth'; optional):
    小提琴形状，可选项有`'smooth'`（平滑）、`'hollow'`（空心）、`'hollow-smooth'`（平滑+空心）.

- violinStyle (dict; optional):
    控制小提琴图样式，具体见在线文档相关说明.

    `violinStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- color (dict; optional):
    控制条形填充颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

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

- tooltip (optional):
    配置信息框相关参数，具体见在线文档相关说明.

- annotations (optional):
    配置标注相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

- recentlyTooltipChangeRecord (dict; optional):
    事件监听属性，用于监听最近一次信息框显示事件.

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (list of dicts; optional):
        涉及数据信息.

- recentlyViolinClickRecord (dict; optional):
    事件监听属性，用于监听最近一次小提琴图点击事件.

    `recentlyViolinClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- recentlyLegendInfo (dict; optional):
    事件监听属性，用于监听最近一次图例点击事件.

    `recentlyLegendInfo` is a dict with keys:

    - triggerItemName (boolean | number | string | dict | list; optional):
        被点击图例项名称.

    - items (list of dicts; optional):
        当前各图例项信息.

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
    _type = 'AntdViolin'
    ViolinStyle = TypedDict(
        "ViolinStyle",
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
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[typing.Sequence[dict]]
        }
    )

    RecentlyViolinClickRecord = TypedDict(
        "RecentlyViolinClickRecord",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[dict]
        }
    )

    RecentlyLegendInfo = TypedDict(
        "RecentlyLegendInfo",
            {
            "triggerItemName": NotRequired[typing.Any],
            "items": NotRequired[typing.Sequence[dict]]
        }
    )

    @_explicitize_args
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
        seriesField: typing.Optional[str] = None,
        box: typing.Optional[bool] = None,
        shape: typing.Optional[Literal["smooth", "hollow", "hollow-smooth"]] = None,
        violinStyle: typing.Optional[typing.Union[typing.Any, "ViolinStyle"]] = None,
        color: typing.Optional[typing.Union[str, typing.Sequence[str], "Color"]] = None,
        xAxis: typing.Optional[typing.Any] = None,
        yAxis: typing.Optional[typing.Any] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        autoFit: typing.Optional[bool] = None,
        padding: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]], str]] = None,
        appendPadding: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]], str]] = None,
        renderer: typing.Optional[Literal["canvas", "svg"]] = None,
        pixelRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        locale: typing.Optional[Literal["zh-CN", "en-US"]] = None,
        limitInPlot: typing.Optional[bool] = None,
        legend: typing.Optional[typing.Any] = None,
        tooltip: typing.Optional[typing.Any] = None,
        annotations: typing.Optional[typing.Any] = None,
        animation: typing.Optional[typing.Any] = None,
        recentlyTooltipChangeRecord: typing.Optional["RecentlyTooltipChangeRecord"] = None,
        recentlyViolinClickRecord: typing.Optional["RecentlyViolinClickRecord"] = None,
        recentlyLegendInfo: typing.Optional["RecentlyLegendInfo"] = None,
        downloadTrigger: typing.Optional[str] = None,
        theme: typing.Optional[typing.Any] = None,
        interactions: typing.Optional[typing.Any] = None,
        state: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'box', 'shape', 'violinStyle', 'color', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyViolinClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'interactions', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'box', 'shape', 'violinStyle', 'color', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyViolinClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'interactions', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdViolin, self).__init__(**args)
