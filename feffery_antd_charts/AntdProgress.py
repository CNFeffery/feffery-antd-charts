# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdProgress(Component):
    """An AntdProgress component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- barWidthRatio (number; optional):
    设置进度条宽度占比，取值应在0到1之间  默认：0.5.

- className (string; optional)

- color (dict; optional):
    配置进度条颜色.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

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

- progressStyle (dict; optional):
    设置进度条样式.

    `progressStyle` is a dict with keys:

    - func (string; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- style (dict; optional)

- theme (optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdProgress'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, percent=Component.REQUIRED, barWidthRatio=Component.UNDEFINED, color=Component.UNDEFINED, progressStyle=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'barWidthRatio', 'className', 'color', 'downloadTrigger', 'height', 'key', 'limitInPlot', 'loading_state', 'locale', 'padding', 'percent', 'progressStyle', 'renderer', 'style', 'theme', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'barWidthRatio', 'className', 'color', 'downloadTrigger', 'height', 'key', 'limitInPlot', 'loading_state', 'locale', 'padding', 'percent', 'progressStyle', 'renderer', 'style', 'theme', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['percent']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdProgress, self).__init__(**args)
