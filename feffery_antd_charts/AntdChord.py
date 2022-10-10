# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdChord(Component):
    """An AntdChord component.


Keyword arguments:

- id (string; optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- data (list of dicts; optional)

- downloadTrigger (string; default 'download-trigger')

- edgeStyle (dict; optional)

    `edgeStyle` is a dict with keys:

    - func (string; optional)

- height (number; optional)

- key (string; optional)

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

- nodePaddingRatio (number; optional)

- nodeStyle (dict; optional)

    `nodeStyle` is a dict with keys:

    - func (string; optional)

- nodeWidthRatio (number; optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- sourceField (string; optional)

- style (dict; optional)

- targetField (string; optional)

- theme (optional)

- weightField (string; optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdChord'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, meta=Component.UNDEFINED, sourceField=Component.UNDEFINED, targetField=Component.UNDEFINED, weightField=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, nodeStyle=Component.UNDEFINED, edgeStyle=Component.UNDEFINED, nodeWidthRatio=Component.UNDEFINED, nodePaddingRatio=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'appendPadding', 'autoFit', 'className', 'data', 'downloadTrigger', 'edgeStyle', 'height', 'key', 'limitInPlot', 'loading_state', 'locale', 'meta', 'nodePaddingRatio', 'nodeStyle', 'nodeWidthRatio', 'padding', 'renderer', 'sourceField', 'style', 'targetField', 'theme', 'weightField', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'appendPadding', 'autoFit', 'className', 'data', 'downloadTrigger', 'edgeStyle', 'height', 'key', 'limitInPlot', 'loading_state', 'locale', 'meta', 'nodePaddingRatio', 'nodeStyle', 'nodeWidthRatio', 'padding', 'renderer', 'sourceField', 'style', 'targetField', 'theme', 'weightField', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdChord, self).__init__(**args)
