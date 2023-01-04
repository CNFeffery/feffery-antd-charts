# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdBullet(Component):
    """An AntdBullet component.


Keyword arguments:

- id (string; optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- bulletStyle (dict; optional)

    `bulletStyle` is a dict with keys:

    - measure (dict; optional)

        `measure` is a dict with keys:

        - func (string; optional)

    - range (dict; optional)

        `range` is a dict with keys:

        - func (string; optional)

    - target (dict; optional)

        `target` is a dict with keys:

        - func (string; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a dict with keys:

    - measure (string | list of strings; optional)

    - range (string | list of strings; optional)

    - target (string | list of strings; optional)

- data (list of dicts; required)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- key (string; optional)

- label (dict; optional)

    `label` is a dict with keys:

    - measure (optional)

    - range (optional)

    - target (optional)

- layout (a value equal to: 'horizontal', 'vertical'; default 'horizontal')

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

- measureField (string; required)

- meta (optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- rangeField (string; required)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- size (dict; optional)

    `size` is a dict with keys:

    - measure (dict; optional)

        `measure` is a number

      Or list of numbers | dict with keys:

        - func (string; optional)

    - range (dict; optional)

        `range` is a number | list of numbers | dict with keys:

        - func (string; optional)

    - target (dict; optional)

        `target` is a number | list of numbers | dict with keys:

        - func (string; optional)

- style (dict; optional)

- targetField (string; required)

- theme (optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- xField (string; optional)

- yAxis (optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdBullet'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, measureField=Component.REQUIRED, rangeField=Component.REQUIRED, targetField=Component.REQUIRED, xField=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, layout=Component.UNDEFINED, color=Component.UNDEFINED, size=Component.UNDEFINED, bulletStyle=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, legend=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'appendPadding', 'autoFit', 'bulletStyle', 'className', 'color', 'data', 'downloadTrigger', 'height', 'key', 'label', 'layout', 'legend', 'limitInPlot', 'loading_state', 'locale', 'measureField', 'meta', 'padding', 'rangeField', 'renderer', 'size', 'style', 'targetField', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'appendPadding', 'autoFit', 'bulletStyle', 'className', 'color', 'data', 'downloadTrigger', 'height', 'key', 'label', 'layout', 'legend', 'limitInPlot', 'loading_state', 'locale', 'measureField', 'meta', 'padding', 'rangeField', 'renderer', 'size', 'style', 'targetField', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'measureField', 'rangeField', 'targetField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdBullet, self).__init__(**args)
