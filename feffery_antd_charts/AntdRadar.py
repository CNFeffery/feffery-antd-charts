# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AntdRadar(Component):
    """An AntdRadar component.
雷达图组件AntdRadar

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- style (dict; optional):
    当前组件css样式.

- data (list of dicts; required):
    必填，定义绘图所需数据.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- xField (string; required):
    必填，图表角度字段.

- yField (string; required):
    必填，图表半径字段.

- seriesField (string; optional):
    图表分组字段.

- smooth (boolean; optional):
    是否渲染为平滑曲线  默认值：`False`.

- radius (number; optional):
    雷达图相对画布的外环半径尺寸，取值应在`0`到`1`之间.

- startAngle (number; optional):
    雷达图开始角度，弧度制  默认值：`0`.

- endAngle (number; optional):
    雷达图结束角度，弧度制  默认值：`π`.

- color (dict; optional):
    控制雷达图折线颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- lineStyle (dict; optional):
    控制雷达图折线样式，具体见在线文档相关说明.

    `lineStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- point (dict; optional):
    配置折点相关参数，具体见在线文档相关说明.

    `point` is a dict with keys:

    - color (dict; optional):
        配置折点颜色，具体见在线文档相关说明.

        `color` is a string

      Or list of strings | dict with keys:

        - func (string; optional):

            js函数体字符串.

    - shape (dict; optional):
        配置折点形状，具体见在线文档相关说明.

        `shape` is a string | dict with keys:

        - func (string; optional)

    - style (dict; optional):
        配置折点样式，具体见在线文档相关说明.

        `style` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

- area (dict; optional):
    配置面积填充相关参数，具体见在线文档相关说明.

    `area` is a dict with keys:

    - smooth (boolean; optional):
        是否渲染为平滑曲线  默认值：`False`.

    - color (dict; optional):
        配置填充面积颜色.

        `color` is a string

      Or list of strings | dict with keys:

        - func (string; optional):

            js函数体字符串.

    - style (dict; optional):
        配置填充面积样式.

        `style` is a dict with keys:

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
    事件监听属性，用于监听最近一次填充区域点击事件.

    `recentlyAreaClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (boolean | number | string | dict | list; optional):
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
    _type = 'AntdRadar'
    Color = TypedDict(
        "Color",
            {
            "func": NotRequired[str]
        }
    )

    LineStyle = TypedDict(
        "LineStyle",
            {
            "func": NotRequired[str]
        }
    )

    PointColor = TypedDict(
        "PointColor",
            {
            "func": NotRequired[str]
        }
    )

    PointShape = TypedDict(
        "PointShape",
            {
            "func": NotRequired[str]
        }
    )

    PointStyle = TypedDict(
        "PointStyle",
            {
            "func": NotRequired[str]
        }
    )

    Point = TypedDict(
        "Point",
            {
            "color": NotRequired[typing.Union[str, typing.Sequence[str], "PointColor"]],
            "shape": NotRequired[typing.Union[str, "PointShape"]],
            "style": NotRequired[typing.Union[typing.Any, "PointStyle"]]
        }
    )

    AreaColor = TypedDict(
        "AreaColor",
            {
            "func": NotRequired[str]
        }
    )

    AreaStyle = TypedDict(
        "AreaStyle",
            {
            "func": NotRequired[str]
        }
    )

    Area = TypedDict(
        "Area",
            {
            "smooth": NotRequired[bool],
            "color": NotRequired[typing.Union[str, typing.Sequence[str], "AreaColor"]],
            "style": NotRequired[typing.Union[typing.Any, "AreaStyle"]]
        }
    )

    RecentlyTooltipChangeRecord = TypedDict(
        "RecentlyTooltipChangeRecord",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[typing.Sequence[dict]]
        }
    )

    RecentlyAreaClickRecord = TypedDict(
        "RecentlyAreaClickRecord",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[typing.Any]
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
        style: typing.Optional[dict] = None,
        data: typing.Optional[typing.Sequence[dict]] = None,
        meta: typing.Optional[typing.Any] = None,
        xField: typing.Optional[str] = None,
        yField: typing.Optional[str] = None,
        seriesField: typing.Optional[str] = None,
        smooth: typing.Optional[bool] = None,
        radius: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        startAngle: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        endAngle: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        color: typing.Optional[typing.Union[str, typing.Sequence[str], "Color"]] = None,
        lineStyle: typing.Optional[typing.Union[typing.Any, "LineStyle"]] = None,
        point: typing.Optional["Point"] = None,
        area: typing.Optional["Area"] = None,
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
        label: typing.Optional[typing.Any] = None,
        tooltip: typing.Optional[typing.Any] = None,
        annotations: typing.Optional[typing.Any] = None,
        animation: typing.Optional[typing.Any] = None,
        recentlyTooltipChangeRecord: typing.Optional["RecentlyTooltipChangeRecord"] = None,
        recentlyAreaClickRecord: typing.Optional["RecentlyAreaClickRecord"] = None,
        recentlyLegendInfo: typing.Optional["RecentlyLegendInfo"] = None,
        downloadTrigger: typing.Optional[str] = None,
        theme: typing.Optional[typing.Any] = None,
        interactions: typing.Optional[typing.Any] = None,
        state: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'smooth', 'radius', 'startAngle', 'endAngle', 'color', 'lineStyle', 'point', 'area', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'interactions', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'smooth', 'radius', 'startAngle', 'endAngle', 'color', 'lineStyle', 'point', 'area', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'interactions', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdRadar, self).__init__(**args)
