# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdWaterfall(Component):
    """An AntdWaterfall component.


Keyword arguments:

- id (string; optional)

- key (string; optional)

- className (string; optional)

- style (dict; optional)

- data (list of dicts; required):
    必填，用于定义绘图所需数据.

- meta (optional)

- xField (string; required):
    x轴对应字段.

- yField (string; required):
    y轴对应字段.

- labelMode (a value equal to: 'absolute', 'difference'; optional):
    设置数据模式，可选的有'absolute'、'difference'  默认：'difference'.

- total (dict; optional):
    配置总计值显示.

    `total` is a boolean | dict with keys:

    - label (string; optional):
        设置总计值柱体的标签.

    - style (optional):
        配置总计值柱体样式.

- leaderLine (dict; optional):
    配置牵引线显示.

    `leaderLine` is a boolean | dict with keys:

    - style (optional):
        配置牵引线样式.

- risingFill (string; optional):
    设置上涨色  默认：'#f4664a'.

- fallingFill (string; optional):
    设置下降色  默认：'#30bf78'.

- columnWidthRatio (number; optional):
    设置柱体宽度占比，取值应在0到1之间.

- color (dict; optional):
    配置柱体颜色.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- slider (optional)

- waterfallStyle (dict; optional):
    配置柱体样式.

    `waterfallStyle` is a dict with keys:

    - func (string; optional)

- xAxis (optional)

- yAxis (optional)

- width (number; optional)

- height (number; optional)

- autoFit (boolean; optional)

- padding (number | list of numbers | string; optional)

- appendPadding (number | list of numbers | string; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- limitInPlot (boolean; optional)

- label (optional)

- tooltip (optional)

- annotations (optional)

- animation (optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (list of dicts; optional)

- recentlyColumnClickRecord (dict; optional)

    `recentlyColumnClickRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (dict; optional)

- downloadTrigger (string; default 'download-trigger')

- theme (optional)

- interactions (optional):
    交互功能项配置.

- state (optional):
    状态样式配置.

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
    _type = 'AntdWaterfall'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, labelMode=Component.UNDEFINED, total=Component.UNDEFINED, leaderLine=Component.UNDEFINED, risingFill=Component.UNDEFINED, fallingFill=Component.UNDEFINED, columnWidthRatio=Component.UNDEFINED, color=Component.UNDEFINED, slider=Component.UNDEFINED, waterfallStyle=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyColumnClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'labelMode', 'total', 'leaderLine', 'risingFill', 'fallingFill', 'columnWidthRatio', 'color', 'slider', 'waterfallStyle', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyColumnClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'labelMode', 'total', 'leaderLine', 'risingFill', 'fallingFill', 'columnWidthRatio', 'color', 'slider', 'waterfallStyle', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyColumnClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdWaterfall, self).__init__(**args)
