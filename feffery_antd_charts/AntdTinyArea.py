# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTinyArea(Component):
    """An AntdTinyArea component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers; optional)

- areaStyle (optional):
    设置面积区域样式.

- autoFit (boolean; optional)

- className (string; optional)

- color (string; optional)

- data (list of numbers; required)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- interactions (optional):
    交互功能项配置.

- key (string; optional)

- limitInPlot (boolean; optional)

- line (dict; optional):
    配置折线样式.

    `line` is a dict with keys:

    - color (string; optional):
        设置折线颜色.

    - style (optional):
        设置折线样式.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- meta (optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- pattern (optional):
    配置图形填充贴图样式.

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- point (dict; optional):
    配置折点样式.

    `point` is a dict with keys:

    - color (string; optional):
        设置折点颜色.

    - style (optional):
        设置折点样式.

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- smooth (boolean; optional)

- state (optional):
    状态样式配置.

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- yAxis (optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdTinyArea'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, smooth=Component.UNDEFINED, color=Component.UNDEFINED, areaStyle=Component.UNDEFINED, line=Component.UNDEFINED, point=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, pattern=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'areaStyle', 'autoFit', 'className', 'color', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'limitInPlot', 'line', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'pixelRatio', 'point', 'recentlyTooltipChangeRecord', 'renderer', 'smooth', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'yAxis']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'areaStyle', 'autoFit', 'className', 'color', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'limitInPlot', 'line', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'pixelRatio', 'point', 'recentlyTooltipChangeRecord', 'renderer', 'smooth', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'yAxis']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdTinyArea, self).__init__(**args)
