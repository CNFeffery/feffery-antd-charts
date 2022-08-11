# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdBar(Component):
    """An AntdBar component.


Keyword arguments:

- id (string; optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- barBackground (dict; optional)

    `barBackground` is a dict with keys:

    - style (optional)

- barStyle (dict; optional)

    `barStyle` is a dict with keys:

    - func (string; optional)

- barWidthRatio (number; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- connectedArea (dict; optional)

    `connectedArea` is a dict with keys:

    - trigger (boolean | string; optional) | boolean

- conversionTag (dict; optional)

    `conversionTag` is a dict with keys:

    - arrow (dict; optional)

        `arrow` is a boolean

      Or dict with keys:

        - headSize (number; optional)

    - offset (number; optional)

    - size (number; optional)

    - spacing (number; optional)

    - text (dict; optional)

        `text` is a boolean | dict with keys:

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - style (optional)

- data (list of dicts; required)

- dodgePadding (number; optional)

- downloadTrigger (string; default 'download-trigger')

- groupField (string; optional)

- height (number; optional)

- intervalPadding (number; optional)

- isGroup (boolean; optional)

- isPercent (boolean; optional)

- isRange (boolean; optional)

- isStack (boolean; optional)

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

- locale (string; optional)

- marginRatio (number; optional)

- maxBarWidth (number; optional)

- meta (optional)

- minBarWidth (number; optional)

- padding (number | list of numbers | string; optional)

- renderer (string; optional)

- scrollbar (optional)

- seriesField (string; optional)

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (optional)

- yField (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdBar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, seriesField=Component.UNDEFINED, groupField=Component.UNDEFINED, isStack=Component.UNDEFINED, isGroup=Component.UNDEFINED, isRange=Component.UNDEFINED, isPercent=Component.UNDEFINED, color=Component.UNDEFINED, intervalPadding=Component.UNDEFINED, dodgePadding=Component.UNDEFINED, minBarWidth=Component.UNDEFINED, maxBarWidth=Component.UNDEFINED, barStyle=Component.UNDEFINED, barBackground=Component.UNDEFINED, barWidthRatio=Component.UNDEFINED, marginRatio=Component.UNDEFINED, scrollbar=Component.UNDEFINED, conversionTag=Component.UNDEFINED, connectedArea=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'appendPadding', 'autoFit', 'barBackground', 'barStyle', 'barWidthRatio', 'className', 'color', 'connectedArea', 'conversionTag', 'data', 'dodgePadding', 'downloadTrigger', 'groupField', 'height', 'intervalPadding', 'isGroup', 'isPercent', 'isRange', 'isStack', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'marginRatio', 'maxBarWidth', 'meta', 'minBarWidth', 'padding', 'renderer', 'scrollbar', 'seriesField', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'appendPadding', 'autoFit', 'barBackground', 'barStyle', 'barWidthRatio', 'className', 'color', 'connectedArea', 'conversionTag', 'data', 'dodgePadding', 'downloadTrigger', 'groupField', 'height', 'intervalPadding', 'isGroup', 'isPercent', 'isRange', 'isStack', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'marginRatio', 'maxBarWidth', 'meta', 'minBarWidth', 'padding', 'renderer', 'scrollbar', 'seriesField', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdBar, self).__init__(**args)
