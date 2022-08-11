# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTreemap(Component):
    """An AntdTreemap component.


Keyword arguments:

- id (string; optional)

- annotations (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- colorField (string; required)

- data (dict; optional)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

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

- locale (a value equal to: 'zh-CN', 'en-US'; optional)

- meta (optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- rawFields (list of strings; optional)

- rectStyle (dict; optional)

    `rectStyle` is a dict with keys:

    - func (string; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdTreemap'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, meta=Component.UNDEFINED, colorField=Component.REQUIRED, rawFields=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, rectStyle=Component.UNDEFINED, color=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'height', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'rawFields', 'rectStyle', 'renderer', 'style', 'theme', 'tooltip', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'height', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'rawFields', 'rectStyle', 'renderer', 'style', 'theme', 'tooltip', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['colorField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdTreemap, self).__init__(**args)
