# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSankey(Component):
    """An AntdSankey component.


Keyword arguments:

- id (string; optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- data (list of dicts; optional)

- downloadTrigger (string; optional)

- edgeStyle (dict; optional)

    `edgeStyle` is a dict with keys:

    - func (string; optional)

- height (number; optional)

- key (string; optional)

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

- nodeAlign (a value equal to: 'left', 'right', 'center', 'justify'; optional)

- nodeDraggable (boolean; optional)

- nodePaddingRatio (number; optional)

- nodeStyle (dict; optional)

    `nodeStyle` is a dict with keys:

    - func (string; optional)

- nodeWidthRatio (number; optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- rawFields (list of strings; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- sourceField (string; optional)

- style (dict; optional)

- targetField (string; optional)

- weightField (string; optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdSankey'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, meta=Component.UNDEFINED, sourceField=Component.UNDEFINED, targetField=Component.UNDEFINED, weightField=Component.UNDEFINED, rawFields=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, nodeStyle=Component.UNDEFINED, edgeStyle=Component.UNDEFINED, color=Component.UNDEFINED, nodeWidthRatio=Component.UNDEFINED, nodePaddingRatio=Component.UNDEFINED, nodeAlign=Component.UNDEFINED, nodeDraggable=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'appendPadding', 'autoFit', 'className', 'color', 'data', 'downloadTrigger', 'edgeStyle', 'height', 'key', 'loading_state', 'locale', 'meta', 'nodeAlign', 'nodeDraggable', 'nodePaddingRatio', 'nodeStyle', 'nodeWidthRatio', 'padding', 'rawFields', 'renderer', 'sourceField', 'style', 'targetField', 'weightField', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'appendPadding', 'autoFit', 'className', 'color', 'data', 'downloadTrigger', 'edgeStyle', 'height', 'key', 'loading_state', 'locale', 'meta', 'nodeAlign', 'nodeDraggable', 'nodePaddingRatio', 'nodeStyle', 'nodeWidthRatio', 'padding', 'rawFields', 'renderer', 'sourceField', 'style', 'targetField', 'weightField', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdSankey, self).__init__(**args)
