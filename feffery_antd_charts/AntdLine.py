# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdLine(Component):
    """An AntdLine component.


Keyword arguments:

- id (string; optional)

- annotations (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- connectNulls (boolean; optional)

- data (list of dicts; required)

- downloadTrigger (string; optional)

- height (number; optional)

- isStack (boolean; optional)

- key (string; optional)

- label (optional)

- legend (optional)

- lineStyle (dict; optional)

    `lineStyle` is a dict with keys:

    - func (string; optional)

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

- recentlyPointClickRecord (dict; optional)

    `recentlyPointClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- seriesField (string; optional)

- slider (optional)

- smooth (boolean; optional)

- stepType (string; optional)

- style (dict; optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (optional)

- yField (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdLine'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, seriesField=Component.UNDEFINED, smooth=Component.UNDEFINED, stepType=Component.UNDEFINED, connectNulls=Component.UNDEFINED, isStack=Component.UNDEFINED, color=Component.UNDEFINED, lineStyle=Component.UNDEFINED, point=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, slider=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyPointClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'connectNulls', 'data', 'downloadTrigger', 'height', 'isStack', 'key', 'label', 'legend', 'lineStyle', 'loading_state', 'locale', 'meta', 'padding', 'point', 'recentlyPointClickRecord', 'recentlyTooltipChangeRecord', 'renderer', 'seriesField', 'slider', 'smooth', 'stepType', 'style', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'connectNulls', 'data', 'downloadTrigger', 'height', 'isStack', 'key', 'label', 'legend', 'lineStyle', 'loading_state', 'locale', 'meta', 'padding', 'point', 'recentlyPointClickRecord', 'recentlyTooltipChangeRecord', 'renderer', 'seriesField', 'slider', 'smooth', 'stepType', 'style', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdLine, self).__init__(**args)
