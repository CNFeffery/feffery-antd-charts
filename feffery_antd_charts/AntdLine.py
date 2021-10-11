# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdLine(Component):
    """An AntdLine component.


Keyword arguments:

- id (string; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- connectNulls (boolean; optional)

- data (list of dicts; required)

- height (number; optional)

- isStack (boolean; optional)

- legend (dict; optional)

    `legend` is a dict with keys:

    - background (dict; optional)

        `background` is a dict with keys:

        - padding (number | list of numbers; optional)

    - flipPage (boolean; optional)

    - itemHeight (number; optional)

    - itemName (dict; optional)

        `itemName` is a dict with keys:

        - spacing (number; optional)

    - itemSpacing (number; optional)

    - itemValue (dict; optional)

        `itemValue` is a dict with keys:

        - alignRight (boolean; optional)

    - itemWidth (number; optional)

    - layout (string; optional)

    - maxHeight (number; optional)

    - maxWidth (number; optional)

    - offsetX (number; optional)

    - offsetY (number; optional)

    - position (string; optional)

    - reversed (boolean; optional)

    - selected (dict; optional) | boolean

- lineStyle (dict; optional)

    `lineStyle` is a string | dict with keys:

    - cursor (string; optional)

    - lineDash (list of numbers; optional)

    - lineOpacity (number; optional)

    - lineWidth (number; optional)

    - shadowBlur (number; optional)

    - shadowColor (string; optional)

    - shadowOffsetX (number; optional)

    - shadowOffsetY (number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (string; optional)

- padding (number | list of numbers; optional)

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

        - cursor (string; optional)

        - fill (string; optional)

        - fillOpacity (number; optional)

        - func (string; optional)

        - lineDash (list of numbers; optional)

        - lineWidth (number; optional)

        - r (number; optional)

        - stroke (string; optional)

        - strokeOpacity (number; optional)

- renderer (string; optional)

- seriesField (string; optional)

- smooth (boolean; optional)

- stepType (string; optional)

- style (dict; optional)

- tooltip (dict; optional)

    `tooltip` is a dict with keys:

    - enterable (boolean; optional)

    - fields (list of strings; optional)

    - follow (boolean; optional)

    - position (string; optional)

    - showTitle (boolean; optional)

    - title (string; optional)

- width (number; optional)

- xField (string; required)

- yField (string; required)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, xField=Component.REQUIRED, yField=Component.REQUIRED, seriesField=Component.UNDEFINED, smooth=Component.UNDEFINED, stepType=Component.UNDEFINED, connectNulls=Component.UNDEFINED, isStack=Component.UNDEFINED, color=Component.UNDEFINED, lineStyle=Component.UNDEFINED, point=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, legend=Component.UNDEFINED, tooltip=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoFit', 'className', 'color', 'connectNulls', 'data', 'height', 'isStack', 'legend', 'lineStyle', 'loading_state', 'locale', 'padding', 'point', 'renderer', 'seriesField', 'smooth', 'stepType', 'style', 'tooltip', 'width', 'xField', 'yField']
        self._type = 'AntdLine'
        self._namespace = 'feffery_antd_charts'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoFit', 'className', 'color', 'connectNulls', 'data', 'height', 'isStack', 'legend', 'lineStyle', 'loading_state', 'locale', 'padding', 'point', 'renderer', 'seriesField', 'smooth', 'stepType', 'style', 'tooltip', 'width', 'xField', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdLine, self).__init__(**args)
