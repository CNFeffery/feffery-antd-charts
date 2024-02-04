# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdHistogram(Component):
    """An AntdHistogram component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- binField (string; required)

- binNumber (number; optional)

- binWidth (number; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- columnStyle (dict; optional)

    `columnStyle` is a dict with keys:

    - func (string; optional)

- data (list of dicts; required)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- interactions (optional):
    交互功能项配置.

- key (string; optional)

- label (optional)

- legend (optional)

- limitInPlot (boolean; optional)

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

- padding (number | list of numbers | string; optional)

- pattern (optional):
    配置图形填充贴图样式.

- recentlyAreaClickRecord (dict; optional)

    `recentlyAreaClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- recentlyLegendInfo (dict; optional)

    `recentlyLegendInfo` is a dict with keys:

    - items (list of dicts; optional)

    - triggerItemName (boolean | number | string | dict | list; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- stackField (string; optional)

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
    _type = 'AntdHistogram'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, binField=Component.REQUIRED, stackField=Component.UNDEFINED, binWidth=Component.UNDEFINED, binNumber=Component.UNDEFINED, color=Component.UNDEFINED, columnStyle=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyAreaClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'binField', 'binNumber', 'binWidth', 'className', 'color', 'columnStyle', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'stackField', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'yAxis']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'binField', 'binNumber', 'binWidth', 'className', 'color', 'columnStyle', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'stackField', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'yAxis']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['binField', 'data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdHistogram, self).__init__(**args)
