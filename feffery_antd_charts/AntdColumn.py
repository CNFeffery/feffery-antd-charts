# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AntdColumn(Component):
    """An AntdColumn component.
柱状图组件AntdColumn

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
    必填，图表x轴字段.

- yField (string; required):
    必填，图表y轴字段.

- seriesField (string; optional):
    图表分组字段.

- groupField (string; optional):
    `isGroup=True`时有效，用于针对堆叠分组柱状图指定分组字段.

- isStack (boolean; optional):
    `seriesField`有效时，是否渲染堆叠柱状图.

- isGroup (boolean; optional):
    `seriesField`有效时，是否渲染分组柱状图.

- isRange (boolean; optional):
    当`yField`对应数据项满足格式`[区间开始值, 区间结束值]`时，用于控制是否渲染区间柱状图.

- isPercent (boolean; optional):
    是否渲染为百分比柱状图，需配合设置`isStack=True`.

- color (dict; optional):
    控制柱体填充颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- columnStyle (dict; optional):
    控制柱体填充样式，具体见在线文档相关说明.

    `columnStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- slider (optional):
    配置缩略轴相关参数，具体见在线文档相关说明.

- intervalPadding (number; optional):
    分组柱状图组间间隔像素宽度.

- dodgePadding (number; optional):
    分组柱状图组内间隔像素宽度.

- minColumnWidth (number; optional):
    柱状图最小像素宽度.

- maxColumnWidth (number; optional):
    柱状图最大像素宽度.

- columnBackground (dict; optional):
    配置柱体背景相关参数，具体见在线文档相关说明.

    `columnBackground` is a dict with keys:

    - style (optional):
        柱体背景样式.

- columnWidthRatio (number; optional):
    柱体宽度比例，取值在`0`到`1`之间.

- marginRatio (number; optional):
    分组柱体间隔宽度比例，取值在`0`到`1`之间.

- scrollbar (optional):
    配置滚动条相关参数，具体见在线文档相关说明.

- conversionTag (dict; optional):
    配置转化标签相关参数，具体见在线文档相关说明.

    `conversionTag` is a dict with keys:

    - size (number; optional):
        转化率标签像素尺寸.

    - spacing (number; optional):
        转化率标签与图表元素之间的像素间距.

    - offset (number; optional):
        组件与坐标轴之间的像素距离.

    - arrow (dict; optional):
        配置转化率组件箭头样式，设置为`False`时不显示箭头.

        `arrow` is a boolean

      Or dict with keys:

        - headSize (number; optional):

            箭头像素尺寸.

    - text (dict; optional):
        配置转化率组件文本，设置为`False`时不显示文本.

        `text` is a boolean | dict with keys:

        - formatter (dict; optional):

            自定义转化率计算`javascript`函数.

            `formatter` is a dict with keys:

            - func (string; optional):

                js函数体字符串.

        - style (optional):

            转化率文本样式.

- connectedArea (dict; optional):
    配置联通对比区域相关参数，具体见在线文档相关说明.

    `connectedArea` is a dict with keys:

    - trigger (boolean | string; optional):
        触发方式，可选项有`'hover'`、`'click'`，设置为`False`时不触发. | boolean

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

- recentlyColumnClickRecord (dict; optional):
    事件监听属性，用于监听最近一次柱体点击事件.

    `recentlyColumnClickRecord` is a dict with keys:

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

- pattern (optional):
    配置图形填充贴图相关参数，具体见在线文档相关说明.

- interactions (optional):
    配置交互功能相关参数，具体见在线文档相关说明.

- state (optional):
    配置状态样式相关参数，具体见在线文档相关说明."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdColumn'
    Color = TypedDict(
        "Color",
            {
            "func": NotRequired[str]
        }
    )

    ColumnStyle = TypedDict(
        "ColumnStyle",
            {
            "func": NotRequired[str]
        }
    )

    ColumnBackground = TypedDict(
        "ColumnBackground",
            {
            "style": NotRequired[typing.Any]
        }
    )

    ConversionTagArrow = TypedDict(
        "ConversionTagArrow",
            {
            "headSize": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    ConversionTagTextFormatter = TypedDict(
        "ConversionTagTextFormatter",
            {
            "func": NotRequired[str]
        }
    )

    ConversionTagText = TypedDict(
        "ConversionTagText",
            {
            "formatter": NotRequired["ConversionTagTextFormatter"],
            "style": NotRequired[typing.Any]
        }
    )

    ConversionTag = TypedDict(
        "ConversionTag",
            {
            "size": NotRequired[typing.Union[int, float, numbers.Number]],
            "spacing": NotRequired[typing.Union[int, float, numbers.Number]],
            "offset": NotRequired[typing.Union[int, float, numbers.Number]],
            "arrow": NotRequired[typing.Union[bool, "ConversionTagArrow"]],
            "text": NotRequired[typing.Union[bool, "ConversionTagText"]]
        }
    )

    ConnectedArea = TypedDict(
        "ConnectedArea",
            {
            "trigger": NotRequired[typing.Union[bool, str]]
        }
    )

    RecentlyTooltipChangeRecord = TypedDict(
        "RecentlyTooltipChangeRecord",
            {
            "timestamp": NotRequired[typing.Union[int, float, numbers.Number]],
            "data": NotRequired[typing.Sequence[dict]]
        }
    )

    RecentlyColumnClickRecord = TypedDict(
        "RecentlyColumnClickRecord",
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
        style: typing.Optional[dict] = None,
        data: typing.Optional[typing.Sequence[dict]] = None,
        meta: typing.Optional[typing.Any] = None,
        xField: typing.Optional[str] = None,
        yField: typing.Optional[str] = None,
        seriesField: typing.Optional[str] = None,
        groupField: typing.Optional[str] = None,
        isStack: typing.Optional[bool] = None,
        isGroup: typing.Optional[bool] = None,
        isRange: typing.Optional[bool] = None,
        isPercent: typing.Optional[bool] = None,
        color: typing.Optional[typing.Union[str, typing.Sequence[str], "Color"]] = None,
        columnStyle: typing.Optional[typing.Union[typing.Any, "ColumnStyle"]] = None,
        slider: typing.Optional[typing.Any] = None,
        intervalPadding: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        dodgePadding: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minColumnWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        maxColumnWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        columnBackground: typing.Optional["ColumnBackground"] = None,
        columnWidthRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        marginRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        scrollbar: typing.Optional[typing.Any] = None,
        conversionTag: typing.Optional["ConversionTag"] = None,
        connectedArea: typing.Optional[typing.Union["ConnectedArea", bool]] = None,
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
        recentlyColumnClickRecord: typing.Optional["RecentlyColumnClickRecord"] = None,
        recentlyLegendInfo: typing.Optional["RecentlyLegendInfo"] = None,
        downloadTrigger: typing.Optional[str] = None,
        theme: typing.Optional[typing.Any] = None,
        pattern: typing.Optional[typing.Any] = None,
        interactions: typing.Optional[typing.Any] = None,
        state: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'groupField', 'isStack', 'isGroup', 'isRange', 'isPercent', 'color', 'columnStyle', 'slider', 'intervalPadding', 'dodgePadding', 'minColumnWidth', 'maxColumnWidth', 'columnBackground', 'columnWidthRatio', 'marginRatio', 'scrollbar', 'conversionTag', 'connectedArea', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyColumnClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'groupField', 'isStack', 'isGroup', 'isRange', 'isPercent', 'color', 'columnStyle', 'slider', 'intervalPadding', 'dodgePadding', 'minColumnWidth', 'maxColumnWidth', 'columnBackground', 'columnWidthRatio', 'marginRatio', 'scrollbar', 'conversionTag', 'connectedArea', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyColumnClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdColumn, self).__init__(**args)
