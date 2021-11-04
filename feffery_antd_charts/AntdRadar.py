# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdRadar(Component):
    """An AntdRadar component.


Keyword arguments:

- id (string; optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- area (dict; optional)

    `area` is a dict with keys:

    - color (dict; optional)

        `color` is a string

      Or list of strings | dict with keys:

        - func (string; optional)

    - smooth (boolean; optional)

    - style (dict; optional)

        `style` is a dict with keys:

        - func (string; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- data (list of dicts; required)

- endAngle (number; optional)

- height (number; optional)

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

- locale (string; optional)

- meta (optional)

- padding (number | list of numbers | string; optional)

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

- radius (number; optional)

- renderer (string; optional)

- seriesField (string; optional)

- smooth (boolean; optional)

- startAngle (number; optional)

- style (dict; optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (optional)

- yField (string; required)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, seriesField=Component.UNDEFINED, smooth=Component.UNDEFINED, radius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, color=Component.UNDEFINED, lineStyle=Component.UNDEFINED, point=Component.UNDEFINED, area=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'appendPadding', 'area', 'autoFit', 'className', 'color', 'data', 'endAngle', 'height', 'label', 'legend', 'lineStyle', 'loading_state', 'locale', 'meta', 'padding', 'point', 'radius', 'renderer', 'seriesField', 'smooth', 'startAngle', 'style', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._type = 'AntdRadar'
        self._namespace = 'feffery_antd_charts'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'appendPadding', 'area', 'autoFit', 'className', 'color', 'data', 'endAngle', 'height', 'label', 'legend', 'lineStyle', 'loading_state', 'locale', 'meta', 'padding', 'point', 'radius', 'renderer', 'seriesField', 'smooth', 'startAngle', 'style', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdRadar, self).__init__(**args)
