# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSunburst(Component):
    """An AntdSunburst component.


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

- data (dict; required)

- downloadTrigger (string; optional)

- drilldown (dict; optional)

    `drilldown` is a dict with keys:

    - breadCrumb (dict; optional)

        `breadCrumb` is a dict with keys:

        - activeTextStyle (optional)

        - dividerText (string; optional)

        - position (a value equal to: 'top-left', 'bottom-left'; optional)

        - rootText (string; optional)

        - textStyle (optional)

    - enabled (boolean; optional)

- height (number; optional)

- hierarchyConfig (dict; optional)

    `hierarchyConfig` is a dict with keys:

    - field (string; optional)

    - ignoreParentValue (boolean; optional)

- innerRadius (number; optional)

- key (string; optional)

- label (optional)

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

- radius (number; optional)

- rawFields (list of strings; optional)

- reflect (boolean; default False)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- style (dict; optional)

- sunburstStyle (dict; optional)

    `sunburstStyle` is a dict with keys:

    - func (string; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdSunburst'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, colorField=Component.UNDEFINED, rawFields=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, hierarchyConfig=Component.UNDEFINED, drilldown=Component.UNDEFINED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, color=Component.UNDEFINED, sunburstStyle=Component.UNDEFINED, reflect=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'drilldown', 'height', 'hierarchyConfig', 'innerRadius', 'key', 'label', 'loading_state', 'locale', 'meta', 'padding', 'radius', 'rawFields', 'reflect', 'renderer', 'style', 'sunburstStyle', 'theme', 'tooltip', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'drilldown', 'height', 'hierarchyConfig', 'innerRadius', 'key', 'label', 'loading_state', 'locale', 'meta', 'padding', 'radius', 'rawFields', 'reflect', 'renderer', 'style', 'sunburstStyle', 'theme', 'tooltip', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdSunburst, self).__init__(**args)
