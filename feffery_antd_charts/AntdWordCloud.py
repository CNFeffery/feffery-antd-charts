# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdWordCloud(Component):
    """An AntdWordCloud component.


Keyword arguments:

- id (string; optional)

- annotations (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- colorField (string; optional)

- data (list of dicts; optional)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- imageMask (string; optional)

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

- placementStrategy (dict; optional)

    `placementStrategy` is a dict with keys:

    - func (string; optional)

- recentlyWordClickRecord (dict; optional)

    `recentlyWordClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- spiral (a value equal to: 'archimedean', 'rectangular'; optional)

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- weightField (string; required)

- width (number; optional)

- wordField (string; required)

- wordStyle (dict; optional)

    `wordStyle` is a dict with keys:

    - fontFamily (string; optional)

    - fontSize (list of numbers; optional)

    - fontWeight (string; optional)

    - padding (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdWordCloud'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, meta=Component.UNDEFINED, wordField=Component.REQUIRED, weightField=Component.REQUIRED, colorField=Component.UNDEFINED, spiral=Component.UNDEFINED, placementStrategy=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, wordStyle=Component.UNDEFINED, imageMask=Component.UNDEFINED, color=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, recentlyWordClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'height', 'imageMask', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'placementStrategy', 'recentlyWordClickRecord', 'renderer', 'spiral', 'style', 'theme', 'tooltip', 'weightField', 'width', 'wordField', 'wordStyle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'height', 'imageMask', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'placementStrategy', 'recentlyWordClickRecord', 'renderer', 'spiral', 'style', 'theme', 'tooltip', 'weightField', 'width', 'wordField', 'wordStyle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['weightField', 'wordField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdWordCloud, self).__init__(**args)
