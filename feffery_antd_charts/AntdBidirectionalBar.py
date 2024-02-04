# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdBidirectionalBar(Component):
    """An AntdBidirectionalBar component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- barStyle (dict; optional)

    `barStyle` is a dict with keys:

    - func (string; optional)

- className (string; optional)

- data (list of dicts; required)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- interactions (optional):
    交互功能项配置.

- key (string; optional)

- label (optional)

- layout (a value equal to: 'horizontal', 'vertical'; optional)

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

- recentlyBarClickRecord (dict; optional)

    `recentlyBarClickRecord` is a dict with keys:

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

- state (optional):
    状态样式配置.

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (optional)

- yField (list of strings; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdBidirectionalBar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, layout=Component.UNDEFINED, barStyle=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyBarClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'barStyle', 'className', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'label', 'layout', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'recentlyBarClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'barStyle', 'className', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'label', 'layout', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'recentlyBarClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdBidirectionalBar, self).__init__(**args)
