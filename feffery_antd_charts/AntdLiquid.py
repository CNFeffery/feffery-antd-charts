# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AntdLiquid(Component):
    """An AntdLiquid component.
水波图组件AntdLiquid

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- style (dict; optional):
    css样式.

- percent (number; required):
    当前水波图实际值，取值应在`0`到`1`之间.

- radius (number; default 0.9):
    水波图相对画布的外环半径尺寸，取值应在`0`到`1`之间  默认值：`0.9`.

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

- liquidStyle (dict; optional):
    控制水波图样式，具体见在线文档相关说明.

    `liquidStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- shape (a value equal to: 'circle', 'diamond', 'triangle', 'pin', 'rect'; default 'circle'):
    水波图形状，可选项有`'circle'`、`'diamond'`、`'triangle'`、`'pin'`、`'rect'
    默认值：`'circle'`.

- color (dict; optional):
    控制水波图颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- outline (dict; optional):
    配置水波图外轮廓，具体见在线文档相关说明.

    `outline` is a dict with keys:

    - border (number; optional):
        水波图外轮廓像素宽度  默认值：`2`.

    - distance (number; optional):
        水波图外轮廓与内部波形之间的像素间距  默认值：`0`.

    - style (dict; optional):
        配置水波图外轮廓.

        `style` is a dict with keys:

        - stroke (string; optional):
            外轮廓填充色.

        - strokeOpacity (number; optional):
            外轮廓填充透明度.

- wave (dict; optional):
    配置水波图波形，具体见在线文档相关说明.

    `wave` is a dict with keys:

    - count (number; optional):
        水波数量  默认值：`3`.

    - length (number; optional):
        水波像素长度  默认值：`192`.

- statistic (dict; optional):
    配置水波图中心统计内容，具体见在线文档相关说明.

    `statistic` is a boolean | dict with keys:

    - title (dict; optional):
        配置统计内容标题，设置为`False`时将隐藏标题.

        `title` is a boolean

      Or dict with keys:

        - style (dict; optional):

            统计内容标题样式.

        - content (string; optional):

            配置统计内容标题文本.

        - formatter (dict; optional):

            格式化统计内容标题文本函数.

            `formatter` is a dict with keys:

            - func (string; optional)

        - customHtml (dict; optional):

            配置统计内容标题原始html文本内容.

            `customHtml` is a dict with keys:

            - func (string; optional)

        - rotate (number; optional):

            标题旋转角度.

        - offsetX (number; optional):

            标题水平像素偏移.

        - offsetY (number; optional):

            标题竖直像素偏移.

    - content (dict; optional):
        配置统计内容，设置为`False`时将隐藏内容.

        `content` is a boolean | dict with keys:

        - style (dict; optional):

            统计内容样式.

        - content (string; optional):

            配置统计内容文本.

        - formatter (dict; optional):

            格式化统计内容文本函数.

            `formatter` is a dict with keys:

            - func (string; optional)

        - customHtml (dict; optional):

            配置统计内容原始html文本内容.

            `customHtml` is a dict with keys:

            - func (string; optional):

                js函数体字符串.

        - rotate (number; optional):

            标题旋转角度.

        - offsetX (number; optional):

            标题水平像素偏移.

        - offsetY (number; optional):

            标题竖直像素偏移.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

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
    _type = 'AntdLiquid'
    LiquidStyle = TypedDict(
        "LiquidStyle",
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

    OutlineStyle = TypedDict(
        "OutlineStyle",
            {
            "stroke": NotRequired[str],
            "strokeOpacity": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Outline = TypedDict(
        "Outline",
            {
            "border": NotRequired[typing.Union[int, float, numbers.Number]],
            "distance": NotRequired[typing.Union[int, float, numbers.Number]],
            "style": NotRequired["OutlineStyle"]
        }
    )

    Wave = TypedDict(
        "Wave",
            {
            "count": NotRequired[typing.Union[int, float, numbers.Number]],
            "length": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    StatisticTitleFormatter = TypedDict(
        "StatisticTitleFormatter",
            {
            "func": NotRequired[str]
        }
    )

    StatisticTitleCustomHtml = TypedDict(
        "StatisticTitleCustomHtml",
            {
            "func": NotRequired[str]
        }
    )

    StatisticTitle = TypedDict(
        "StatisticTitle",
            {
            "style": NotRequired[dict],
            "content": NotRequired[str],
            "formatter": NotRequired["StatisticTitleFormatter"],
            "customHtml": NotRequired["StatisticTitleCustomHtml"],
            "rotate": NotRequired[typing.Union[int, float, numbers.Number]],
            "offsetX": NotRequired[typing.Union[int, float, numbers.Number]],
            "offsetY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    StatisticContentFormatter = TypedDict(
        "StatisticContentFormatter",
            {
            "func": NotRequired[str]
        }
    )

    StatisticContentCustomHtml = TypedDict(
        "StatisticContentCustomHtml",
            {
            "func": NotRequired[str]
        }
    )

    StatisticContent = TypedDict(
        "StatisticContent",
            {
            "style": NotRequired[dict],
            "content": NotRequired[str],
            "formatter": NotRequired["StatisticContentFormatter"],
            "customHtml": NotRequired["StatisticContentCustomHtml"],
            "rotate": NotRequired[typing.Union[int, float, numbers.Number]],
            "offsetX": NotRequired[typing.Union[int, float, numbers.Number]],
            "offsetY": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Statistic = TypedDict(
        "Statistic",
            {
            "title": NotRequired[typing.Union[bool, "StatisticTitle"]],
            "content": NotRequired[typing.Union[bool, "StatisticContent"]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[dict] = None,
        percent: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        radius: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        autoFit: typing.Optional[bool] = None,
        padding: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]], Literal["auto"]]] = None,
        appendPadding: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]]]] = None,
        renderer: typing.Optional[Literal["canvas", "svg"]] = None,
        pixelRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        locale: typing.Optional[Literal["zh-CN", "en-US"]] = None,
        limitInPlot: typing.Optional[bool] = None,
        liquidStyle: typing.Optional[typing.Union[typing.Any, "LiquidStyle"]] = None,
        shape: typing.Optional[Literal["circle", "diamond", "triangle", "pin", "rect"]] = None,
        color: typing.Optional[typing.Union[str, typing.Sequence[str], "Color"]] = None,
        outline: typing.Optional["Outline"] = None,
        wave: typing.Optional["Wave"] = None,
        statistic: typing.Optional[typing.Union[bool, "Statistic"]] = None,
        animation: typing.Optional[typing.Any] = None,
        downloadTrigger: typing.Optional[str] = None,
        theme: typing.Optional[typing.Any] = None,
        pattern: typing.Optional[typing.Any] = None,
        interactions: typing.Optional[typing.Any] = None,
        state: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'percent', 'radius', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'liquidStyle', 'shape', 'color', 'outline', 'wave', 'statistic', 'animation', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'percent', 'radius', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'liquidStyle', 'shape', 'color', 'outline', 'wave', 'statistic', 'animation', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['percent']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdLiquid, self).__init__(**args)
