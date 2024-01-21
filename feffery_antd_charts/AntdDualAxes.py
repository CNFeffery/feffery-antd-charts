# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdDualAxes(Component):
    """An AntdDualAxes component.


Keyword arguments:

- id (string; optional)

- animation (dict | boolean; optional)

- annotations (dict with strings as keys and values of type ; optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- data (list of list of dictss; required)

- downloadTrigger (string; default 'download-trigger')

- geometryOptions (list of dicts; optional)

    `geometryOptions` is a list of dicts with keys:

    - color (dict; optional)

        `color` is a string

      Or list of strings | dict with keys:

        - func (string; optional)

    - connectNulls (boolean; optional)

    - geometry (a value equal to: 'line', 'column'; optional)

    - label (optional)

    - lineStyle (dict; optional)

        `lineStyle` is a dict with keys:

        - func (string; optional)

    - point (dict; optional)

        `point` is a dict with keys:

        - color (dict; optional)

            `color` is a string

          Or list of strings | dict with keys:

    - func (string; optional)

        - shape (dict; optional)

            `shape` is a string | dict with keys:

    - func (string; optional)

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional)

    - seriesField (string; optional)

    - smooth (boolean; optional) | dict with keys:

    - color (dict; optional)

        `color` is a string | list of strings | dict with keys:

        - func (string; optional)

    - columnStyle (dict; optional)

        `columnStyle` is a dict with keys:

        - func (string; optional)

    - columnWidthRatio (number; optional)

    - geometry (a value equal to: 'line', 'column'; optional)

    - groupField (string; optional)

    - isGroup (boolean; optional)

    - isStack (boolean; optional)

    - label (optional)

    - marginRatio (number; optional)

    - seriesField (string; optional)

- height (number; optional)

- interactions (list; optional)

- key (string; optional)

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

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- recentlyClickRecord (dict; optional)

    `recentlyClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- slider (optional)

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (dict with strings as keys and values of type ; optional)

- yField (list of strings; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdDualAxes'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, geometryOptions=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, tooltip=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, annotations=Component.UNDEFINED, legend=Component.UNDEFINED, slider=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'data', 'downloadTrigger', 'geometryOptions', 'height', 'interactions', 'key', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'recentlyClickRecord', 'renderer', 'slider', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'data', 'downloadTrigger', 'geometryOptions', 'height', 'interactions', 'key', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'recentlyClickRecord', 'renderer', 'slider', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdDualAxes, self).__init__(**args)
