# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdGauge(Component):
    """An AntdGauge component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- axis (optional)

- className (string; optional)

- downloadTrigger (string; default 'download-trigger')

- endAngle (number; optional)

- gaugeStyle (dict; optional)

    `gaugeStyle` is a dict with keys:

    - func (string; optional)

- height (number; optional)

- indicator (dict; optional)

    `indicator` is a dict with keys:

    - pin (dict; optional)

        `pin` is a dict with keys:

        - style (optional)

    - pointer (dict; optional)

        `pointer` is a dict with keys:

        - style (optional)

    - shape (a value equal to: 'default', 'cursor', 'ring-cursor', 'simple'; optional)

- innerRadius (number; optional)

- interactions (optional):
    交互功能项配置.

- key (string; optional)

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

- meter (dict; optional)

    `meter` is a dict with keys:

    - stepRatio (number; optional)

    - steps (number; optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- percent (number; required)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- radius (number; default 0.95)

- range (dict; optional)

    `range` is a dict with keys:

    - color (string | list of strings; optional)

    - ticks (list of numbers; optional)

    - width (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- startAngle (number; optional)

- state (optional):
    状态样式配置.

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

    - style (optional)

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

- type (a value equal to: 'meter'; optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdGauge'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, percent=Component.REQUIRED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, range=Component.UNDEFINED, type=Component.UNDEFINED, meter=Component.UNDEFINED, gaugeStyle=Component.UNDEFINED, axis=Component.UNDEFINED, indicator=Component.UNDEFINED, statistic=Component.UNDEFINED, animation=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'appendPadding', 'autoFit', 'axis', 'className', 'downloadTrigger', 'endAngle', 'gaugeStyle', 'height', 'indicator', 'innerRadius', 'interactions', 'key', 'limitInPlot', 'loading_state', 'locale', 'meter', 'padding', 'percent', 'pixelRatio', 'radius', 'range', 'renderer', 'startAngle', 'state', 'statistic', 'style', 'theme', 'type', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'appendPadding', 'autoFit', 'axis', 'className', 'downloadTrigger', 'endAngle', 'gaugeStyle', 'height', 'indicator', 'innerRadius', 'interactions', 'key', 'limitInPlot', 'loading_state', 'locale', 'meter', 'padding', 'percent', 'pixelRatio', 'radius', 'range', 'renderer', 'startAngle', 'state', 'statistic', 'style', 'theme', 'type', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['percent']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdGauge, self).__init__(**args)
