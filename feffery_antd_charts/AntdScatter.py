# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdScatter(Component):
    """An AntdScatter component.


Keyword arguments:

- id (string; optional)

- animation (dict | boolean; optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- colorField (string; optional)

- data (list of dicts; required)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- interactions (list; optional)

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

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- meta (optional)

- padding (number | list of numbers | string; optional)

- pointStyle (dict; optional)

    `pointStyle` is a dict with keys:

    - func (string; optional)

- quadrant (dict; optional)

    `quadrant` is a dict with keys:

    - labels (list of dicts; optional)

        `labels` is a list of dicts with keys:

        - content (string; optional)

        - position (list of numbers; optional)

        - style (optional)

    - lineStyle (optional)

    - regionStyle (list; optional)

    - xBaseline (number; optional)

    - yBaseline (number; optional)

- recentlyLegendInfo (dict; optional)

    `recentlyLegendInfo` is a dict with keys:

    - items (list of dicts; optional)

    - triggerItemName (boolean | number | string | dict | list; optional)

- recentlyPointClickRecord (dict; optional)

    `recentlyPointClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- regressionLine (dict; optional)

    `regressionLine` is a dict with keys:

    - algorithm (dict; optional)

        `algorithm` is a dict with keys:

        - func (string; optional)

    - style (optional)

    - top (boolean; optional)

    - type (a value equal to: 'exp', 'linear', 'loess', 'log', 'poly', 'pow', 'quad'; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- shape (dict; optional)

    `shape` is a string | list of strings | dict with keys:

    - func (string; optional)

- shapeField (string; optional)

- shapeLegend (optional)

- size (dict; optional)

    `size` is a number | list of numbers | dict with keys:

    - func (string; optional)

- sizeField (string; optional)

- sizeLegend (optional)

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
    _type = 'AntdScatter'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, colorField=Component.UNDEFINED, sizeField=Component.UNDEFINED, shapeField=Component.UNDEFINED, color=Component.UNDEFINED, size=Component.UNDEFINED, shape=Component.UNDEFINED, pointStyle=Component.UNDEFINED, shapeLegend=Component.UNDEFINED, sizeLegend=Component.UNDEFINED, quadrant=Component.UNDEFINED, regressionLine=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyPointClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pointStyle', 'quadrant', 'recentlyLegendInfo', 'recentlyPointClickRecord', 'recentlyTooltipChangeRecord', 'regressionLine', 'renderer', 'shape', 'shapeField', 'shapeLegend', 'size', 'sizeField', 'sizeLegend', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pointStyle', 'quadrant', 'recentlyLegendInfo', 'recentlyPointClickRecord', 'recentlyTooltipChangeRecord', 'regressionLine', 'renderer', 'shape', 'shapeField', 'shapeLegend', 'size', 'sizeField', 'sizeLegend', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdScatter, self).__init__(**args)
