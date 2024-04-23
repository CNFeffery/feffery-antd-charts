# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdRingProgress(Component):
    """An AntdRingProgress component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional):
    配置进度环颜色.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- innerRadius (number; optional):
    设置内环半径，取值应在0到1之间.

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

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- percent (number; required):
    必填，设置百分比数值，取值应在0到1.

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- progressStyle (dict; optional):
    设置进度环样式.

    `progressStyle` is a dict with keys:

    - func (string; optional)

- radius (number; optional):
    设置外环半径，取值应在0到1之间.

- renderer (a value equal to: 'canvas', 'svg'; optional)

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

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdRingProgress'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, percent=Component.REQUIRED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, color=Component.UNDEFINED, progressStyle=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, statistic=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'downloadTrigger', 'height', 'innerRadius', 'key', 'limitInPlot', 'loading_state', 'locale', 'padding', 'percent', 'pixelRatio', 'progressStyle', 'radius', 'renderer', 'statistic', 'style', 'theme', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'downloadTrigger', 'height', 'innerRadius', 'key', 'limitInPlot', 'loading_state', 'locale', 'padding', 'percent', 'pixelRatio', 'progressStyle', 'radius', 'renderer', 'statistic', 'style', 'theme', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['percent']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdRingProgress, self).__init__(**args)
