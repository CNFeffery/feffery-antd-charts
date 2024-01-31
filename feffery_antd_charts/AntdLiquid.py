# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdLiquid(Component):
    """An AntdLiquid component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- interactions (optional):
    交互功能项配置.

- key (string; optional)

- limitInPlot (boolean; optional)

- liquidStyle (dict; optional)

    `liquidStyle` is a dict with keys:

    - func (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- outline (dict; optional)

    `outline` is a dict with keys:

    - border (number; optional)

    - distance (number; optional)

    - style (dict; optional)

        `style` is a dict with keys:

        - stroke (string; optional)

        - strokeOpacity (number; optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- pattern (optional):
    配置图形填充贴图样式.

- percent (number; required)

- radius (number; default 0.9)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- shape (a value equal to: 'circle', 'diamond', 'triangle', 'pin', 'rect'; default 'circle')

- statistic (dict; optional)

    `statistic` is a boolean | dict with keys:

    - content (dict; optional)

        `content` is a boolean

      Or dict with keys:

        - content (string; optional)

        - customHtml (dict; optional)

            `customHtml` is a dict with keys:

            - func (string; optional)

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - offsetX (number; optional)

        - offsetY (number; optional)

        - rotate (number; optional)

        - style (dict; optional)

    - title (dict; optional)

        `title` is a boolean | dict with keys:

        - content (string; optional)

        - customHtml (dict; optional)

            `customHtml` is a dict with keys:

            - func (string; optional)

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - offsetX (number; optional)

        - offsetY (number; optional)

        - rotate (number; optional)

        - style (dict; optional)

- style (dict; optional)

- theme (optional)

- wave (dict; optional)

    `wave` is a dict with keys:

    - count (number; optional)

    - length (number; optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdLiquid'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, percent=Component.REQUIRED, radius=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, liquidStyle=Component.UNDEFINED, shape=Component.UNDEFINED, color=Component.UNDEFINED, outline=Component.UNDEFINED, wave=Component.UNDEFINED, statistic=Component.UNDEFINED, animation=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'appendPadding', 'autoFit', 'className', 'color', 'downloadTrigger', 'height', 'interactions', 'key', 'limitInPlot', 'liquidStyle', 'loading_state', 'locale', 'outline', 'padding', 'pattern', 'percent', 'radius', 'renderer', 'shape', 'statistic', 'style', 'theme', 'wave', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'appendPadding', 'autoFit', 'className', 'color', 'downloadTrigger', 'height', 'interactions', 'key', 'limitInPlot', 'liquidStyle', 'loading_state', 'locale', 'outline', 'padding', 'pattern', 'percent', 'radius', 'renderer', 'shape', 'statistic', 'style', 'theme', 'wave', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['percent']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdLiquid, self).__init__(**args)
