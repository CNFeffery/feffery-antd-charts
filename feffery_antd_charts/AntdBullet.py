# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AntdBullet(Component):
    """An AntdBullet component.
子弹图组件AntdBullet

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- data (list of dicts; required):
    必填，定义绘图所需数据，格式如`[{title: '满意度', ranges: [50, 100], measures: [80],
    target: 85}]`.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- measureField (string; required):
    必填，子弹图长度字段.

- rangeField (string; required):
    必填，子弹图背景条字段.

- targetField (string; required):
    必填，子弹图目标值字段.

- xField (string; optional):
    必填，子弹图分组字段.

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

- layout (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    布局方向，可选项有`'horizontal'`、`'vertical'`  默认值：`'horizontal'`.

- color (dict; optional):
    控制子弹图各部分填充颜色，具体见在线文档相关说明.

    `color` is a dict with keys:

    - range (string | list of strings; optional):
        区间背景颜色.

    - measure (string | list of strings; optional):
        实际值颜色.

    - target (string | list of strings; optional):
        目标值颜色.

- size (dict; optional):
    配置子弹图各部分尺寸，具体见在线文档相关说明.

    `size` is a dict with keys:

    - range (dict; optional):
        区间背景像素尺寸.

        `range` is a number

      Or list of numbers | dict with keys:

        - func (string; optional):

            js函数体字符串.

    - measure (dict; optional):
        实际值像素尺寸.

        `measure` is a number | list of numbers | dict with keys:

        - func (string; optional):

            js函数体字符串.

    - target (dict; optional):
        目标值像素尺寸.

        `target` is a number | list of numbers | dict with keys:

        - func (string; optional):

            js函数体字符串.

- bulletStyle (dict; optional):
    控制子弹图各部分样式，具体见在线文档相关说明.

    `bulletStyle` is a dict with keys:

    - range (dict; optional):
        区间背景样式.

        `range` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - measure (dict; optional):
        实际值样式.

        `measure` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - target (dict; optional):
        目标值样式.

        `target` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

- label (dict; optional):
    配置子弹图各部分数值标签，具体见在线文档相关说明.

    `label` is a dict with keys:

    - range (optional):
        区间数值标签.

    - measure (optional):
        实际值标签.

    - target (optional):
        目标值标签.

- tooltip (optional):
    配置信息框相关参数，具体见在线文档相关说明.

- legend (optional):
    配置图例相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

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
    _type = 'AntdBullet'
    Color = TypedDict(
        "Color",
            {
            "range": NotRequired[typing.Union[str, typing.Sequence[str]]],
            "measure": NotRequired[typing.Union[str, typing.Sequence[str]]],
            "target": NotRequired[typing.Union[str, typing.Sequence[str]]]
        }
    )

    SizeRange = TypedDict(
        "SizeRange",
            {
            "func": NotRequired[str]
        }
    )

    SizeMeasure = TypedDict(
        "SizeMeasure",
            {
            "func": NotRequired[str]
        }
    )

    SizeTarget = TypedDict(
        "SizeTarget",
            {
            "func": NotRequired[str]
        }
    )

    Size = TypedDict(
        "Size",
            {
            "range": NotRequired[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]], "SizeRange"]],
            "measure": NotRequired[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]], "SizeMeasure"]],
            "target": NotRequired[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]], "SizeTarget"]]
        }
    )

    BulletStyleRange = TypedDict(
        "BulletStyleRange",
            {
            "func": NotRequired[str]
        }
    )

    BulletStyleMeasure = TypedDict(
        "BulletStyleMeasure",
            {
            "func": NotRequired[str]
        }
    )

    BulletStyleTarget = TypedDict(
        "BulletStyleTarget",
            {
            "func": NotRequired[str]
        }
    )

    BulletStyle = TypedDict(
        "BulletStyle",
            {
            "range": NotRequired[typing.Union[typing.Any, "BulletStyleRange"]],
            "measure": NotRequired[typing.Union[typing.Any, "BulletStyleMeasure"]],
            "target": NotRequired[typing.Union[typing.Any, "BulletStyleTarget"]]
        }
    )

    Label = TypedDict(
        "Label",
            {
            "range": NotRequired[typing.Any],
            "measure": NotRequired[typing.Any],
            "target": NotRequired[typing.Any]
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
        measureField: typing.Optional[str] = None,
        rangeField: typing.Optional[str] = None,
        targetField: typing.Optional[str] = None,
        xField: typing.Optional[str] = None,
        xAxis: typing.Optional[typing.Any] = None,
        yAxis: typing.Optional[typing.Any] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        autoFit: typing.Optional[bool] = None,
        padding: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]], Literal["auto"]]] = None,
        appendPadding: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]]]] = None,
        renderer: typing.Optional[Literal["canvas", "svg"]] = None,
        pixelRatio: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        locale: typing.Optional[Literal["zh-CN", "en-US"]] = None,
        limitInPlot: typing.Optional[bool] = None,
        layout: typing.Optional[Literal["horizontal", "vertical"]] = None,
        color: typing.Optional["Color"] = None,
        size: typing.Optional["Size"] = None,
        bulletStyle: typing.Optional["BulletStyle"] = None,
        label: typing.Optional["Label"] = None,
        tooltip: typing.Optional[typing.Any] = None,
        legend: typing.Optional[typing.Any] = None,
        animation: typing.Optional[typing.Any] = None,
        downloadTrigger: typing.Optional[str] = None,
        theme: typing.Optional[typing.Any] = None,
        interactions: typing.Optional[typing.Any] = None,
        state: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'measureField', 'rangeField', 'targetField', 'xField', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'layout', 'color', 'size', 'bulletStyle', 'label', 'tooltip', 'legend', 'animation', 'downloadTrigger', 'theme', 'interactions', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'measureField', 'rangeField', 'targetField', 'xField', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'layout', 'color', 'size', 'bulletStyle', 'label', 'tooltip', 'legend', 'animation', 'downloadTrigger', 'theme', 'interactions', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'measureField', 'rangeField', 'targetField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdBullet, self).__init__(**args)
