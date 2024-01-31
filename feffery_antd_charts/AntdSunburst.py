# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSunburst(Component):
    """An AntdSunburst component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- colorField (string; optional)

- data (dict; required)

- downloadTrigger (string; default 'download-trigger')

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

- interactions (optional):
    交互功能项配置.

- key (string; optional)

- label (optional)

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

- pattern (optional):
    配置图形填充贴图样式.

- radius (number; optional)

- rawFields (list of strings; optional)

- recentlyAreaClickRecord (dict; optional)

    `recentlyAreaClickRecord` is a dict with keys:

    - data (boolean | number | string | dict | list; optional)

    - timestamp (number; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (boolean | number | string | dict | list; optional)

    - timestamp (number; optional)

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
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, colorField=Component.UNDEFINED, rawFields=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, hierarchyConfig=Component.UNDEFINED, drilldown=Component.UNDEFINED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, color=Component.UNDEFINED, sunburstStyle=Component.UNDEFINED, reflect=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyAreaClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'drilldown', 'height', 'hierarchyConfig', 'innerRadius', 'interactions', 'key', 'label', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'radius', 'rawFields', 'recentlyAreaClickRecord', 'recentlyTooltipChangeRecord', 'reflect', 'renderer', 'style', 'sunburstStyle', 'theme', 'tooltip', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'drilldown', 'height', 'hierarchyConfig', 'innerRadius', 'interactions', 'key', 'label', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'radius', 'rawFields', 'recentlyAreaClickRecord', 'recentlyTooltipChangeRecord', 'reflect', 'renderer', 'style', 'sunburstStyle', 'theme', 'tooltip', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdSunburst, self).__init__(**args)
