# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AntdRingProgress(Component):
    """An AntdRingProgress component.
进度环图组件AntdRingProgress

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- percent (number; required):
    当前进度实际值，取值应在`0`到`1`之间.

- radius (number; optional):
    外环半径尺寸，取值应在`0`到`1`之间.

- innerRadius (number; optional):
    内环半径尺寸，取值应在`0`到`1`之间.

- color (dict; optional):
    控制进度环形填充颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- progressStyle (dict; optional):
    控制进度环形样式，具体见在线文档相关说明.

    `progressStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

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

- annotations (optional):
    配置标注相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

- statistic (dict; optional):
    配置饼图中心统计内容，具体见在线文档相关说明.

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

            - func (string; optional):

                js函数体字符串.

        - customHtml (dict; optional):

            配置统计内容标题原始html文本内容.

            `customHtml` is a dict with keys:

            - func (string; optional):

                js函数体字符串.

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

            - func (string; optional):

                js函数体字符串.

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

    - style (optional)

- downloadTrigger (string; default 'download-trigger'):
    对当前组件的`downloadTrigger`值进行更新，可实现主动下载当前图表为`png`格式图片.

- theme (optional):
    配置主题相关参数，具体见在线文档相关说明."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdRingProgress'
    Color = TypedDict(
        "Color",
            {
            "func": NotRequired[str]
        }
    )

    ProgressStyle = TypedDict(
        "ProgressStyle",
            {
            "func": NotRequired[str]
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
            "content": NotRequired[typing.Union[bool, "StatisticContent"]],
            "style": NotRequired[typing.Any]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        percent: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        radius: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        innerRadius: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        color: typing.Optional[typing.Union[str, typing.Sequence[str], "Color"]] = None,
        progressStyle: typing.Optional[typing.Union[typing.Any, "ProgressStyle"]] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        autoFit: typing.Optional[bool] = None,
        padding: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]], Literal["auto"]]] = None,
        appendPadding: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]]]] = None,
        renderer: typing.Optional[Literal["canvas", "svg"]] = None,
        pixelRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        locale: typing.Optional[Literal["zh-CN", "en-US"]] = None,
        limitInPlot: typing.Optional[bool] = None,
        annotations: typing.Optional[typing.Any] = None,
        animation: typing.Optional[typing.Any] = None,
        statistic: typing.Optional[typing.Union[bool, "Statistic"]] = None,
        downloadTrigger: typing.Optional[str] = None,
        theme: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'percent', 'radius', 'innerRadius', 'color', 'progressStyle', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'annotations', 'animation', 'statistic', 'downloadTrigger', 'theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'percent', 'radius', 'innerRadius', 'color', 'progressStyle', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'annotations', 'animation', 'statistic', 'downloadTrigger', 'theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['percent']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdRingProgress, self).__init__(**args)
