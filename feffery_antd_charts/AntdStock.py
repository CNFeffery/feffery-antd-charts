# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdStock(Component):
    """An AntdStock component.


Keyword arguments:

- id (string; optional)

- annotations (optional)

- appendPadding (number | list of numbers | a value equal to: 'auto'; optional)

- autoFit (boolean; optional)

- className (string; optional)

- data (list of dicts with strings as keys and values of type string | number; required)

- fallingFill (string; default '#26a69a')

- height (number; optional)

- label (optional)

- legend (optional)

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

- renderer (a value equal to: 'canvas', 'svg'; optional)

- risingFill (string; default '#ef5350')

- slider (optional)

- stockStyle (dict; optional)

    `stockStyle` is a dict with keys:

    - func (string; optional)

- style (dict; optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (optional)

- yField (list of strings; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdStock'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, risingFill=Component.UNDEFINED, fallingFill=Component.UNDEFINED, stockStyle=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, slider=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'data', 'fallingFill', 'height', 'label', 'legend', 'loading_state', 'locale', 'meta', 'padding', 'renderer', 'risingFill', 'slider', 'stockStyle', 'style', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'data', 'fallingFill', 'height', 'label', 'legend', 'loading_state', 'locale', 'meta', 'padding', 'renderer', 'risingFill', 'slider', 'stockStyle', 'style', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdStock, self).__init__(**args)
