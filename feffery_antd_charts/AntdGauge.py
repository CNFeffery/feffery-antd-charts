# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdGauge(Component):
    """An AntdGauge component.


Keyword arguments:

- id (string; optional)

- key (string; optional)

- className (string; optional)

- style (dict; optional)

- percent (number; required)

- radius (number; default 0.95)

- innerRadius (number; optional)

- startAngle (number; optional)

- endAngle (number; optional)

- width (number; optional)

- height (number; optional)

- autoFit (boolean; optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- appendPadding (number | list of numbers; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- limitInPlot (boolean; optional)

- range (dict; optional)

    `range` is a dict with keys:

    - ticks (list of numbers; optional)

    - color (string | list of strings; optional)

    - width (number; optional)

- type (a value equal to: 'meter'; optional)

- meter (dict; optional)

    `meter` is a dict with keys:

    - steps (number; optional)

    - stepRatio (number; optional)

- gaugeStyle (dict; optional)

    `gaugeStyle` is a dict with keys:

    - func (string; optional)

- axis (optional)

- indicator (dict; optional)

    `indicator` is a dict with keys:

    - pointer (dict; optional)

        `pointer` is a dict with keys:

        - style (optional)

    - pin (dict; optional)

        `pin` is a dict with keys:

        - style (optional)

    - shape (a value equal to: 'default', 'cursor', 'ring-cursor', 'simple'; optional)

- statistic (dict; optional)

    `statistic` is a boolean | dict with keys:

    - title (dict; optional)

        `title` is a boolean

      Or dict with keys:

        - style (dict; optional)

        - content (string; optional)

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - customHtml (dict; optional)

            `customHtml` is a dict with keys:

            - func (string; optional)

        - rotate (number; optional)

        - offsetX (number; optional)

        - offsetY (number; optional)

    - content (dict; optional)

        `content` is a boolean | dict with keys:

        - style (dict; optional)

        - content (string; optional)

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - customHtml (dict; optional)

            `customHtml` is a dict with keys:

            - func (string; optional)

        - rotate (number; optional)

        - offsetX (number; optional)

        - offsetY (number; optional)

    - style (optional)

- animation (optional)

- downloadTrigger (string; default 'download-trigger')

- theme (optional)

- interactions (optional):
    交互功能项配置.

- state (optional):
    状态样式配置.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdGauge'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, percent=Component.REQUIRED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, range=Component.UNDEFINED, type=Component.UNDEFINED, meter=Component.UNDEFINED, gaugeStyle=Component.UNDEFINED, axis=Component.UNDEFINED, indicator=Component.UNDEFINED, statistic=Component.UNDEFINED, animation=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'percent', 'radius', 'innerRadius', 'startAngle', 'endAngle', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'range', 'type', 'meter', 'gaugeStyle', 'axis', 'indicator', 'statistic', 'animation', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'percent', 'radius', 'innerRadius', 'startAngle', 'endAngle', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'range', 'type', 'meter', 'gaugeStyle', 'axis', 'indicator', 'statistic', 'animation', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
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
